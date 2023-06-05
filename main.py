from bs4 import BeautifulSoup
import pandas as pd
import requests
import time
from urllib.parse import urljoin






page_content=[]

data=[]
domain="http://books.toscrape.com/"
url="http://books.toscrape.com/catalogue/the-black-maria_991/index.html"
r= requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})
soup = BeautifulSoup(r.content,'html.parser')
#construction of the absolute url via concatenation

image_url = urljoin(domain,soup.find('img')['src'])
category = soup.find_all('li')[2].text.strip()
product_description= soup.find_all('p')[3].text.strip()
#here we need a container since we have "p" tag with star attributes at the bottom of the page
container = soup.find_all('div',class_='row')[1]
title = container.find('h1').text.strip()
#here we getting the number of stars from the star rating class
if container.find('p',class_='star-rating One') :
    review_rating = '1 star'
elif container.find('p',class_='star-rating Two'):
    review_rating = '2 stars'
elif container.find('p',class_='star-rating Three'):
    review_rating = '3 stars'
elif container.find('p',class_='star-rating Four'):
    review_rating = '4 stars'
elif container.find('p',class_='star-rating Five'):
    review_rating = '5 stars'
else:
    review_rating='0 star'
product_page_url=url
table = soup.find("table",{"class":"table table-striped"})
for x in table.find_all('tr'):
    for y in x.find_all('td'):
        data.append(y.text)
universal_product_code= data[0].strip()
#convert prices to float for future price analysis
price_excluding_tax= float(data[2].strip().replace('£',''))
price_including_tax= float(data[3].strip().replace('£',''))
number_available= data[5].strip()
fulldata = {
    'Title':title,
    'Category': category,
    'Image Url': image_url,    
    'product_description': product_description,
    'Url': product_page_url,
    'Upc': universal_product_code,
    'Price_excluding_tax': price_excluding_tax,
    'Price_including_tax': price_including_tax,
    'Number Available': number_available,
    'review_rating' : review_rating,
    }
page_content.append(fulldata)



print(len(page_content))

df=pd.DataFrame(page_content)   
print(df.head())
df.to_csv("downloads/step1/SingleProductSrapping.csv")
