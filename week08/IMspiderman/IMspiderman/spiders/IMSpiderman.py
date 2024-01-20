import scrapy


class ImspidermanSpider(scrapy.Spider):
    name = "IMSpiderman"
    allowed_domains = ["category.dangdang.com"]
    start_urls = ["http://category.dangdang.com/cp01.54.00.00.00.00.html"]

    def parse(self, response):
        xpath_parse = response.xpath('/html/body/div[1]/div[2]/div[1]/div')
        for xpath in xpath_parse:
            item = {}
            item['text'] = xpath.xpath('./span[1]/text()').extract_first().replace('“', '').replace('”', '')
            item['author'] = xpath.xpath('./span[2]/small/text()').extract_first()
            print(item)