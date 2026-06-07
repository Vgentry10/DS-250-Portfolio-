import pandas as pd
import numpy as np
from lets_plot import *
LetsPlot.setup_html(isolated_frame=True)
df = pd.read_json("https://github.com/byuidatascience/data4missing/raw/master/data-raw/flights_missing/flights_missing.json")


print(df.isna().sum())
