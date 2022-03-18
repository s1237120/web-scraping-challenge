from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


def scrape():
    # browser = init_browser()
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    mars_data = {}
    
    url1 = 'https://redplanetscience.com/'
    browser.visit(url1)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    news_title = soup.find_all('div', class_='content_title')[0].text
    news_p = soup.find_all ('div', class_= 'article_teaser_body')[0].text
    news_title

    url2 ="https://spaceimages-mars.com/"
    browser.visit(url2)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    findimage = soup.find_all('img',class_='headerimage')
    imgPath=soup.find_all('img')[1]['src']
    featured_image_url = url2+imgPath
    featured_image_url

    url3 = 'https://galaxyfacts-mars.com'
    tables = pd.read_html(url3)
    df=tables[1]

    html_table = df.to_html()
    html_table.replace('\n', '')
    html_table

    url3 = 'https://marshemispheres.com/'
    browser.visit(url3)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    results = soup.find_all('div', class_='description')
    hemiImgUrl = []

    for result in results:
        try:
            title = result.find('h3').text
            imgLink = result.a['href']
            url4 = f"https://marshemispheres.com/" + imgLink
            browser.visit(url4)
            html = browser.html
            soup = BeautifulSoup(html, 'html.parser')
            output = soup.find('img', class_= "wide-image")
            dlLink = output['src']
            imgUrl = f"https://marshemispheres.com/" + dlLink

            if (title and dlLink):
                print(title)
                print(f"https://marshemispheres.com/" + dlLink)
                
                hemiDict = { 
                    'Title' :title, 
                    'Img_Url': imgUrl}
                
                hemiImgUrl.append(hemiDict)
                
        except Exception as error:
            print(error)


    mars_data = {

    }
    # Quit the browser
    browser.quit()

    return mars_data
