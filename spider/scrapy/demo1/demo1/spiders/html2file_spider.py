from scrapy.spider import BaseSpider
class DmozSpider(BaseSpider):
    name = "demo"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.pythontab.com/html/2013/pythonhexinbiancheng_0814/541.html"
    ]
    def parse(self, response):
        filename = response.url.split("/")[-2]
        open(filename, 'wb').write(response.body)