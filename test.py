# Read in libraries
import pandas as pd
import numpy as np
from lets_plot import *
LetsPlot.setup_html(isolated_frame=True)
# read in df
url = 'https://raw.githubusercontent.com/byuidatascience/data4names/master/data-raw/names_year/names_year.csv'
df = pd.read_csv(url)

oliver_ut_total = int(df.loc[df['name'] == 'Oliver', 'UT'].sum())
felisha_earliest_year = int(df.loc[df['name'] == 'Felisha', 'year'].min())

print(oliver_ut_total)
print(felisha_earliest_year)

