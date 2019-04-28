from splinter import Browser
from bs4 import BeautifulSoup as bs
import datetime as dt 
import time

def init_browser():
    return Browser("chrome", headless=True)

def scrape_info():
    browser = init_browser()

    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "lxml")
    relative_image_list = [img['src'] for img in soup.find_all('img', class_="fancybox-image")]
    relative_image_list = []
    for img in soup.find_all('img'):
        relative_image_list.append(img['src'])
        featured_image =  relative_image_list[-1]

    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(url)

    news_title = soup.body.find('p').text
    news_p = soup.body.find('p').text 

    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)

    mars_weather = soup.find('p', class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text

    time = dt.datetime.now()

    mars_data = ({
            'Article Title': news_title,
            'Summary': news_p,
            'Featured Image': featured_image,
            'Weather': mars_weather, 
                "Date of entry": time
    })

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data
