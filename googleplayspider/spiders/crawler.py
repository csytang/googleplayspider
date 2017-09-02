from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider,Rule
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from googleplayspider.items import GoogleplayspiderItem
import urllib

"""
the spider class, which will read and parse the url from Google Play
    and extract the information for @see items.py;
    data crawled will be stored into MongoDB database
"""



class Googleplayspider(CrawlSpider):
    # define the name of the spider
    name = "GooglePlaySpider"

    # set the allowed domain to crawl
    # see document https://doc.scrapy.org/en/latest/topics/spiders.html
    allowed_domains = ['play.google.com']

    # start_urls to process
    start_urls =[
        'https://play.google.com/store/apps/',
    ]

    # define the rule for Crawler
    rules = (
        Rule(LinkExtractor(allow=('/store/apps',)), follow=True),
        Rule(LinkExtractor(allow=('/store/apps/details\?')), follow=True, callback='parse_link')
    )

    def abs_url(url, response):
        """Return absolute link"""
        base = response.xpath('//head/base/@href').extract()
        if base:
            base = base[0]
        else:
            base = response.url
        return urllib.basejoin(base,url)



    def parse_link(self, response):
        hxs = HtmlXPathSelector(response)
        titles = hxs.select('/html')
        for titles in titles:
            item = GoogleplayspiderItem()
            item["Link"] = titles.select('head/link[5]/@href').extract()
            item["Item_name"] = titles.select('//*[@class="document-title"]/div/text()').extract()
            item["Updated"] = titles.select('//*[@itemprop="datePublished"]/text()').extract()
            item["Author"] = titles.select('//*[@itemprop="author"]/a/span/text()').extract()
            item["Filesize"] = titles.select('//*[@itemprop="fileSize"]/text()').extract()
            item["Downloads"] = titles.select('//*[@itemprop="numDownloads"]/text()').extract()
            item["Version"] = titles.select('//*[@itemprop="softwareVersion"]/text()').extract()
            item["Compatibility"] = titles.select('//*[@itemprop="softwareVersion"]/text()').extract()
            item["Content_rating"] = titles.select('//*[@itemprop="contentRating"]/text()').extract()
            item["Author_link"] = titles.select('//*[@class="dev-link"]/@href').extract()
            item["Author_link_test"] = titles.select('//*[@class="content contains-text-link"]/a/@href').extract()
            item["Genre"] = titles.select('//*[@itemprop="genre"]/text()').extract()
            item["Price"] = titles.select('//*[@class="price buy id-track-click"]/span[2]/text()').extract()
            item["Rating_value"] = titles.select('//*[@class="score"]/text()').extract()
            item["Review_number"] = titles.select('//*[@class="reviews-num"]/text()').extract()
            item["Description"] = titles.select('//*[@class="id-app-orig-desc"]//text()').extract()
            item["IAP"] = titles.select('//*[@class="inapp-msg"]/text()').extract()
            item["Developer_badge"] = titles.select('//*[@class="badge-title"]//text()').extract()
            item["Physical_address"] = titles.select('//*[@class="content physical-address"]/text()').extract()
            item["Video_URL"] = titles.select('//*[@class="play-action-container"]/@data-video-url').extract()
            item["Developer_ID"] = titles.select('//*[@itemprop="author"]/a/@href').extract()
            yield item

