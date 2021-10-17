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
DATA_DIR = os.path.join(REPO_DIR, update_slash_depends_on_system("data/"))
FILE_PATH = os.path.join(DATA_DIR, update_slash_depends_on_system("articles/back.txt"))
HISTORY_PATH = os.path.join(DATA_DIR, update_slash_depends_on_system("articles/history.csv"))


