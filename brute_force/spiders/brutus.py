from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from brute_force.items import BruteForceItem
from urlparse import urljoin
from collections import OrderedDict

class DmozSpider(BaseSpider):
    name = "brutus"
    allowed_domains = ["tool.httpcn.com"]
    start_urls = ['http://tool.httpcn.com/Zi/BuShou.html']

    def parse(self, response):
        for url in response.css('td a::attr(href)').extract():
            cb = self.parse if '/zi/bushou' in url.lower() else self.parse_item
            yield Request(urljoin(response.url, url), callback=cb)   

    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        item =  BruteForceItem()
        item["a_alpha"] = hxs.xpath('//*[@id="div_a1"]/table').extract()
        item["c_seperator"] = "#######################"
        item["b_the_strokes"] = hxs.xpath('//*[@id="div_a1"]/div[2]/text()[2]').extract()
        return item









# from scrapy.spider import BaseSpider
# from scrapy.selector import HtmlXPathSelector
# from brute_force.items import BruteForceItem

# class DmozSpider(BaseSpider):
#     name = "brutus"
#     allowed_domains = ["tool.httpcn.com"]
#     start_urls = [ #Page One
#                   "http://tool.httpcn.com/Html/Zi/21/PWAZAZAZXVILEPWXV.shtml",
#                   "http://tool.httpcn.com/Html/Zi/21/PWAZAZCQCQILEPWB.shtml",
#                   "http://tool.httpcn.com/Html/Zi/21/PWAZAZCQKOILEPWD.shtml",
#                   "http://tool.httpcn.com/Html/Zi/21/PWAZAZCQUYILEPWF.shtml",
#                   "http://tool.httpcn.com/Html/Zi/21/PWAZAZCQMEILEKOCQ.shtml",
#                   "http://tool.httpcn.com/Html/Zi/21/PWAZAZCQRNILEKOKO.shtml",
#                   "http://tool.httpcn.com/Html/Zi/22/PWCQKOILUYUYKOTBCQ.shtml",
#                   "http://tool.httpcn.com/Html/Zi/21/PWAZAZAZRNILEPWRN.shtml",
#                   "http://tool.httpcn.com/Html/Zi/21/PWAZAZCQPWILEPWC.shtml",
#                   "http://tool.httpcn.com/Html/Zi/21/PWAZAZCQILILEPWE.shtml",
#                   "http://tool.httpcn.com/Html/Zi/21/PWAZAZCQTBILEKOAZ.shtml",
#                   "http://tool.httpcn.com/Html/Zi/21/PWAZAZCQXVILEKOPW.shtml",
#                   "http://tool.httpcn.com/Html/Zi/21/PWAZAZPWAZILEKOIL.shtml",
#                   "http://tool.httpcn.com/Html/Zi/22/PWCQKOILRNUYKOTBUY.shtml",
#                    #Page Two
#                   "http://tool.httpcn.com/Html/Zi/21/PWAZCQAZCQILEXVUY.shtml",
#                   "http://tool.httpcn.com/Html/Zi/21/PWAZCQAZMEILEXVB.shtml",
#                   "http://tool.httpcn.com/Html/Zi/21/PWAZCQAZTBILEXVA.shtml",
#                   #Page Three
#                   "http://tool.httpcn.com/Html/Zi/20/CQRNRNRNPWILECQXV.shtml",
#                   "http://tool.httpcn.com/Html/Zi/21/PWAZAZPWILILEKOXV.shtml",
#                   "http://tool.httpcn.com/Html/Zi/21/PWAZAZKOCQILEKOF.shtml",
#                   "http://tool.httpcn.com/Html/Zi/21/PWAZAZKOKOILEILCQ.shtml",
#                   "http://tool.httpcn.com/Html/Zi/21/PWAZAZKOUYILEILKO.shtml",
#                   "http://tool.httpcn.com/Html/Zi/21/PWAZAZKOMEILEILUY.shtml",
#                   "http://tool.httpcn.com/Html/Zi/21/PWAZAZKORNILEILME.shtml",
#                   "http://tool.httpcn.com/Html/Zi/21/PWAZAZILPWILEILA.shtml",
#                   "http://tool.httpcn.com/Html/Zi/21/PWAZAZILUYILEILD.shtml",
#                   "http://tool.httpcn.com/Html/Zi/21/PWAZAZILMEILEILF.shtml",
#                   "http://tool.httpcn.com/Html/Zi/21/PWAZAZILRNILEUYCQ.shtml",
#                   "http://tool.httpcn.com/Html/Zi/21/PWAZAZUYCQILEUYKO.shtml",
#                   "http://tool.httpcn.com/Html/Zi/21/PWAZAZUYKOILEUYUY.shtml",
#                   "http://tool.httpcn.com/Html/Zi/21/PWAZAZUYUYILEUYME.shtml",
#                   "http://tool.httpcn.com/Html/Zi/21/PWAZAZTBCQILEUYD.shtml",
#                   "http://tool.httpcn.com/Html/Zi/21/PWAZXVMETBUYCQXVC.shtml",
#                   "http://tool.httpcn.com/Html/Zi/41/ILAZCQMEPWRNCEC.shtml",
#                   "http://tool.httpcn.com/Html/Zi/21/PWAZAZAZPWILEPWPW.shtml",
#                   "http://tool.httpcn.com/Html/Zi/21/PWAZAZPWUYILEKORN.shtml",
#                   "http://tool.httpcn.com/Html/Zi/21/PWAZAZKOPWILEILAZ.shtml",
#                   "http://tool.httpcn.com/Html/Zi/21/PWAZAZKOILILEILPW.shtml",
#                   "http://tool.httpcn.com/Html/Zi/21/PWAZAZKOTBILEILIL.shtml",
#                   "http://tool.httpcn.com/Html/Zi/21/PWAZAZKOXVILEILTB.shtml",
#                   "http://tool.httpcn.com/Html/Zi/21/PWAZAZILAZILEILXV.shtml",
#                   "http://tool.httpcn.com/Html/Zi/21/PWAZAZILILILEILC.shtml",
#                   "http://tool.httpcn.com/Html/Zi/21/PWAZAZILTBILEILE.shtml",
#                   "http://tool.httpcn.com/Html/Zi/21/PWAZAZILXVILEUYAZ.shtml",
#                   "http://tool.httpcn.com/Html/Zi/21/PWAZAZUYAZILEUYPW.shtml",
#                   "http://tool.httpcn.com/Html/Zi/21/PWAZAZUYPWILEUYIL.shtml",
#                   "http://tool.httpcn.com/Html/Zi/21/PWAZAZUYILILEUYTB.shtml",
#                   "http://tool.httpcn.com/Html/Zi/21/PWAZAZUYTBILEUYXV.shtml",
#                   "http://tool.httpcn.com/Html/Zi/21/PWAZCQAZKOILEXVME.shtml",
#                   "http://tool.httpcn.com/Html/Zi/30/PWRNUYXVCQMEKOXVD.shtml"
#                   #Page Four
#                   ]

#     def parse(self, response):
#         hxs = HtmlXPathSelector(response)
        
#         items = []
#         item =  BruteForceItem()

#         item["the_strokes"] = hxs.xpath('//*[@id="div_a1"]/div[2]').extract()
#         item["character"] = hxs.xpath('//*[@id="div_a1"]/div[3]').extract()
#         items.append(item)
#         return items