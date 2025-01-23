import scrapy
import os
from datetime import datetime

class Vatan_Spider(scrapy.Spider):
    name = "vatan"
    start_urls = ['https://www.vatanbilgisayar.com/',]

    # Define custom settings to specify the CSV output location
    custom_settings = {
        'FEEDS': {
            os.path.join('/home/zaryal/Desktop/Websites/Ucuzcu/BE/Data_Analysis/csv', f'vatan{datetime.now().strftime("%Y%m%d")}.csv'): {
                'format': 'csv',
                'overwrite': True
            }
        }
    }

    def parse(self, response):
        category_links = response.css('li.brand-list__item')
        for link in category_links:
            category_url = link.css('a::attr(href)').get()
            category_name = link.css('a::text').get()
            yield response.follow(category_url, callback=self.parse_data, meta={'category_name': category_name})

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

        # Check for pagination and follow the next page if available
        next_page = response.css('ul.pagination li.pagination__item a.pagination__content::attr(href)').extract()
        for page in next_page:
            if page:
                yield response.follow(page, callback=self.parse_data, meta={'category_name': category_name})
