#### Preamble ####
# Purpose: Models... [...UPDATE THIS...]
# Author: Rohan Alexander [...UPDATE THIS...]
# Date: 11 February 2023 [...UPDATE THIS...]
# Contact: rohan.alexander@utoronto.ca [...UPDATE THIS...]
# License: MIT
# Pre-requisites: [...UPDATE THIS...]
# Any other information needed? [...UPDATE THIS...]


#### Workspace setup ####
import numpy as np
import polars as pl
import matplotlib.pyplot as plt

#### Read data ####
most_common_data = pl.read_csv("data/02-analysis_data/high_disease_count.csv")
dict1 = most_common_data.to_dict(as_series = False)
analysis_data = pl.read_csv("data/02-analysis_data/yearly_disease_count.csv")


### Model data ####
t = np.arange(2019, 2025, 1)
DISEASES = ["Influenza", "Coronavirus", "Syncytial Virus", "Metapneumovirus", "Rhinovirus", "Parainfluenza"]
SMALLER = ["Syncytial Virus", "Metapneumovirus", "Rhinovirus", "Parainfluenza"]
LARGER = {"Coronavirus", "Respiratory", "Total"}

for disease in SMALLER:
  plt.plot(t, analysis_data[disease], label = disease)


plt.legend(loc="upper right")
plt.show()

#### Save model ####