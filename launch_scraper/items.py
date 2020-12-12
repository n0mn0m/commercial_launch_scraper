from scrapy.item import Item, Field


"""A variety of dictionary like containers for scraped data"""
class LicensedLaunchScraperItem(Item):
    """Active license container used by faacommspider.py LicensedLaunchSpider"""
    date = Field()
    payload = Field()
    vehicle = Field()
    company = Field()
    site = Field()

class ActiveLicenseScraperItem(Item):
    """Active license container used by faaactlic.py ActiveLicenseSpider"""
    license = Field()
    company = Field()
    vehicle = Field()
    location = Field()
    expiration = Field()

class ActivePermitScraperItem(Item):
    """Active license container used by faaactpermits.py ActivePermitSpider"""
    permit = Field()
    company = Field()
    vehicle = Field()
    location = Field()
    expiration = Field()

class PermittedLaunchScraperItem(Item):
    """Active license container used by faapermlaunch.py PermittedLaunchSpider"""
    date = Field()
    payload = Field()
    vehicle = Field()
    company = Field()
    site = Field()

class ReentryScraperItem(Item):
    """Active license container used by faareentry.py ReentrySpider"""
    license = Field()
    company = Field()
    vehicle = Field()
    payload = Field()
    date = Field()
    site = Field()

class SafetyApprovalScraperItem(Item):
    """Active license container used by faasafeappr.py SafetyApprovalSpider"""
    safety_approval = Field()
    company = Field()
    purpose = Field()
    expiration = Field()

class ActiveLaunchLicenseScraperItem(Item):
    """Active license container used by faaactlnchlic.py ActiveLaunchLicenseSpider"""
    license = Field()
    company = Field()
    vehicle = Field()
    location = Field()
    expiration = Field()

class ActiveLaunchSiteOperatorScraperItem(Item):
    """Active license container used by faaactlnchsitelic.py ActiveSiteOperatorLicenseSpider"""
    license = Field()
    operator = Field()
    site = Field()
    location = Field()
    expiration = Field()
