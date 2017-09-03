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
        #'https://play.google.com/store/apps',
        #'https://play.google.com/store/apps/details?id=com.instagram.android',
        'https://play.google.com/store/apps/details?id=com.liquidator.ruaz404'
    ]

    # define the rule for Crawler
    '''
     please notice that the scrapy will check the first rule and the second, thrid
    '''
    rules = (
        Rule(LinkExtractor(allow=("^https://play\.google\.com/store/apps/details\?id=.*&.*")),follow=True),
        Rule(LinkExtractor(allow=("^https://play\.google\.com/store/apps/details\?id=")), callback='parselink',follow=False),
        #Rule(LinkExtractor(allow=("^https://play\.google\.com/store/apps/details\?id=")), callback='parselink', follow=False),
        Rule(LinkExtractor(allow=("^https://play\.google\.com/store/apps")),follow = True),
    )

    def parselink(self, response):

        item = GoogleplayspiderItem()
        # url of this app

        item["Link"] = str(response.url)
        # return the name of this app

        item["Item_name"] = response.xpath('//*[@class="document-title"]/div/text()').extract_first().encode("utf-8")
        # return the last update of this app
        '''
            u'2017\u5e748\u670830\u65e5'
            the return the update is the time slot, which is in unicode
        '''

        item["Last_Updated"] = response.xpath('//*[@itemprop="datePublished"]/text()').extract_first().encode("utf-8")
        # return the author of this app

        item["Author"] = response.xpath('//*[@itemprop="author"]/a/span/text()').extract_first().encode("utf-8")

        # return the file size of this app
        '''
        u'  \u56e0\u88dd\u7f6e\u800c\u7570 '
        '''
        filesize = response.xpath('//*[@itemprop="fileSize"]/text()').extract_first()
        if filesize is not None:
            item["Filesize"] = filesize.encode("utf-8")
        else:
            item["Filesize"] = ""

        # return the downloads
        item["Downloads"] = response.xpath('//*[@itemprop="numDownloads"]/text()').extract_first().encode("utf-8")

        # return the version of application
        item["Version"] = str(response.xpath('//*[@itemprop="softwareVersion"]/text()').extract_first())

        # return the operation system of the application
        item["Operation_system"] = response.xpath('//*[@itemprop="operatingSystems"]/text()').extract_first().encode("utf-8")

        # return the contaent rating for the age of
        content_rating = response.xpath('//*[@itemprop="contentRating"]/text()').extract_first()
        if content_rating is not None:
            item["Content_rating"] = content_rating.encode("utf-8")
        else:
            item["Content_rating"] = ""

        # return the link of application provider
        author_link = response.xpath('//*[@class="dev-link"]/@href').extract_first()
        if author_link is not None:
            item["Author_link"] = author_link.encode("utf-8")
        else:
            item["Author_link"] = ""

        # return the link of privacy policy
        if len(response.xpath('//*[@class="dev-link"]/@href')) >= 3:
            privacy_link = response.xpath('//*[@class="dev-link"]/@href')[2].extract()
            if privacy_link is not None:
                item['Privacy_link'] = privacy_link.encode("utf-8")
            else:
                item['Privacy_link'] = ""
        else:
            item['Privacy_link'] = ""

        # category
        item["Genre"] = response.xpath('//*[@itemprop="genre"]/text()').extract_first().encode("utf-8")

        # price
        #item["Price"] = response.xpath('//*[@class="price buy id-track-click"]/span[2]/text()').extract_first()
        price = response.xpath('//*[@class="subtitle-container"]/span/span[2]/button/span/text()').extract_first()
        if price is not None:
            item["Price"] = price.encode("utf-8")
        else:
            item["Price"] = ""

        # rating from user
        rating_value = response.xpath('//*[@class="score"]/text()').extract_first()
        if rating_value is not None:
            item["Rating_value"] = rating_value.encode("utf-8")
        else:
            item["Rating_value"] = ""


        # the number of reviews
        item["Review_number"] = str(response.xpath('//*[@class="reviews-num"]/text()').extract_first())


        # the description of this app
        item["Description"] = str(response.xpath('//*[@itemprop="description"]//text()').extract_first())


        # the in app purchase of the app
        iap = response.xpath('//*[@class="inapp-msg"]/text()').extract_first()
        if iap is not None:
            item["IAP"] = iap.encode("utf-8")
        else:
            item["IAP"] = ""

        # the badge of developer
        badge = response.xpath('//*[@class="badge-title"]//text()').extract_first()

        if badge is not None:
            item["Developer_badge"] = badge.encode("utf-8")
        else:
            item["Developer_badge"] = ""

        # the address of developer
        physicaladdr = response.xpath('//*[@class="content physical-address"]/text()').extract_first()

        if physicaladdr is not None:
            item["Physical_address"] = physicaladdr.encode("utf-8")
        else:
            item["Physical_address"] = ""

        # the url of demo video
        video_url = response.xpath('//*[@class="play-action-container"]/@data-video-url').extract_first()

        if video_url is not None:
            item["Video_URL"] = video_url.encode("utf-8")
        else:
            item["Video_URL"] = ""

        # the id of the developer
        item["Developer_ID"] = response.xpath('//*[@itemprop="author"]/a/@href').extract_first().encode("utf-8")

        yield item




