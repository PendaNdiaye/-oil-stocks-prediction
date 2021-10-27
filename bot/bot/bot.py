import os
from selenium import webdriver
from datetime import datetime
from bot.tools import normalize_date
from bot.settings import *


class HeadersData:
    base_url = BASE_URL

    def scrape(self, **kwargs):
        url = self.base_url
        if 'page' in kwargs: # ensemble des pages
            page = kwargs.get('page') #récupére la page
            url = os.path.join(url, str(page)) #joint un ou plusieurs composants de chemin
        chrome_driver_path = CHROMEDRIVER_PATH #récupére le chemin
        driver = webdriver.Chrome(chrome_driver_path) #ouvre le web
        driver.get(url)
        titles = self.__get_titles(driver)
        dates = self.__get_dates(driver)
        # process dates before push them to backend
        dates = [normalize_date(date) for date in dates]
        chronos = [datetime.now().strftime("%m/%d/%Y, %H:%M:%S")] * len(dates)
        # return data as dict
        scraped_data = []
        for data in zip(
            chronos,
            titles,
            dates):
            s = dict()
            s['scraping_date'], s['new_header'], s['public_date'] = data
            scraped_data.append(s)
        return scraped_data

    def current_scraper(self):
        return self.scrape()

    def back_scraper(self, pagination_low, pagination_up, **kwargs):
        lower = pagination_low
        upper = pagination_up
        history_data = []
        for page in range(lower, upper):
            history_data += self.scrape(page=page)
        return history_data


    @staticmethod
    def __get_titles(driver, limit=15): #récupére les titres
        return [s.text for s in driver.find_elements_by_class_name("title")[11:limit + 11]]

    @staticmethod
    def __get_dates(driver, limit=15): #récupère les dates
        return [s.text for  s in driver.find_elements_by_xpath('.//span[@class = "date"]')[:limit]]

