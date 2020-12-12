## Custom webscraper for [FAA Commercial Space Data](http://www.faa.gov/data_research/commercial_space_data/)

Scraped data is stored in the **csv** and **json** folders with timestamped file names.

Currently scraping the following pages:

- ReentrySpider http://www.faa.gov/data_research/commercial_space_data/reentries/
- SafetyApprovalSpider http://www.faa.gov/data_research/commercial_space_data/safety_approvals/
- ActivePermitSpider http://www.faa.gov/data_research/commercial_space_data/permits/
- LicensedLaunchSpider http://www.faa.gov/data_research/commercial_space_data/launches/?type=Licensed
- PermittedLaunchSpider http://www.faa.gov/data_research/commercial_space_data/launches/?type=Permitted
- ActiveLaunchLicenseSpider http://www.faa.gov/data_research/commercial_space_data/licenses/
- ActiveSiteOperatorLicenseSpider http://www.faa.gov/data_research/commercial_space_data/licenses

Main.py has a list of Spiders to execute.

By default all spiders are included.
