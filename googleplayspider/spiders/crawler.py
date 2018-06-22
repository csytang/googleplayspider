from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider,Rule
from scrapy.selector import HtmlXPathSelector
from googleplayspider.items import GoogleplayspiderItem
import urllib
import scrapy

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
        "https://play.google.com/store/apps/"
    ]

    # define the rule for Crawler
    '''
     please notice that the scrapy will check the first rule and the second, thrid
    '''
    rules = (
        Rule(LinkExtractor(allow=(r'apps',), deny=(r'reviewId')), follow=True, callback='parselink'),
        Rule(LinkExtractor(allow=('/store/apps')), follow=True)
    )

    def parselink(self, response):

        item = GoogleplayspiderItem()
        # url of this app

        if not str(response.url).startswith("https://play.google.com/store/apps/details?id="):
            return

        item["Link"] = str(response.url)
        # return the name of this app
		
        tmpitemname = response.xpath('//*[@itemprop="name"]/span/text()').extract_first()

        if tmpitemname is not None:
            item["Item_name"] = tmpitemname.encode("utf-8")
        else:
            item["Item_name"] = ""
        # return the last update of this app
        '''
            u'2017\u5e748\u670830\u65e5'
            the return the update is the time slot, which is in unicode
        '''

        tmplastupdate = response.xpath('//*[@id="fcxH9b"]//div[@class="hAyfc"][1]//span/text()').extract()[0]
        if tmplastupdate is not None:
            item["Last_Updated"] = tmplastupdate.encode("utf-8")
        else:
            item["Last_Updated"] = ""

        # return the file size of this app
        '''
        u'  \u56e0\u88dd\u7f6e\u800c\u7570 '
        '''
        filesize = response.xpath('//*[@id="fcxH9b"]//div[@class="hAyfc"][2]//span/text()').extract_first()
        if filesize is not None:
            item["Filesize"] = filesize.encode("utf-8")
        else:
            item["Filesize"] = ""

        # return the downloads
        downloads = response.xpath('//*[@id="fcxH9b"]//div[@class="hAyfc"][3]//span/text()').extract_first()
        if downloads is not None:
            item["Downloads"] = downloads.encode("utf-8")
        else:
            item["Downloads"] = ""

        # return the version of application
        version = response.xpath('//*[@id="fcxH9b"]//div[@class="hAyfc"][4]//span/text()').extract()[0]
        if version is not None:
            item["Version"] = version.encode("utf-8")
        else:
            item["Version"] = ""

        # return the operation system of the application

        operation_system = response.xpath('//*[@id="fcxH9b"]//div[@class="hAyfc"][5]//span/text()').extract_first()
        if operation_system is not None:
            item["Operation_system"] = operation_system.encode("utf-8")
        else:
            item["Operation_system"] = ""

        # return the contaent rating for the age of
        content_rating = response.xpath('//*[@id="fcxH9b"]//div[@class="hAyfc"][6]//span/div/text()').extract_first()
        if content_rating is not None:
            item["Content_rating"] = content_rating.encode("utf-8")
        else:
            item["Content_rating"] = ""


        # category
        genre = response.xpath('//*[@itemprop="genre"]/text()').extract_first()
        if genre is not None:
            item["Genre"] = genre.encode("utf-8")
        else:
            item["Genre"] = ""



        # the number of reviews
        review_count = response.xpath('//*[@id="fcxH9b"]//span[@class="AYi5wd TBRnV"]//text()').extract()[0]
        if review_count is not None:
            item["Review_number"] = review_count.encode("utf-8")
        else:
            item["Review_number"] = ""

        # the description of this app
        description_content = response.xpath('//*[@itemprop="description"]//text()').extract_first()
        if description_content is not None:
            item["Description"] = description_content.encode("utf-8")
        else:
            item["Description"] = ""


        # the id of the developer
        #item["Developer_ID"] = response.xpath('//*[@id="fcxH9b"]//div[@class="hAyfc"][9]//span/div/text()').extract()[0]

        yield item




