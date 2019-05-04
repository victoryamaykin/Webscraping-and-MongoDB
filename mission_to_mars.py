browser = Browser('chrome', headless=False)


# In[3]:


url = 'https://mars.nasa.gov/news/'
browser.visit(url)


# In[8]:


html = browser.html
soup = bs(html, 'html.parser')


# In[26]:


news_title = soup.find("div", class_="content_title").text
print(news_title)
news_p = soup.find("div", class_="article_teaser_body").text
print(news_p)


# In[17]:


url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)


# In[18]:



full_image_elem = browser.find_by_id('full_image')
full_image_elem.click()

browser.is_element_present_by_text('more info', wait_time=1)

more_info_elem = browser.find_link_by_partial_text('more info')

more_info_elem.click()

html = browser.html
soup = bs(html, 'html.parser')


# In[19]:


relative_image_path = soup.select_one('figure.lede a img').get("src")
print(relative_image_path)


# In[20]:


url = 'https://www.jpl.nasa.gov'
featured_image_url = url + relative_image_path
featured_image_url


# In[23]:


url = 'https://twitter.com/marswxreport?lang=en'
browser.visit(url)


# In[24]:


html = browser.html
soup = bs(html, 'html.parser')


# In[25]:


mars_weather = soup.find('p', class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
mars_weather


# In[46]:


url =  'https://space-facts.com/mars/'
browser.visit(url)
html = browser.html
soup = bs(html, 'html.parser')


# In[47]:


tables = pd.read_html(url)


# In[48]:


mars_df = tables[0]
mars_df.columns = ["", "Value"]
mars_df


# In[37]:


html_table = df.to_html()
html_table.replace('\n', '')
html_table


# In[3]:


url =  'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)
html = browser.html
soup = bs(html, 'html.parser')


# In[90]:


titles = []
img_urls = []

hemisphere_image_urls = []


# In[94]:


url =  'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)

# full_image_elem = browser.find_by_css('a.product-item h3')
# full_image_elem.click()

html = browser.html
soup = bs(html, 'html.parser')


# In[86]:


relative_image_url_list = []

link_list = browser.find_by_css('a.product-item h3')

print(dir(link_list[0]))


# In[95]:


link_list = browser.find_by_css('a.product-item h3')

sample = {}

link_list[0].click()

results = browser.find_by_text('Sample')
print(results)
relative_image_url = results["href"]



title = soup.find('h2', class_="title").text

sample['title':title]
sample['img_url':relative_image_url]

hemisphere_image_urls.append(sample)

browser.back()


# In[89]:


hemisphere_image_urls


# In[ ]:




