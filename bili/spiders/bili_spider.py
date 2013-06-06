from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
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
        #self.log('$'*100)
        #self.log('Here is the page %s' % response.url)
        hxs = HtmlXPathSelector(response)
        if hxs.select("//center").extract():
            return
        bili = BiliItem()
        bili['url']     = response.url
        bili['avNo']    = re.search(r'\d+', str(response.url)).group()
        bili['title']   = hxs.select("//h2/text()").extract()[0]
        bili['time']    = hxs.select("//time/i/text()").extract()[0]

        infoAddress = 'http://interface.bilibili.tv/count?aid='+bili['avNo']
        request = urllib2.Request(infoAddress)
        response = urllib2.urlopen(request)
        content = response.read()
        dataList = re.findall(r'\d+',content)

        # Guess the below items are created by js. So cannot do crawl
        bili['play']    = dataList[0]
        bili['favor']   = dataList[1]
        bili['v_time']  = dataList[2]
        bili['v_score'] = dataList[3]
        return bili
