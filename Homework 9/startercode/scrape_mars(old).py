from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import datetime as dt
import requests

def scrape_all():

    # Initiate headless driver for deployment
    browser = Browser("chrome", executable_path="chromedriver", headless=True)
    news_title, news_paragraph = mars_news(browser)
    twitter_weather(browser)
    featured_image(browser)
    hemispheres(browser)
    mars_facts()

    # Stop webdriver and return data
    browser.quit()

def mars_news(browser):
    url = 'https://mars.nasa.gov/news/8369/nasa-seeking-partner-in-contest-to-name-next-mars-rover/'
    response = requests.get(url)
    soup = bs(response.text, 'html.parser')
    title=soup.find('h1', class_="article_title").text
    paragraph=soup.find('p').text
    return title, paragraph

def featured_image(browser):     
 # Find and click the full image button
    url="https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    nasaurl="https://www.jpl.nasa.gov"
    response = requests.get(url)
    soup = bs(response.text, 'html.parser')
    image=soup.find('a', class_="button fancybox")
    image=image.get("data-link")
    image
   # get the image page
    imgurl=nasaurl+str(image)
    imgurl
    imgresponse=requests.get(imgurl)
    soup = bs(imgresponse.text, 'html.parser')
    mainimg=soup.find('img', class_="main_image").get("src")
    mainimg=nasaurl+str(mainimg)
    mainimg   
    # return img_url
    return mainimg

def hemispheres(browser):
    baseurl="https://astrogeology.usgs.gov"
    findurl="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    response = requests.get(findurl)
    soup = bs(response.text, 'html.parser')
    mainpages=soup.find_all("a", class_="itemLink product-item")
    hemispheresInfo=[]
    for title in mainpages:
        imgurl=title.get("href")
        imgurl=baseurl+str(imgurl)
        imgresponse=requests.get(imgurl)
        imgsoup = bs(imgresponse.text, 'html.parser')
        imgreal=imgsoup.find("div", class_="downloads")
        imgreal=imgreal.find("a").get("href")
        dic={"title":title.text,"imgurl":imgreal}
        hemispheresInfo.append(dic)
    
    return hemispheresInfo


def twitter_weather(browser):

    # return mars_weather


# def scrape_hemisphere(html_text):

#     # Soupify the html text
    
#     # Try to get href and text except if error.
#     try:
#         pass

#     except AttributeError:
#         pass


#     # return hemisphere


def mars_facts():
    
    facturl="https://space-facts.com/mars/"
    ftables = pd.read_html(facturl)
    df = ftables[0]
    df.columns = ["Description","Value"]
    df.set_index('Description', inplace=True)
    fact_table = df.to_html()
    fact_table.replace('\n', '')
    return fact_table

# if __name__ == "__main__":
#     app.run(debug=True)
#     # If running as script, print scraped data
#     # print(scrape_all())
