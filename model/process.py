from selenium import webdriver
from chromedriver_py import binary_path # this will get you the path variable
import os
import pandas as pd

REPO_DIR = os.path.dirname(os.path.abspath(''))
BASE_URL = "https://fr.investing.com/commodities/crude-oil-news"
DATA_DIR = os.path.join(REPO_DIR, "model/")

FILE_PATH = os.path.join(DATA_DIR, "output_process.csv")

def register_ag(titles, dates, file_path):
    with open(file_path, "w") as csv_file:
        for title, date in zip(titles, dates):
            csv_file.write(title)
            csv_file.write("|")
            csv_file.write(date)   
            csv_file.write("\n")
    return