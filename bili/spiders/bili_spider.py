from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from bili.items import BiliItem

class BiliSpider(CrawlSpider):

    name = 'bili'
    allowed_domains = ['bilibili.tv']
    start_urls = []
    for index in range(5100,5300):
        start_urls.append('http://www.bilibili.tv/video/av' + str(index))
    #rules = [Rule(SgmlLinkExtractor(allow=['/av\d+']), callback='parse_bili')]

    def parse(self, response):
        #self.log('$'*100)
        #self.log('Here is the page %s' % response.url)
        hxs = HtmlXPathSelector(response)
        if hxs.select("//center").extract():
            self.log("$"*100)
            self.log('Jumping since not found')
            return
        bili = BiliItem()
        bili['url']     = response.url
        bili['title']   = hxs.select("//h2/text()").extract()[0]
        bili['time']    = hxs.select("//time/i/text()").extract()[0]

        # Guess the below items are created by js. So cannot do crawl
        #bili['play']    = hxs.select("//i[@id='dianji']/text()").extract()[0]
        #bili['favor']   = hxs.select("//i[@id='stow_count']/text()").extract()[0]
        #bili['v_time']  = hxs.select("//span[@id='v_ctimes']/text()").extract()[0]
        #bili['v_score'] = hxs.select("//span[@id='v_cscores']/text()").extract()[0]
        return bili
