from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import datetime as dt
import requests

def scrape_all():

    # Initiate headless driver for deployment
    browser = Browser("chrome", executable_path="chromedriver", headless=True)
    news_title, news_paragraph = mars_news(browser)
    


    # Stop webdriver and return data
    browser.quit()
    # return data


def mars_news(browser):
    url = 'https://mars.nasa.gov/news/8369/nasa-seeking-partner-in-contest-to-name-next-mars-rover/'
    response = requests.get(url)
    soup = bs(response.text, 'html.parser')
    title=soup.find('h1', class_="article_title").text
    paragraph=soup.find('p').text
    return title, paragraph

    # return news_title, news_p


# def featured_image(browser):

#     # Find and click the full image button


#     try:
#        pass

#     except AttributeError:
#         pass

#     # Use the base url to create an absolute url
   

#     # return img_url


# def hemispheres(browser):


#     browser.visit(url)

#     # Click the link, find the sample anchor, return the href
   
#         # Finally, we navigate backwards
#     browser.back()

#     # return hemisphere_image_urls


# def twitter_weather(browser):

#     # return mars_weather


# def scrape_hemisphere(html_text):

#     # Soupify the html text
    
#     # Try to get href and text except if error.
#     try:
#         pass

#     except AttributeError:
#         pass


#     # return hemisphere


# def mars_facts():

#     try:
#         pass
#     except BaseException:
#         pass
       
#     # Add some bootstrap styling to <table>
#     # return df


if __name__ == "__main__":

    # If running as script, print scraped data
    print(scrape_all())
