import os
from selenium import webdriver
from datetime import datetime
from tools import normalize_date
from settings import *


class HeadersData:
    base_url = BASE_URL

    def scrape(self, **kwargs):
        url = self.base_url
        if 'page' in kwargs:
            page = kwargs.get('page')
            url = os.path.join(url, str(page))
        chrome_driver_path = CHROMEDRIVER_PATH
        if 'chrome_driver_path' in kwargs:
            chrome_driver_path = kwargs.get('chrome_driver_path')
        driver = webdriver.Chrome(chrome_driver_path)
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
        if 'chrome_driver_path' in kwargs:
            chrome_driver_path = kwargs.get('chrome_driver_path')
        else:
            chrome_driver_path = None
        lower = pagination_low
        upper = pagination_up
        history_data = []
        for page in range(lower, upper):
            print(page)
            if chrome_driver_path is None:
                history_data += self.scrape(page=page)
            else:
                history_data += self.scrape(page=page, chrome_driver_path=chrome_driver_path)
            print("ok")
        return history_data


    @staticmethod
    def __get_titles(driver, limit=15):
        return [s.text for s in driver.find_elements_by_class_name("title")[11:limit + 11]]

    @staticmethod
    def __get_dates(driver, limit=15):
        return [s.text for  s in driver.find_elements_by_xpath('.//span[@class = "date"]')[:limit]]

