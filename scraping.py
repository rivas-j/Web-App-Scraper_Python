# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import datetime as dt

def scrape_all():
    # Initiate headless driver for deployment
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    news_title, news_paragraph = mars_news(browser)
    
    # Run all scraping functions and store results in dictionary
    data = {
          "news_title": news_title,
          "news_paragraph": news_paragraph,
          "featured_image": featured_image(browser),
          "facts": mars_facts(),
          "last_modified": dt.datetime.now(),
          "hemisphere": hemisphere_data(browser)
    }

    # Stop webdriver and return data
    browser.quit()

    return data  
    

def mars_news(browser):

    # Scrape Mars News
    # Visit the mars nasa news site
    url = 'https://data-class-mars.s3.amazonaws.com/Mars/index.html'
    browser.visit(url)

    # Optional delay for loading the page
    browser.is_element_present_by_css('div.list_text', wait_time=1)

    # Convert the browser html to a soup object and then quit the browser
    html = browser.html
    news_soup = soup(html, 'html.parser')

    # Add try/except for error handling
    try:
        slide_elem = news_soup.select_one('div.list_text')
        # Use the parent element to find the first 'a' tag and save it as 'news_title'
        news_title = slide_elem.find('div', class_='content_title').get_text()
        # Use the parent element to find the paragraph text
        news_p = slide_elem.find('div', class_='article_teaser_body').get_text()

    except AttributeError:
        return None, None

    return news_title, news_p


def featured_image(browser):
    # Visit URL
    url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
    browser.visit(url)

    # Find and click the full image button
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')

    # Add try/except for error handling
    try:
        # Find the relative image url
        img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')

    except AttributeError:
        return None

    # Use the base url to create an absolute url
    img_url = f'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/{img_url_rel}'

    return img_url

def mars_facts():
    print("collecing the facts")
    # Add try/except for error handling
    try:
        # Use 'read_html' to scrape the facts table into a dataframe
        df = pd.read_html('https://data-class-mars-facts.s3.amazonaws.com/Mars_Facts/index.html')[0]
        print("collected the facts")
    except BaseException:
        print("base exception")
        return None

    # Assign columns and set index of dataframe
    df.columns=['Description', 'Mars', 'Earth']
    df.set_index('Description', inplace=True)

    # Convert dataframe into HTML format, add bootstrap
    return df.to_html(classes="table table-striped")

def hemisphere_data(browser):
    print("scraping hemisphere data")
    # Use browser to visit the URL 
    url = 'https://marshemispheres.com/'
    browser.visit(url)


    # Create a list to hold the images and titles.
    hemisphere_image_urls = []


    html = browser.html
    hemi_soup = soup(html, 'html.parser')

    # Write code to retrieve the image urls and titles for each hemisphere.

    hemi_name_list_raw = hemi_soup.find_all('h3')
    hemi_name_list = []
    hemi_list_index = 0

    hemi_name_list_raw.pop(-1)


    for hemi_name in hemi_name_list_raw:
        hemi_name_list.append(hemi_name.text)


    for image in hemi_name_list:
        hemispheres = {}
        # click on each hemisphere link
        browser.links.find_by_partial_text(hemi_name_list[hemi_list_index]).click()
        hemi_list_index = hemi_list_index + 1
             
        # retrieve the full-resolution image URL string and title for the hemisphere image
        html = browser.html
        img_soup = soup(html, 'html.parser')
        img_url_elem = img_soup.find('li')
        img_url_rel = img_url_elem.find('a').get('href')
        img_url = f'https://data-class-mars-hemispheres.s3.amazonaws.com/Mars_Hemispheres/{img_url_rel}'
        
        img_title_elem = img_soup.find('h2')
        img_title = img_title_elem.get_text()
        
        hemispheres['img_url']=img_url
        hemispheres['title']=img_title
        hemisphere_image_urls.append(hemispheres)
        # use browser.back() to navigate back to the beginning to get the next hemisphere image
        browser.back()



    # Print the list that holds the dictionary of each image url and title.
    return hemisphere_image_urls



if __name__ == "__main__":
    # If running as script, print scraped data
    print(scrape_all())