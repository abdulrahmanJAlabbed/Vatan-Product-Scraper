🖥️ Vatan Bilgisayar Web Scraper
📝 Project Description
A Python Scrapy spider designed to scrape comprehensive product information from Vatan Bilgisayar's online store, extracting details across multiple product categories.
🌟 Features

Automated web scraping of Vatan Bilgisayar website
Extracts product details: name, price, image, URL
Handles multiple category pages
Saves data to timestamped CSV file
Supports pagination

🔧 Prerequisites

Python 3.8+
Scrapy
Operating Systems: Windows, macOS, Linux

💻 Installation Guide
1. Python Installation
Windows

Download Python from official website
During installation, check "Add Python to PATH"
Verify installation:

bashCopypython --version
pip --version
macOS/Linux
bashCopy# macOS (using Homebrew)
brew install python

# Linux (Ubuntu/Debian)
sudo apt-get update
sudo apt-get install python3 python3-pip
2. Virtual Environment Setup
bashCopy# Create virtual environment
python -m venv vatan_scraper_env

# Activate virtual environment
# Windows
vatan_scraper_env\Scripts\activate

# macOS/Linux
source vatan_scraper_env/bin/activate
3. Install Scrapy
bashCopypip install scrapy
📂 Project Setup
1. Repository Structure
Copyproject_folder/
│
├── scrapy.cfg
└── vatan_scraper/
    └── spiders/
        └── vatan_spider.py
2. Move Spider File

Move your vatan_spider.py into vatan_scraper/spiders/ directory

3. Configure Output Path
Windows Users

Open vatan_spider.py
Modify output path:

pythonCopy# Replace with your desired path
os.path.join('C:\\Users\\YourUsername\\Documents\\ScraperOutput', f'vatan{datetime.now().strftime("%Y%m%d")}.csv')
macOS/Linux Users

Existing path should work: /home/zaryal/Desktop/Websites/Ucuzcu/BE/Data_Analysis/csv/
Ensure directory exists or modify as needed

🚀 Running the Spider
bashCopy# Activate virtual environment first
scrapy crawl vatan
📊 Extracted Data Columns

Product Name
Price
Image URL
Product Page URL
Category Name

⚠️ Legal & Ethical Considerations

Respect Vatan Bilgisayar's robots.txt
Implement rate limiting
Use for educational/research purposes
Comply with website's terms of service

🛡️ Error Handling

Check internet connection
Verify website structure hasn't changed
Update CSS selectors if needed

📜 License
[Specify your project's license]
🤝 Contributing

Fork repository
Create feature branch
Commit changes
Push to branch
Create pull request
