import os



def update_slash_depends_on_system(s):
    import platform
    slash = {
        "Windows" : "\\",
        "Darwin": "/"

    }
    platform__ = platform.system()
    context_slash = slash.get(platform__)
    
    
    context_s =  s.replace('/', context_slash)
    return context_s

    
REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath('')))

BASE_URL = "https://www.investing.com/crypto/bitcoin/news"
DATA_DIR = os.path.join(REPO_DIR, update_slash_depends_on_system("data/"))
FILE_PATH = os.path.join(DATA_DIR, update_slash_depends_on_system("articles/output.csv"))


# load chromedriver path from yaml
import yaml
with open(os.path.join(REPO_DIR, update_slash_depends_on_system("bot/bot/chrome.yaml"))) as file:
    chrome_config = yaml.full_load(file)
    CHROMEDRIVER_PATH= chrome_config['CHROME_DRIVER']


