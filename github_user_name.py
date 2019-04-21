# -*- coding: utf-8 -*-
import scrapy


class GithubUserNameSpider(scrapy.Spider):
    name = 'github_user_name'
    allowed_domains = ['www.github.com/augustinetharakan12']
    start_urls = ['http://www.github.com/augustinetharakan12/']

    def parse(self, response):

        name = response.css('.p-name::text').extract_first()

        print("\n####\n", name, "\n####\n")

        yield name

	   # Code for writing into the database or csv file
