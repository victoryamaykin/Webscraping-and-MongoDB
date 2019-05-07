from splinter import Browser
from splinter.exceptions import ElementDoesNotExist
from selenium import webdriver

from bs4 import BeautifulSoup as bs

import pandas as pd

def init_browser():
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=True)

def scrape_info():
    browser = init_browser()
# Scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text.
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    html = browser.html
    soup = bs(html, 'html.parser')

    news_title = soup.find("div", class_="content_title").text
    print(news_title)
    news_p = soup.find("div", class_="article_teaser_body").text
    print(news_p)

# Use splinter to navigate the site and collect the featured image url
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

# Visit the Mars Weather twitter account and scrape the latest tweet

    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)

    html = browser.html
    soup = bs(html, 'html.parser')

    mars_weather = soup.find('p', class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
    mars_weather

# Visit the Mars Facts site and collect the table 

    url =  'https://space-facts.com/mars/'
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')

# Convest the table to html using pandas 

    tables = pd.read_html(url)

    mars_df = tables[0]
    mars_df.columns = ["", "Value"]
    mars_df.reset_index(drop = True) 

    html_table = mars_df.to_html()
    html_table.replace('\n', '')
    html_table

# Visit the USDS Astrogeology site and collect the high res images for each hemisphere

    url =  'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')

    results = soup.find_all('h3')
    links = ['https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced','https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced','https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced', 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced']
    
    titles = []
    
    hemisphere_image_urls = []

    for result in results:
            try:
                title = result.text
                
                titles.append(title)
            except AttributeError as e: 
                print(e)
                
    for link in links:  
            try:
                browser.visit(link)
                html = browser.html
                soup = bs(html, 'html.parser')
                find = browser.find_by_text('Sample')
                image_url = find["href"]
                hemisphere_image_urls.append(image_url)
                
            except AttributeError as e: 
                print(e)

# Append this data to a dictionary to be stored in MongoDB NoSQL

    mars_data = {
        'Article_Title': news_title,
        'Summary': news_p,
        'Featured_Image': featured_image_url,
        'Weather': mars_weather, 
        "Mars_Facts": html_table, 
        "Title1": titles[0],
        "Hemisphere1": hemisphere_image_urls[0],
        "Title2": titles[1],
        "Hemisphere2": hemisphere_image_urls[1],
        "Title3": titles[2],
        "Hemisphere3": hemisphere_image_urls[2],
        "Title4": titles[3],
        "Hemisphere4": hemisphere_image_urls[3]
    }

    print("Data Uploaded!")

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data
