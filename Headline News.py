

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

def news():

	#Below are some news websites if you want get the new just uncomment...
        #The paricular website and get the instant news in python
        #my_url="https://news.google.com/news/rss?ned=in&hl=en-IN"
        #my_url = "http://www.eenaduindia.com/RSS/SectionRssFeed.aspx?Id=13&Main=2"
        #my_url = "http://www.cinejosh.com/rss-feed/1/english.html"

        my_url = "http://www.thehindubusinessline.com/?service=rss"
        
        #Opening the entered URL
        Client=urlopen(my_url)

        html_page=Client.read()
        Client.close()

        soup_page=soup(html_page,"html.parser")
        news_headlines=soup_page.findAll("item")
	
        for news in news_headlines:
                print(news.title.text)
                print(news.description.text)
                print("-" * 90)
			
        n=input()

news()	
