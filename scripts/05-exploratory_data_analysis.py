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
import numpy as np

t = np.arange(2019, 2025, 1)
KEYS = ["Coronavirus", "Respiratory", "Total"]
df = pl.read_csv("data/02-analysis_data/yearly_disease_count.csv")
raw_data = df.to_dict()
for key in KEYS:
  plt.plot(t, raw_data[key], marker = 'o', label = key)

plt.title("Coronavirus, Respiratory & Total Outbreaks")
plt.xlabel("Year")
plt.ylabel("Outbreak Count")
plt.grid()

plt.legend()
plt.show()


#### Workspace setup ####
# import numpy as np
# import polars as pl
# import matplotlib.pyplot as plt

# #### Read data ####
# composition_data = pl.read_csv("data/02-analysis_data/disease_count.csv")
# dict1 = composition_data.to_dict(as_series = False)
# analysis_data = pl.read_csv("data/02-analysis_data/yearly_disease_count.csv")


# ### Model data ####
# t = np.arange(2019, 2025, 1)
# DISEASES = ["Influenza", "Coronavirus", "Syncytial Virus", "Metapneumovirus", "Rhinovirus", "Parainfluenza"]
# SMALLER = ["Syncytial Virus", "Metapneumovirus", "Rhinovirus", "Parainfluenza"]
# LARGER = {"Coronavirus", "Respiratory", "Total"}

# print(dict1)
# COLUMNS = ["Coronavirus", "Other", "Unknown"]
# for key in COLUMNS:
#   for i in range(6):
#     dict1[key][i] = 100*dict1[key][i]/dict1["Total Agents"][i]

# print(dict1)
# corona = np.array(dict1["Coronavirus"])
# other = np.array(dict1["Other"])
# unknown = np.array(dict1["Unknown"])

# ind = np.arange(6)    
# width = 0.35       

# p1 = plt.bar(ind, corona, width, color='#d62728', )
# p2 = plt.bar(ind, other, width,  bottom=corona)
# p3 = plt.bar(ind, unknown, width,  bottom=corona+other)

# plt.ylabel('Percentage of Causative Agents')
# plt.title('Composition of Respiratory Disease Outbreaks')
# plt.xticks(ind, ('2019', '2020', '2021', '2022', '2023', '2024'))
# plt.yticks(np.arange(0, 110, 10))
# plt.legend((p1[0], p2[0], p3[0]), ('Coronavirus', 'Other', "Unknown"))

# plt.show()

#### Save model ####