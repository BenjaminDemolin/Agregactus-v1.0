import Common.aa_webscrapping_function as webscrapping_f

URL = "https://www.france24.com/fr/info-en-continu/"

"""
    File name: aa_webscrapping_france24_function.py
    Description: This file contains functions to extract data from france24 website
"""

"""
    Description: 
        This function returns all articles links from france24 website. Limit is 20 articles.
    Parameters:
        None
    Return:
        articles_links: list
"""
def get_all_articles():
    try:
        return webscrapping_f.get_articles_links(URL,".news__content")[:20]
    except Exception as e:
        print(e)
        return e

"""
    Description:
        This function returns the text of an article from a given url
    Parameters:
        url: string
    Return:
        text: string
"""
def get_article_text(url):
    try:
        return webscrapping_f.find_tag(url,"article")[0].text
    except Exception as e:
        print(e)
        return e