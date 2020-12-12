import pandas as pd
from datetime import datetime
import os

class PandasItemPipeLineTools():
    def cleanup_scraped_item(self, item, spider):
        """Function for cleaning the data from the scraping and storing it for future use."""

        #Setting up some variables to store the data
        current_file = os.path.dirname(os.path.realpath(__file__))
        csv_filename = os.path.join(current_file,'csv/' + str(spider.name) + '_' + datetime.now().strftime('%Y%m%d') + '.csv')
        json_filename = os.path.join(current_file,'json/' + str(spider.name) + '_' + datetime.now().strftime('%Y%m%d') + '.json')

        #Pulling in the item from the scrape and cleaning out tags as well as other non standard characters
        #Once cleaning of items is done then formatting the dataframe and storing csv and json files
        df = pd.DataFrame.from_dict(dict(item), orient='index')
        df.replace(to_replace="<[^>]*>", value='', inplace=True, regex=True)
        df.replace(to_replace="[\t\r\n]", value='', inplace=True, regex=True)
        df = df.transpose()
        df.to_csv(path_or_buf=csv_filename, na_rep='NaN', index=False, header=True)
        df.to_json(path_or_buf=json_filename)