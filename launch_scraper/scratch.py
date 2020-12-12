import pandas as pd
from datetime import datetime
import os
current_file = os.path.dirname(os.path.realpath(__file__))
csv_filename = os.path.join(current_file, 'csv/' + 'test' + '_' + datetime.now().strftime('%Y%m%d') + '.csv')
df = pd.read_csv('launch_scraper/csv/faa_reentry_20161023.csv')
df.replace(to_replace="<[^>]*>", value='', inplace=True, regex=True)
df.replace(to_replace="[\t\r\n]", value='', inplace=True, regex=True)
df = df.transpose()
df.columns = df.iloc[0]
df = df[1:]
df.to_csv(path_or_buf=csv_filename, na_rep='NaN', index=False, header=True)