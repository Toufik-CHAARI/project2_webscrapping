from bs4 import BeautifulSoup
import pandas as pd
import requests
import time
from urllib.parse import urljoin
import os
import re





'''
Step 4 and 5 -  : scrapping and saving all products from all the 
website categories in a separate csv file for each category as well
as all the product images.
'''


url1 = []
cat = []
url = 'http://books.toscrape.com/index.html'
data_per_category = {} #empty dictionnary

r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
soup = BeautifulSoup(r.content, 'lxml')
categories = soup.find_all('div', class_='side_categories')

for category in categories:
    atag = category.find_all('a')[1:]
    #ignore the Books "li" tag
    for h in atag:
        catename = h['href'].split('/')[3]
        cat.append(catename)
        url1.append(urljoin('http://books.toscrape.com/', h['href']))
        data_per_category[catename] = []  
        '''
        data_per_category will become a dictionnary of list
        where category name is key and the list the value 
        We Initialize data_per_category[catename] as an empty list here 
        '''
print('list of category page with empty list : ', data_per_category)


def scrape_category_products(category_url, catename):
    links =[]
    while True :
        print('list of category pages :',category_url)
        r = requests.get(category_url,headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(r.content,'lxml') 
        content = soup.find('ol',class_="row")
        if content is None:
            break  # Handle the case when 'content' is missing
        page_links = content.find_all('li')        
        for page_link in page_links:
            ahref = page_link.find('a')['href'].replace('../../../','')
            links.append(urljoin('http://books.toscrape.com/catalogue/',ahref))
        
        # this condition check if there's a next button and construct
        #the absolute url of the next page as long as there is one.    
        
        nextpage = soup.find('li',class_='next')    
        if nextpage:
            next_url = nextpage.find('a')['href']
            category_url = urljoin(category_url, next_url)
        else:
            break

    for productlink in links:
        data = []
        domain = "http://books.toscrape.com/"
        r = requests.get(productlink,headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(r.content,'lxml')
        #construction of the absolute url by concatenation with urljoin
        image_url = urljoin(domain,soup.find('img')['src'])
        alt = soup.find('img')['alt']
        alt = re.sub(r'\(.*?\)','',alt)
        #regex which remove any text within parentheses
        directory = "downloads/images/"
        os.makedirs(directory, exist_ok=True)
        #create the folder if it doesn't exist
        filepath = os.path.join(directory,alt.replace('/','').replace('/', '').replace(' ','_').strip() + '.png')
        with open(filepath,'wb') as f:
            image = requests.get(image_url)
            f.write(image.content)
        print(alt,' : is saved ')
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
        universal_product_code = data[0].strip()    
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
        
        #Add the data for this product to the corresponding category
        data_per_category[catename].append(fulldata)
        #time.sleep(1)
        
for category_url, catename in zip(url1, cat):
    #allow to iterate within the tuple(url1, cat)
    scrape_category_products(category_url, catename)          

   
# Write data to a separate CSV file for each category
for category, data in data_per_category.items():
    df = pd.DataFrame(data)
    df.to_csv(f"downloads/step4_et_5/{category}_ProductCategoriesScraping.csv")
    print(category, 'csv file is saved')


