from scrapy.spiders import Spider
import items as spi

class ReentrySpider(Spider):
    """Spider for regularly updated FAA Reentry data"""
    name = "faa_reentry"
    allowed_domains = ['faa.gov']
    start_urls = ['http://www.faa.gov/data_research/commercial_space_data/reentries/']

    def parse(self, response):
        reentries = response.xpath('//tbody')
        for reentry in reentries:
            reentry_item = spi.ReentryScraperItem()
            reentry_item['license'] = reentry.xpath('//tr/td[1]/a').extract()
            reentry_item['company'] = reentry.xpath('//tr/td[2]').extract()
            reentry_item['vehicle'] = reentry.xpath('//tr/td[3]').extract()
            reentry_item['payload'] = reentry.xpath('//tr/td[4]/a').extract()
            reentry_item['date'] = reentry.xpath('//tr/td[5]').extract()
            reentry_item['site'] = reentry.xpath('//tr/td[6]').extract()
            yield reentry_item

class SafetyApprovalSpider(Spider):
    """Spider for regularly updated FAA Safety Approval data"""
    name = "faa_safetyappr"
    allowed_domains = ['faa.gov']
    start_urls = ['http://www.faa.gov/data_research/commercial_space_data/safety_approvals/']

    def parse(self, response):
        approvals = response.xpath('//tbody')
        for approval in approvals:
            approval_item = spi.SafetyApprovalScraperItem()
            approval_item['safety_approval'] = approval.xpath('//tr/td[1]/a').extract()
            approval_item['company'] = approval.xpath('//tr/td[2]').extract()
            approval_item['purpose'] = approval.xpath('//tr/td[3]').extract()
            approval_item['expiration'] = approval.xpath('//tr/td[4]/span').extract()
            yield approval_item

class ActivePermitSpider(Spider):
    """Spider for regularly updated FAA Active Permit data"""
    name = "faa_actpermit"
    allowed_domains = ['faa.gov']
    start_urls = ['http://www.faa.gov/data_research/commercial_space_data/permits/']

    def parse(self, response):
        permits = response.xpath('//tbody')
        for permit in permits:
            permit_item = spi.ActivePermitScraperItem()
            permit_item['permit'] = permit.xpath('//tr/td[1]/a').extract()
            permit_item['company'] = permit.xpath('//tr/td[2]').extract()
            permit_item['vehicle'] = permit.xpath('//tr/td[3]').extract()
            permit_item['location'] = permit.xpath('//tr/td[4]').extract()
            permit_item['expiration'] = permit.xpath('//tr/td[5]/span').extract()
            yield permit_item

class LicensedLaunchSpider(Spider):
    """Spider for regularly updated FAA Licensed Launch data"""
    name = "faa_licensedlaunch"
    allowed_domains = ['faa.gov']
    start_urls = ['http://www.faa.gov/data_research/commercial_space_data/launches/?type=Licensed']

    def parse(self, response):
        launches = response.xpath('//tbody')
        for launch in launches:
            launch_item = spi.LicensedLaunchScraperItem()
            launch_item['date'] = launch.xpath('//tr/td[1]/span').extract()
            launch_item['payload'] = launch.xpath('//tr/td[2]/a').extract()
            launch_item['vehicle'] = launch.xpath('//tr/td[3]').extract()
            launch_item['company'] = launch.xpath('//tr/td[4]').extract()
            launch_item['site'] = launch.xpath('//tr/td[5]').extract()
            yield launch_item

class PermittedLaunchSpider(Spider):
    """Spider for regularly updated FAA Permitted Launch data"""
    name = "faa_permlaunch"
    allowed_domains = ['faa.gov']
    start_urls = ['http://www.faa.gov/data_research/commercial_space_data/launches/?type=Permitted']

    def parse(self, response):
        launches = response.xpath('//tbody')
        for launch in launches:
            launch_item = spi.PermittedLaunchScraperItem()
            launch_item['date'] = launch.xpath('//tr/td[1]/span').extract()
            launch_item['payload'] = launch.xpath('//tr/td[2]/a').extract()
            launch_item['vehicle'] = launch.xpath('//tr/td[3]').extract()
            launch_item['company'] = launch.xpath('//tr/td[4]').extract()
            launch_item['site'] = launch.xpath('//tr/td[5]').extract()
            yield launch_item

class ActiveLaunchLicenseSpider(Spider):
    """Spider for regularly updated FAA Active Launch License data"""
    name = "faa_actlnchlic"
    allowed_domains = ['faa.gov']
    start_urls = ['http://www.faa.gov/data_research/commercial_space_data/licenses/']

    def parse(self, response):
        licenses = response.xpath("//caption[text()='Active Launch Licenses']/following-sibling::tbody[1]")
        for license in licenses:
            license_item = spi.ActiveLaunchLicenseScraperItem()
            license_item['license'] = license.xpath('.//tr/td[1]/a').extract()
            license_item['company'] = license.xpath('.//tr/td[2]').extract()
            license_item['vehicle'] = license.xpath('.//tr/td[3]').extract()
            license_item['location'] = license.xpath('.//tr/td[4]').extract()
            license_item['expiration'] = license.xpath('.//tr/td[5]/span').extract()
            yield license_item

class ActiveSiteOperatorLicenseSpider(Spider):
    """Spider for regularly updated FAA Active Launch Site Operator License data"""
    name = "faa_actlnchsitelic"
    allowed_domains = ['faa.gov']
    start_urls = ['http://www.faa.gov/data_research/commercial_space_data/licenses']

    def parse(self, response):
        licenses = response.xpath("//caption[text()='Active Launch Site Operator Licenses']/following-sibling::tbody[1]")
        for license in licenses:
            license_item = spi.ActiveLaunchSiteOperatorScraperItem()
            license_item['license'] = license.xpath('.//tr/td[1]/a').extract()
            license_item['operator'] = license.xpath('.//tr/td[2]').extract()
            license_item['site'] = license.xpath('.//tr/td[3]').extract()
            license_item['location'] = license.xpath('.//tr/td[4]').extract()
            license_item['expiration'] = license.xpath('.//tr/td[5]/span').extract()
            yield license_item