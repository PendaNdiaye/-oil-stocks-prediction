from selenium import webdriver
from chromedriver_py import binary_path # this will get you the path variable
import os
import pandas as pd

import hashlib
import requests
#from selenium import webdriver
from datetime import datetime
import psycopg2
from settings import (
    CONFIG_PATH,   
)
from exceptions import (
    RegisterModeException,
    EmptyNewsPageException,
)
from docker_env import is_dot_docker_env_there
import yaml
from tools import normalize_date
from config import get_driver

REPO_DIR = os.path.dirname(os.path.abspath(''))
BASE_URL = "https://www.investing.com/crypto/bitcoin"
DATA_DIR = os.path.join(REPO_DIR, "data/")

FILE_PATH = os.path.join(DATA_DIR, "articles/output.csv")


def load_configs():
    #dotenv_path = os.path.join(env_file_location_dir, '.env')
    #load_dotenv(dotenv_path)

    #chrome_driver = os.environ.get("CHROME_DRIVER")
    #user_agent = os.environ.get("USER_AGENT")
    #return chrome_driver, user_agent
    pass 

#def get_driver():
    #configs = load_configs()
    #if isinstance(configs, tuple):
        # local env dev
    #chrome_driver_path, user_agent = configs
    #print(chrome_driver_path)
 #   driver = webdriver.Chrome(binary_path)
  #  return driver




class GoldNewsRetriever:

    def __init__(self):
        self.base_url = BASE_URL

    def scrape(self, **kwargs):
        driver, user_agent = get_driver()
        url = self.base_url
        current = True
        if 'page' in kwargs:
            current = False
            page = kwargs.get('page')
            url = os.path.join(url, str(page))
            docker_env = is_dot_docker_env_there()
            if docker_env:
                response = requests.get(url=url)
            else:
                headers = {'User-Agent': user_agent}
                response = requests.get(url=url, headers=headers)
            if len(response.history) == 1:
                #raise Exception("No data retrieved")
                raise EmptyNewsPageException(page)
        driver.get(url)
        titles = self.__get_titles(driver)
        dates = self.__get_dates(driver)
        # process dates before push them to backend
        norm_dates = [normalize_date(date) for date in dates]
        dates = norm_dates
        sources = self.__get_sources(driver)
        hashes = [hashlib.md5(title.encode()).hexdigest() for title in titles]
        chronos = [datetime.now().strftime("%m/%d/%Y, %H:%M:%S")] * len(hashes)
        # return data as dict
        scraped_data = []
        for data in zip(
            hashes,
            chronos,
            titles,
            sources,
            dates):
            s = dict()
            s['header_hash'], s['scraping_date'], s['new_header'], s['source'], s['public_date'] = data
            scraped_data.append(s)
        return scraped_data

    def current_scraper(self):
        return self.scrape()

    def back_scraper(self, pagination_low, pagination_up):
        lower = pagination_low
        upper = pagination_up
        history_data = []
        for page in range(lower, upper):
            print(page)
            history_data += self.scrape(page=page)
            print("ok")
        return history_data


    @staticmethod
    def __get_titles(driver, limit=15):
        return [s.text for s in driver.find_elements_by_class_name("title")[11:limit + 11]]

    @staticmethod
    def __get_dates(driver, limit=15):
        return [s.text for  s in driver.find_elements_by_xpath('.//span[@class = "date"]')[:limit]]

    @staticmethod
    def __get_sources(driver, limit=15):
        return [s.text for s in driver.find_elements_by_xpath('//span[contains(text(), "By")]')[:limit]]