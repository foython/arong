from pathlib import Path
import scrapy

class ArongSpider(scrapy.Spider):
    name = 'arong'


    def start_requests(self):
        urls = [
            'https://www.aarong.com/women/tops',
            'https://www.aarong.com/men/panjabi',
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # page = response.url.split("/")[-2]
        # filename = f"quotes-{page}.html"
        # Path(filename).write_bytes(response.body)
        # self.log(f"Saved file {filename}")
        products = response.css('.product-item').get()
        print(products)
