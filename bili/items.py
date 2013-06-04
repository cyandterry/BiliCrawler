# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class BiliItem(Item):
    url        = Field()
    avNo       = Field()
    title      = Field()
    time       = Field()
    play       = Field()
    favor      = Field()
    v_time     = Field()
    v_score    = Field()
