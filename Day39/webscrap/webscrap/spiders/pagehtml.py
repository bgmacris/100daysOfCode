import scrapy
from .page_html_urls import urls


class PagehtmlSpider(scrapy.Spider):
	name = 'pagehtml'

	def start_requests(self):
		urls_list = urls.urls
		for url in urls_list:
			yield scrapy.Request(url=url, callback=self.parse)

	def parse(self, response):
		page = urls.urls[response.url]
		print(page, "\n\n\n")
		filename = f'/home/kali/python/webscrap/gen_html_page/html_{page}.html'
		with open(filename, 'wb') as f:
			f.write(response.body)
		self.log(f'Saved file {filename}')

