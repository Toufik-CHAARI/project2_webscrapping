from bs4 import BeautifulSoup
import pandas as pd
import requests
import time
from urllib.parse import urljoin





page_content=[]
links=[]


'''
Step 3 : Scrapping all the requested product details from a multipage category.
This method handle the pagination with a for loop which iterates from page 
1 to 10 as long as the http reponse is 200
'''
for i in range(1,10):
    url="http://books.toscrape.com/catalogue/category/books/fiction_10/"+"page-"+str(i)+".html"
    r= requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})
    
    #if http response is not egal to 200. the script stop trying to load new pages. 
       
    if r.status_code == 200:
                
        soup = BeautifulSoup(r.content,'lxml') 
        content = soup.find('ol',class_="row")
        page_links = content.find_all('li')
        for page_link in page_links:
            ahref = page_link.find('a')['href'].replace('../../../','')
            links.append('http://books.toscrape.com/catalogue/'+ ahref)

      
          
for productlink in links:
    data=[]
    domain = "http://books.toscrape.com/"
    r = requests.get(productlink,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'lxml')
    #construction of the absolute url by concatenation with urljoin
    image_url = urljoin(domain,soup.find('img')['src'])
    category = soup.find_all('li')[2].text.strip()
    product_description = soup.find_all('p')[3].text.strip()
    product_page_url = productlink
    container = soup.find_all('div',class_='row')[1]
    title = container.find('h1').text.strip()
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
        review_rating = '0 star'
    table = soup.find("table",{"class":"table table-striped"})
    for x in table.find_all('tr'):
        for y in x.find_all('td'):
            data.append(y.text)        
    universal_product_code= data[0].strip()    
    #convert prices to float for future price analysis
    price_excluding_tax = float(data[2].strip().replace('£',''))
    price_including_tax = float(data[3].strip().replace('£',''))
    number_available = data[5].strip()    
    fulldata = {
        'Title' : title,
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
    time.sleep(1)
    
    
print(len(page_content))
df=pd.DataFrame(page_content)   
print(df.head())
df.to_csv("downloads/step3/HttpMethodSingleProductCategorySrapping.csv")



