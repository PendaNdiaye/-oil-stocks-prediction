import os


REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath('')))

BASE_URL = "https://www.investing.com/crypto/bitcoin/news"
DATA_DIR = os.path.join(REPO_DIR, "data/")
FILE_PATH = os.path.join(DATA_DIR, "articles/output.csv")


# load chromedriver path from yaml
import yaml
with open(os.path.join(REPO_DIR, "bot/bot/chrome.yaml")) as file:
    chrome_config = yaml.full_load(file)
    CHROMEDRIVER_PATH= chrome_config['CHROME_DRIVER']

