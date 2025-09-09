# Books to Scrape - Comprehensive Web Scraping Project

**Python Version : 3.6.5**

## Project Overview

This project is a comprehensive web scraping solution designed to extract and organize book data from the Books to Scrape website (http://books.toscrape.com). The application systematically scrapes all available book categories, extracts detailed product information, downloads product images, and organizes the data into structured CSV files for analysis.

## Features

### 🎯 **Complete Category Coverage**
- Automatically discovers and processes all 50+ book categories from the website
- Handles pagination across multiple pages within each category
- Extracts data from every available book in the catalog

### 📊 **Comprehensive Data Extraction**
For each book, the scraper collects:
- **Product Details**: Title, UPC, category, product description
- **Pricing Information**: Price excluding tax, price including tax
- **Availability**: Stock status and quantity available
- **Quality Metrics**: Customer review ratings (1-5 stars)
- **Media**: High-resolution product images
- **Navigation**: Direct URLs to product pages

### 🖼️ **Image Management**
- Downloads all product images in high quality
- Organizes images in a dedicated `downloads/images/` directory
- Sanitizes filenames for cross-platform compatibility
- Uses descriptive naming based on book titles

### 📁 **Organized Data Output**
- Creates separate CSV files for each book category
- Generates over 50 category-specific datasets
- Maintains data integrity with proper encoding and formatting
- Enables easy analysis and filtering by category

### ⚡ **Robust Architecture**
- Implements proper error handling for missing content
- Uses respectful scraping practices with appropriate delays
- Handles dynamic pagination automatically
- Manages large-scale data processing efficiently

## Technical Implementation

### **Core Technologies**
- **BeautifulSoup4**: HTML parsing and content extraction
- **Pandas**: Data manipulation and CSV generation
- **Requests**: HTTP requests and image downloading
- **LXML**: Fast XML/HTML processing

### **Data Processing Pipeline**
1. **Category Discovery**: Scans the main page to identify all book categories
2. **URL Generation**: Constructs absolute URLs for each category page
3. **Pagination Handling**: Automatically follows "next page" links
4. **Product Extraction**: Scrapes detailed information from individual product pages
5. **Image Download**: Retrieves and saves product images locally
6. **Data Organization**: Structures data into category-specific CSV files

### **Data Structure**
Each CSV file contains the following columns:
- `Title`: Book title
- `Category`: Book category/genre
- `Image Url`: Direct link to product image
- `product_description`: Detailed book description
- `Url`: Direct link to product page
- `Upc`: Universal Product Code
- `Price_excluding_tax`: Price without tax (in GBP)
- `Price_including_tax`: Price with tax (in GBP)
- `Number Available`: Stock availability information
- `review_rating`: Customer rating (1-5 stars)

## Use Cases

This project is ideal for:
- **Market Research**: Analyzing book pricing and availability across categories
- **Data Analysis**: Studying trends in book categories and customer ratings
- **E-commerce Development**: Understanding product data structure and organization
- **Educational Purposes**: Learning web scraping techniques and data processing
- **Price Monitoring**: Tracking price changes across different book categories

## How to run this project
***

### -Open your terminal

### -Create a folder 

 'mkdir bookstoscrape'

### -Change directory

'cd bookstoscrape'

### -Install Virtual Environment:

 'pip install virtualenv'
 
#### -Create Virtual Environment
 'python3 -m venv env'
 
### -Activate Virtual Environment
'source env/bin/activate'

### -Clone the project by running the following command
'git clone https://github.com/Toufik-CHAARI/project2_webscrapping.git'

### -Create a folder named "downloads"

### -Inside the "downloads" folder create 4 folders with the following names:

1. step2
2. step3
3. step4_et_5

### -Install the project dependencies 

'pip install -r requirements.txt'

### -run the code with the command
python3 main.py

***

## **Please be aware that saving all images and   generating csv files with product details requires to wait about 5 mins for the completion of the task.**

## **If you want to generate the code data from steps 1,2 and 3, please go to the gitHub page dedicated to this code in the commits section.**

***
