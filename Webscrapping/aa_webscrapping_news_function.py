import Webscrapping.aa_webscrapping_france24_function as france24_f
import Webscrapping.aa_webscrapping_francetvinfo_function as francetvinfo_f
import Database.aa_local_database_function as localdb_f

"""
    File name: aa_webscrapping_news_function.py
    Description: This file contains functions to extract data from news websites
"""

"""
    Description: 
        This function returns all articles links from all websites. 
    Parameters:
        None
    Return:
        dict_articles: dict
"""
def get_all_articles():
    try:
        dict_articles = {}
        dict_articles["france24".lower()] = france24_f.get_all_articles()
        dict_articles["francetvinfo".lower()] = francetvinfo_f.get_all_articles()
        return dict_articles
    except Exception as e:
        print(e)
        return e

"""
    Description:
        This function adds articles url to the database
    Parameters:
        dict_articles: dict
    Return:
        None
"""
def add_articles_to_database(dict_articles):
    try:
        for website in dict_articles:
            for article in dict_articles[website]:
                article = next(iter(article))
                if not localdb_f.row_exists_news_table(article):
                    localdb_f.insert_row_news_table(website, article)
    except Exception as e:
        print(e)
        return e
