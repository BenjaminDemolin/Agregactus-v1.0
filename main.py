import Common.aa_webscrapping_function as aawebf

# URL = "https://fr.investing.com/news/latest-news"

# #print(aawebf.get_articles_links(URL,"article",True))

# URL = "https://www.france24.com/fr/info-en-continu/"

# print(aawebf.get_articles_links(URL,".news__content"))

# URL = "https://www.france24.com/fr/info-en-continu/20230906-wall-street-termine-en-baisse-prises-de-b%C3%A9n%C3%A9fices-sur-un-march%C3%A9-sans-entrain"

# print(aawebf.find_tag(URL,"article")[0].text)

# URL = "https://fr.investing.com/news/economy/crash-boursier-et-recession-au-printemps-selon-david-rosenberg-2205503"

# text = aawebf.find_tag(URL,"WYSIWYG articlePage",True,True)

# array = aawebf.find_tag_text(text,"p",True)

# for a in array:
#     print(a.text)

import Webscrapping.aa_webscrapping_francetvinfo_function as aa_francetvinfo

#print(aa_francetvinfo.get_article_text("https://www.francetvinfo.fr/faits-divers/police/ce-que-l-on-sait-de-la-collision-mortelle-entre-un-adolescent-en-deux-roues-et-une-voiture-de-police-dans-les-yvelines_6048275.html"))
#print(aa_francetvinfo.get_all_articles())

import Webscrapping.aa_webscrapping_france24_function as aa_france24

#print(aa_france24.get_all_articles())

import Database.aa_global_database_function as aagdbf

#aagdbf.Postgres_db("localhost","PlottingMate","plottingmate_administrator","Pcc2S47AF8spb2",5432)

import Database.aa_local_database_function as aaldbf


#print(aaldbf.reset_tables())
#print(aaldbf.delete_tables())
#print(aaldbf.create_tables())
#aaldbf.insert_row_websites_table("france24","https://www.france24.com/fr/info-en-continu/")
#print(aaldbf.get_website_id("france24"))
#aaldbf.insert_row_websites_table("francetvinfo","https://www.francetvinfo.fr/")

#print(aaldbf.insert_row_news_table("France24","https://www.france24.com/fr/info-en-continu/20230906-wall-street-termine-en-baisse-prises-de-b%C3%A9n%C3%A9fices-sur-un-march%C3%A9-sans-entrain"))
#print(aaldbf.update_row_news_table("https://www.france24.com/fr/info-en-continu/20230906-wall-street-termine-en-baisse-prises-de-b%C3%A9n%C3%A9fices-sur-un-march%C3%A9-sans-entrain",content="tgztgz",ia_tweet="qfvdfv"))

import Webscrapping.aa_webscrapping_news_function as news_f

#articles = aawebscrf.get_all_articles()

#print(articles)
#print(aaldbf.row_exists_news_table("https://www.france24.com/fr/info-en-continu/20230906-wtreet-termine-en-baisse-prises-de-b%C3%A9n%C3%A9fices-sur-un-march%C3%A9-sans-entrain"))
articles = news_f.get_all_articles()
#print(articles)
#print(str(articles['france24'][0]).strip("{").strip("}").strip("'"))
#print(aa_france24.get_article_text(str(articles['france24'][0]).strip("{").strip("}").strip("'")))
#news_f.add_articles_to_database(articles)

text = aa_france24.get_article_text(str(articles['france24'][0]).strip("{").strip("}").strip("'"))

import Common.aa_openai_function as openai_f
print(openai_f.resume_article_chatgpt(text))
#print(openai_f.article_category_chatgpt(text))