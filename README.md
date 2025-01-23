🖥️ Vatan Bilgisayar Web Scraper
📝 Description
Python Scrapy spider for scraping product information from Vatan Bilgisayar's website.

🚀 Features

Crawl product categories
Extract detailed product information
Save data to timestamped CSV
Handles pagination automatically

🛠️ Requirements

Python 3.8+
Scrapy
Libraries: scrapy, datetime, os

📦 Installation
bashCopy# Clone repository
git clone <your-repo-url>

# Install dependencies
pip install scrapy
🔧 Configuration

Modify output path in script: /home/zaryal/Desktop/Websites/Ucuzcu/BE/Data_Analysis/csv/
Filename: vatanYYYYMMDD.csv

🏃 Usage
bashCopy# Run spider
scrapy crawl vatan
📊 Data Extracted

Product Name
Price
Image URL
Product URL
Category Name

⚠️ Important Notes

Respect website's terms of service
Check robots.txt
Implement responsible scraping
