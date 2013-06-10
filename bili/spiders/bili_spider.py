from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from scrapy import log
from bili.items import BiliItem

import xlwt, urllib2, re

class BiliSpider(CrawlSpider):
    name = 'bili'
    allowed_domains = ['bilibili.tv']
    start_urls = []
    #start_urls = ['http://www.bilibili.tv/video']
    #rules = [Rule(SgmlLinkExtractor(allow=['av\d+']), callback='parse_bili')]
    '''
    def parse_bili(self, response):

        self.log('$'*100)
        self.log(response.url)
        return
    '''

    def __init__(self, begin = None, end = None):
        if begin is None:
            begin = 100
        if end is None:
            end = 593000

        for index in range(int(begin), int(end)):
                self.start_urls.append('http://www.bilibili.tv/video/av' + str(index))

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        if hxs.select("//center").extract():
            return
        bili = BiliItem()
        bili['url']     = response.url
        bili['avNo']    = int(re.search(r'\d+', str(response.url)).group())
        bili['title']   = hxs.select("//h2/text()").extract()[0]
        bili['time']    = hxs.select("//time/i/text()").extract()[0]

        infoAddress = 'http://interface.bilibili.tv/count?aid='+ str(bili['avNo'])

        yield Request( url = infoAddress, meta = {'bili':bili}, callback = self.parsejs)


    def parsejs(self, response):
        # These items are created by js.
        content = response.body
        dataList = re.findall(r'\d+',content)

        bili = response.meta['bili']
        bili['play']    = int(dataList[0])
        bili['favor']   = int(dataList[1])
        bili['v_time']  = int(dataList[2])
        bili['v_score'] = int(dataList[3])

        return bili
