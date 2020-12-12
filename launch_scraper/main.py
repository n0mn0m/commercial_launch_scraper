import sys
import logging
import traceback
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import spiders.commspiders as cmpd

spiders_to_run = [
    cmpd.ReentrySpider
    ,cmpd.SafetyApprovalSpider
    ,cmpd.ActivePermitSpider
    ,cmpd.LicensedLaunchSpider
    ,cmpd.PermittedLaunchSpider
    ,cmpd.ActiveLaunchLicenseSpider
    ,cmpd.ActiveSiteOperatorLicenseSpider
    ]

if __name__ == "__main__":
    try:
        # set up the crawler and start to crawl one spider at a time
        process = CrawlerProcess(get_project_settings())
        for spider in spiders_to_run:
            process.crawl(spider)
        process.start()
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        logging.info('Error on line {}'.format(sys.exc_info()[-1].tb_lineno))
        logging.info("Exception: %s" % str(traceback.format_exc()))