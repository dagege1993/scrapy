import scrapy
from coser.items import DoubanspiderItem

class DOubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    start = 0
    url = 'https://movie.douban.com/top250?start='

    ends = '&filter='
    start_urls = [url + str(start) + ends]

    def parse(self,response):
        item = DoubanspiderItem()
        movies = response.xpath('//*[@id="content"]/div/div[1]/ol').extract_first()
        print(movies)
        for movie in movies:
            print(movie)
            # item['title'] = movie.xpath('./li')