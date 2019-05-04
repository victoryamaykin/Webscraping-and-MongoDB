from splinter import Browser
from bs4 import BeautifulSoup as bs
import datetime as dt 
import time
import pymongo
import pandas as pd

def init_browser():
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=True)

def scrape_info():
    browser = init_browser()



    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    html = browser.html
    soup = bs(html, 'html.parser')

    news_title = soup.find("div", class_="content_title").text
    print(news_title)
    news_p = soup.find("div", class_="article_teaser_body").text
    print(news_p)


    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)


    full_image_elem = browser.find_by_id('full_image')
    full_image_elem.click()

    browser.is_element_present_by_text('more info', wait_time=1)

    more_info_elem = browser.find_link_by_partial_text('more info')

    more_info_elem.click()

    html = browser.html
    soup = bs(html, 'html.parser')


    relative_image_path = soup.select_one('figure.lede a img').get("src")
    print(relative_image_path)



    url = 'https://www.jpl.nasa.gov'
    featured_image_url = url + relative_image_path
    featured_image_url




    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)




    html = browser.html
    soup = bs(html, 'html.parser')



    mars_weather = soup.find('p', class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
    mars_weather



    url =  'https://space-facts.com/mars/'
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')


    tables = pd.read_html(url)


    mars_df = tables[0]
    mars_df.columns = ["", "Value"]
    mars_df

    html_table = mars_df.to_html()
    html_table.replace('\n', '')
    html_table

    time = dt.datetime.now()


    mars_data = {
                 "Date of entry": time,
                'Article Title': news_title,
                'Summary': news_p,
                'Featured Image': featured_image_url,
                'Weather': mars_weather, 
                "Mars Facts": html_table, 
    }

    print("Data Uploaded!")

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data
