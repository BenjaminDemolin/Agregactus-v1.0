from dotenv import dotenv_values
import Database.aa_local_database_function as localdb_f
import Webscraping.aa_webscraping_news_function as webscraping_f
import Common.aa_mail_function as mail_f
import datetime as dt
import time

secret = dotenv_values(".env")

email_address = secret["EMAIL_SENDER_ADDRESS"]
email_password = secret["EMAIL_SENDER_PASSWORD"]
receiver_email = secret["EMAIL_RECEIVER_ADDRESS"]

"""
    File name: main.py
    Description: This file contains the main function
"""

"""
    Description:
        Verify if database are good
    Parameters:
        None
    Return:
        None
"""
def verify_database():
    if(localdb_f.table_websites_exists() == False):
        localdb_f.create_websites_table()
    if(localdb_f.table_news_exists() == False):
        localdb_f.create_news_table()
    if(len(localdb_f.get_all_websites()) == 0):
        localdb_f.init_websites_table()

"""
    Description:
        Format a tweet
    Parameters:
        tweet: Tweet to format
        source: Source of the tweet
    Return:
        Formated tweet
"""
def format_tweet(tweet, source):
    return tweet + "\n(source : " + source + ")"

"""
    Description:
        Send email
    Parameters:
        None
    Return:
        None
"""
def send_email():
    try:
        data = localdb_f.get_article_to_send_by_email()
        for article in data:
            website_id = article[0]
            name = localdb_f.get_website_name_by_id(website_id)
            url = article[1]
            tweet = format_tweet(article[2], name)
            question = article[3]
            body = "url : \n" + url + "\n\n\n" + "tweet : \n" + tweet + "\n\n\n" + "question : \n" + question
            mail_sent = mail_f.send_email_gmail(email_address, email_password, receiver_email, url, body)
            if(mail_sent):
                print("email sent")
                localdb_f.update_email_sent_news_table(url)
    except Exception as e:
        print(e)
        return False

"""
    Description:
        Main function
    Parameters:
        None
    Return:
        None
"""
def main():
    while True:
        # check if database are good
        print("----VERIFY DATABASE----")
        verify_database()

        # get article list, parameter is the number of articles to get by website
        print("----GET ARTICLES----")
        dict_articles = webscraping_f.get_all_articles(1)

        #  add articles url to database
        print("----ADD ARTICLES TO DATABASE----")
        webscraping_f.add_articles_to_database(dict_articles)

        # summarize all questions of all tweets in database
        print("----SUMMARIZE ALL QUESTIONS----")
        limit_not_reached = webscraping_f.summarize_all_questions()

        # if chatgpt limit is not reached, summarize all articles and add in database
        if(limit_not_reached):
            print("----SUMMARIZE ALL ARTICLES----")
            limit_not_reached = webscraping_f.summarize_all_articles()

        # send email
        print("----SEND EMAIL----")
        send_email()

        if(limit_not_reached):
            print("--WAIT 5 MINUTE | %s--" % (dt.datetime.now().strftime("%H:%M:%S")))
            time.sleep(60*5)
        else:
            print("--WAIT A MINUTE | %s--" % (dt.datetime.now().strftime("%H:%M:%S")))
            time.sleep(60)


if __name__ == "__main__":
    main()