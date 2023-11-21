import os
from dotenv import dotenv_values

"""
    This file contains all the global variables used in the project
"""

secret = dotenv_values(".env")

"""
    Website table. Contains the list of websites to scrap
"""
TABLE_WEBSITES_NAME = "websites"
TABLE_WEBSITES_COLUMNS = "website_id SERIAL PRIMARY KEY, name TEXT NOT NULL UNIQUE,url TEXT NOT NULL UNIQUE"
TABLE_WEBSITES_INIT = [["france24","https://www.france24.com/fr/info-en-continu/"],
                       ["francetvinfo","https://www.francetvinfo.fr/"]]

"""
    News table. Contains the list of news scrapped
"""
TABLE_NEWS_NAME = "news"
TABLE_NEWS_COLUMNS = " news_id SERIAL PRIMARY KEY, website_id INT REFERENCES websites (website_id), url TEXT NOT NULL UNIQUE, ia_tweet TEXT, question TEXT, date BIGINT, email_sent BOOLEAN DEFAULT FALSE"

def load_var(var_name):
    try:
        if(os.environ.get(var_name) is not None):
            return os.environ.get(var_name)
        elif(secret[var_name] is not None):
            return secret[var_name]
    except:
        print("Error while loading variable " + var_name)
        return None
