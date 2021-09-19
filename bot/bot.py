from selenium import webdriver
from chromedriver_py import binary_path # this will get you the path variable
import os
import pandas as pd

REPO_DIR = os.path.dirname(os.path.abspath(''))
BASE_URL = "https://fr.investing.com/commodities/crude-oil-news"
DATA_DIR = os.path.join(REPO_DIR, "data/")

FILE_PATH = os.path.join(DATA_DIR, "articles/output.csv")


def load_configs():
    #dotenv_path = os.path.join(env_file_location_dir, '.env')
    #load_dotenv(dotenv_path)

    #chrome_driver = os.environ.get("CHROME_DRIVER")
    #user_agent = os.environ.get("USER_AGENT")
    #return chrome_driver, user_agent
    pass 

def get_driver():
    #configs = load_configs()
    #if isinstance(configs, tuple):
        # local env dev
    #chrome_driver_path, user_agent = configs
    #print(chrome_driver_path)
    driver = webdriver.Chrome(binary_path)
    return driver

def __get_titles(driver):
        return [s.text for s in driver.find_elements_by_class_name("title")][3:13]
    
def __get_dates(driver):
        return [s.text for  s in driver.find_elements_by_xpath('.//span[@class = "date"]')]
    
def format_string(s):
    return s.replace(' - ','')

def format_date(dates):
    return list(map(format_string, dates))

def scrape(url):
    #url = base_url + '/'+ str(page)
    driver = get_driver()
    driver.get(url)
    titles = __get_titles(driver)
    dates = __get_dates(driver)
    dates = format_date(dates)
    return titles, dates

import os 
def get_urls(base_url, pagination):
    #urls = [os.path.join(BASE_URL, str(page)) for page in range(1, pagination+1)]
    urls = [base_url + '/' + str(page) for page in range(1, pagination+1)]
    return urls

def scrape_iterate(urls):
    titles = []
    dates = []
    for url in urls:
        current_titles, current_dates = scrape(url)
        titles += current_titles
        dates +=current_dates
    return titles, dates  