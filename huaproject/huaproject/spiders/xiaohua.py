import scrapy
from huaproject.items import HuaprojectItem


class xiaohuaproject(scrapy.Spider):
    name = 'xiaohua'
    allow_domians = ['www.xiaohuar.com']
    page = 0
    url = 'http://www.xiaohuar.com/list-1-'
    start_urls = ['http://www.xiaohuar.com/hua/list-1-0.html']

    def parse(self, response):
        div_list = response.xpath('//*[@id="list_img"]/div/div[1]/div')
        print(div_list)
        for div in div_list:
            item = HuaprojectItem()
            image_url = div.xpath('./div[1]/div[1]/a/img/@src').extract_first()
            # print(image_url)
            item['image_url'] = 'http://www.xiaohuar.com' + image_url
            item['name'] = div.xpath('./div[1]/div[2]/span/a/text()').extract_first()
            item['like'] = div.xpath('./div[2]/div[1]/em/text()').extract_first()
            # 将对象返回
            yield item
        self.page += 1
        if self.page <= 43:
            url = self.url + str(self.page) + '.html'
            yield scrapy.Request(url=url, callback=self.parse)
