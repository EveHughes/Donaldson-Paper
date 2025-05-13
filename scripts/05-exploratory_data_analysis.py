#### Preamble ####
# Purpose: Models... [...UPDATE THIS...]
# Author: Rohan Alexander [...UPDATE THIS...]
# Date: 11 February 2023 [...UPDATE THIS...]
# Contact: rohan.alexander@utoronto.ca [...UPDATE THIS...]
# License: MIT
# Pre-requisites: [...UPDATE THIS...]
# Any other information needed? [...UPDATE THIS...]

import polars as pl
import matplotlib.pyplot as plt

raw_data = pl.read_csv("data/02-analysis_data/disease_count.csv")
raw_data = raw_data.head(5)
raw_data = raw_data.to_pandas()
plt.table(raw_data)

plt.show()

#### Save model ####