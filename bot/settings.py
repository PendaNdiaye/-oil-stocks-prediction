import os


REPO_DIR = os.path.dirname(os.path.abspath(''))
BASE_URL = "https://www.investing.com/crypto/bitcoin/news"
DATA_DIR = os.path.join(REPO_DIR, "data/")

FILE_PATH = os.path.join(DATA_DIR, "articles/output.csv")
CHROMEDRIVER_PATH = '/usr/local/bin/chromedriver'
