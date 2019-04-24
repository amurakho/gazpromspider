from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ..items import GazpromspiderItem
import re
import datetime


class GazpromSpider(CrawlSpider):
    name = 'gazpromspider'

    start_urls = [
        'https://www.gazpromvacancy.ru/jobs/page/0',
        ]

    rules = (
        # Rule for pagination
        Rule(LinkExtractor(allow='page/\d'), callback='parse_links_from_pagination', follow=True),
        # rule for parse page
        Rule(LinkExtractor(allow='job/+'), callback='parse_page')
    )

    def parse_links_from_pagination(self, response):

        # take all links from page
        all_page_links = response.css('.job-list-item h3 a').xpath('@href').getall()

        base_link = 'https://www.gazpromvacancy.ru/job'

        # take each link
        for link in all_page_links:
            # add base_link for full url
            new_url = base_link + link
            # follow the url
            yield response.follow(new_url, callback=self.parse_page)

    def parse_page(self, response):

        items = GazpromspiderItem()

        items['crawled_date'] = datetime.datetime.now().date()

        items['job_title'] = response.css('.job-title::text').get()

        items['job_url'] = response.url

        items['job_description'] = {'Обязаности:': response.css('.inline+ .plain p::text').getall(),
                                    'Требования': response.css('.plain+ .plain p::text').getall()}

        short_info_block = response.css('.job-params').css('dd')

        items['company_name'] = short_info_block.css('::text').get()

        # dont use regex for date becuse it will be hard to read
        items['posted_date'] = short_info_block.css('::text')[6].get()[15:-13]
        yield items