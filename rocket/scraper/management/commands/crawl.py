from django.core.management.base import BaseCommand
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from scraper.scraper import settings as my_settings
from scraper.scraper.spiders.userdata import UserDataSpider
from gitparse.views import link


class Command(BaseCommand):
    help  = 'Release spider'


    def handle(self, *args, **options):
        crawler_settings  = Settings()
        crawler_settings.setmodule(my_settings)
        process = CrawlerProcess(settings=crawler_settings)
        process.crawl(UserDataSpider, link= link)
        process.start()