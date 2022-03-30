import scrapy
from scraper.scraper.items import ScraperItem

class UserDataSpider(scrapy.Spider):
    name = 'userdata'
    allowed_domains = ['github.com']



    start_urls = ['https://github.com/celery']



    def parse(self, response, **kwargs):
        link_all_repo = response.css('details-menu.dropdown-menu-sw').xpath('ul/li[@data-menu-item="org-header-repositories-tab"]/a/@href').get()
        yield response.follow(link_all_repo, callback=self.parse_repos)


    def parse_repos(self, response):

        for repos in response.css('div.org-repos').xpath('div[@class="Box"]/ul/li[@class="Box-row"]'):

            link_repo = repos.xpath('div/div/div/h3[@class="wb-break-all"]/a/@href').get()

            yield response.follow(link_repo, callback=self.parse_info_of_repo)

    def parse_info_of_repo(self, response):
        repo_item = ScraperItem()
        name_repo = response.xpath('//*[@id="repository-container-header"]/div[1]/div/h1/strong/a/text()').get()
        about = response.xpath('//*[@id="repo-content-pjax-container"]/div/div/div[3]/div[2]/div/div[1]/div/p/text()').get().strip()
        link_site = response.xpath('//div[@class="my-3 d-flex flex-items-center"]/span/a/text()').get()
        stars = response.xpath('//a[contains(@href, "stargazers")]/strong/text()').get()
        forks = response.xpath('//a[contains(@href, "network/members")]/strong/text()').get()

        watching = response.xpath('//a[contains(@href, "watchers")]/strong/text()').get()
        commits = response.xpath('//a[@class="pl-3 pr-3 py-3 p-md-0 mt-n3 mb-n3 mr-n3 m-md-0 Link--primary no-underline no-wrap"]/span/strong/text()').get()
        commit_autor = response.xpath('//a[@class="commit-author user-mention"]/text()').get()
        commit_name = response.xpath('//div[@class="css-truncate css-truncate-overflow color-fg-muted"]/span/a/text()').getall()
        commit_date = response.xpath('//relative-time/text()').get()
        releases = response.xpath('//a[contains(@href, "releases")]/span/text()').get()
        releases_version = response.xpath('//a[@class="Link--primary d-flex no-underline"]/div/div/span/text()').get()
        releases_date = response.xpath('//div[@class="text-small color-fg-muted"]/relative-time/text()').get()

        repo_item['default_link'] = self.start_urls
        repo_item['name_repo'] = name_repo
        repo_item['about'] = about
        repo_item['link_site'] = link_site
        repo_item['stars'] = stars
        repo_item['forks'] = forks
        repo_item['watching'] = watching
        repo_item['commits'] = commits
        repo_item['commit_autor'] = commit_autor
        repo_item['commit_name'] = commit_name
        repo_item['commit_date'] = commit_date
        repo_item['releases'] = releases
        repo_item['releases_version'] = releases_version
        repo_item['releases_date'] = releases_date



        yield repo_item


