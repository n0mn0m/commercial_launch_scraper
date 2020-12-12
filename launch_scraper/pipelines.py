from launch_dataframe import PandasItemPipeLineTools

class LaunchScraperPipeline(object):
    """Catch the item and spider to then pass for cleaning and storage of the scraped data."""
    def process_item(self, item, spider):
        data_tools = PandasItemPipeLineTools()
        data_tools.cleanup_scraped_item(item, spider)
        return item
