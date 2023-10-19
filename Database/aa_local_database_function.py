import Database.aa_global_database_function as globaldb_f
from dotenv import dotenv_values

secret = dotenv_values("./.env")

TABLE_WEBSITES_NAME = "websites"
TABLE_WEBSITES_COLUMNS = "website_id SERIAL PRIMARY KEY, name TEXT NOT NULL UNIQUE,url TEXT NOT NULL UNIQUE"

TABLE_NEWS_NAME = "news"
TABLE_NEWS_COLUMNS = " news_id SERIAL PRIMARY KEY, website_id INT REFERENCES websites (website_id), url TEXT NOT NULL UNIQUE, ia_tweet TEXT"

host = secret["HOST"]
dbname = secret["DB_NAME"]
user = secret["USER"]
password = secret["PASSWORD"]
port = secret["PORT"]


"""
    File name: aa_local_database_function.py
    Description: This file contains functions to interact with agregactus database
"""

connector = globaldb_f.Postgres_db(host,dbname,user,password,port)

def create_websites_table():
    return connector.create_table(TABLE_WEBSITES_NAME,TABLE_WEBSITES_COLUMNS)

def create_news_table():
    return connector.create_table(TABLE_NEWS_NAME,TABLE_NEWS_COLUMNS)

def create_tables():
    return create_websites_table() & create_news_table()

def reset_websites_table():
    return connector.reset_table(TABLE_WEBSITES_NAME)

def reset_news_table():  
    return connector.reset_table(TABLE_NEWS_NAME)

def reset_tables():
    return reset_news_table() & reset_websites_table()

def delete_websites_table():
    return connector.delete_table(TABLE_WEBSITES_NAME)

def delete_news_table():
    return connector.delete_table(TABLE_NEWS_NAME)

def delete_tables():
    return delete_news_table() & delete_websites_table()

def insert_row_websites_table(name,url):
    return connector.insert_row(TABLE_WEBSITES_NAME,"name,url","'%s','%s'" % (name.lower(),url))

def get_website_id(name):
    return connector.select_rows(TABLE_WEBSITES_NAME,"website_id","name = '%s'" % (name.lower()))

def insert_row_news_table(website_name,url,ia_tweet=None):
    website_id = get_website_id(website_name)[0][0]
    if ia_tweet is None:
        ia_tweet = "NULL"
    return connector.insert_row(TABLE_NEWS_NAME,"website_id,url,ia_tweet","%s,'%s','%s'" % (website_id,url,ia_tweet))

def update_row_website_table(name,url,new_name = None):
    website_id = get_website_id(name)[0][0]
    if(new_name is None):
        return connector.update_row(TABLE_WEBSITES_NAME,"url" ,"'%s'" % (url),"website_id = %s" % (website_id))
    else:
        return connector.update_row(TABLE_WEBSITES_NAME,"name,url" ,"'%s','%s'" % (new_name.lower(),url),"website_id = %s" % (website_id))

def update_row_news_table(url,ia_tweet=None):
    if ia_tweet is None:
        ia_tweet = "NULL"
    return connector.update_row(TABLE_NEWS_NAME,"ia_tweet = '%s'" % (ia_tweet),"url = '%s'" % (url))

def row_exists_news_table(url):
    if(len(connector.select_rows(TABLE_NEWS_NAME,"url = '%s'" % (url))) == 0):
        return False
    return connector.select_rows(TABLE_NEWS_NAME,"url = '%s'" % (url))[0][0]