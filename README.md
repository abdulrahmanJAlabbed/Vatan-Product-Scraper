
# Vatan Spider 🕷️

A Scrapy spider for scraping product information from the [Vatan Bilgisayar website](https://www.vatanbilgisayar.com/). This spider crawls product categories, retrieves product details such as name, price, image, and URL, and saves the data in a CSV format. It also handles pagination for scraping multiple pages of product listings.

## Features 🌟

- Scrapes product details (name, price, image, URL) from multiple categories.
- Handles pagination to scrape all products across multiple pages.
- Outputs the scraped data to a timestamped CSV file.
- Custom settings for output location and CSV format.

## Installation 💻

To use this spider, make sure you have [Scrapy](https://scrapy.org/) installed. You can install it via pip if you don't have it already:

```bash
pip install scrapy
```

Clone this repository or download the spider file to your local machine.

## Usage 🚀

1. **Setup the Spider**:  
   The spider is set to scrape products from Vatan Bilgisayar. You can customize the start URL and output location if needed.

2. **Run the Spider**:  
   Navigate to the directory where the spider file is saved and run the following command in your terminal:

   ```bash
   scrapy crawl vatan
   ```

3. **Output**:  
   The data will be saved as a CSV file in the specified location (`/home/zaryal/Desktop/Websites/Ucuzcu/BE/Data_Analysis/csv`) with a timestamp in the filename, e.g., `vatan20250123.csv`.

## Code Breakdown 📝

### Spider Configuration:

- **`start_urls`**: The starting URL for the spider. By default, it scrapes the homepage of Vatan Bilgisayar.
  
- **Custom Settings**:  
  The `FEEDS` setting specifies the path where the CSV output will be saved. The filename includes the current date, so each run generates a unique file.

  ```python
  custom_settings = {
      'FEEDS': {
          os.path.join('/home/zaryal/Desktop/Websites/Ucuzcu/BE/Data_Analysis/csv', f'vatan{datetime.now().strftime("%Y%m%d")}.csv'): {
              'format': 'csv',
              'overwrite': True
          }
      }
  }
  ```

### Parsing Logic:

- **`parse` Method**:  
  This method is called for the main page (homepage of Vatan). It extracts the category links and iterates over them to scrape products from each category.

  ```python
  def parse(self, response):
      category_links = response.css('li.brand-list__item')
      for link in category_links:
          category_url = link.css('a::attr(href)').get()
          category_name = link.css('a::text').get()
          yield response.follow(category_url, callback=self.parse_data, meta={'category_name': category_name})
  ```

- **`parse_data` Method**:  
  This method is called for each category page. It extracts product details such as the name, price, image URL, and product URL.

  ```python
  def parse_data(self, response):
      category_name = response.meta['category_name']
      for item in response.css('div.product-list'):
          title = item.css('div.product-list__product-name h3::text').get()
          price = item.css('div.product-list__cost span::text').getall()
          img = item.css('div.slider-img img::attr(src)').get()
          url = item.css('a.product-list__image-safe-link::attr(href)').get()

          yield {
              'product_name': title,
              'Price': price if price else 'N/A',
              'image': img if img else 'N/A',
              'url': url if url else 'N/A',
              'Category Name': category_name if category_name else 'N/A'
          }
  ```

- **Pagination**:  
  If there are additional pages, the spider will follow the pagination links and scrape the next page of products.

  ```python
  next_page = response.css('ul.pagination li.pagination__item a.pagination__content::attr(href)').extract()
  for page in next_page:
      if page:
          yield response.follow(page, callback=self.parse_data, meta={'category_name': category_name})
  ```

## Customization 🔧

- **Changing Output Location**:  
  If you want to change the location where the CSV is saved, modify the path in the `FEEDS` setting in the `custom_settings` dictionary.
  
- **Scraping Different Categories**:  
  If you wish to scrape different categories, you can modify the `start_urls` list to include other category URLs.

## Notes ⚠️

- Ensure that the path you specify for saving the CSV file is correct and accessible.
- This spider is designed to be run on a local machine. For a production environment, consider using Scrapy's CrawlSpider or deploying it to a cloud-based service like Scrapy Cloud.


## Contact 📧

If you have any questions or feedback, feel free to open an issue or contact me directly!

---

Happy scraping! 🕸️

