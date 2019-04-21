import scrapy

from scrapy.crawler import CrawlerProcess as cp

from github_user_name import GithubUserNameSpider

def run_crawler_github_user_name():    
    process = cp({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
        })

    process.crawl(GithubUserNameSpider)
    process.start()