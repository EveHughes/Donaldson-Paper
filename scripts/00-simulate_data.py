#### Preamble ####
# Purpose: Simulates a dataset of Australian electoral divisions, including the 
  # state and party that won each division.
# Author: Rohan Alexander
# Date: 26 September 2024
# Contact: rohan.alexander@utoronto.ca
# License: MIT
# Pre-requisites: 
  # - `polars` must be installed (pip install polars)
  # - `numpy` must be installed (pip install numpy)


#### Workspace setup ####
import polars as pl
import numpy as np
np.random.seed(853)

#### Simulate data ####

#constants
YEARS = ["2019", "2020", "2021", "2022", "2023", "2024"]
DISEASE_COLUMNS = ["Coronavirus", "Influenza", "Syncytial Virus", 
                   "Metapneumovirus", "Rhinovirus", "Parainfluenza", "Respiratory", "Total"]

# Generate the outbreak data using numpy and polars
#creating dictionary w/ columns
data = dict()
data["Year"] = YEARS
for column in DISEASE_COLUMNS:
  data[column] = [0, ]*6
data["Respiratory"] =[0, ]*6
data["Total"] = [0, ]*6

#generating random values for data
for i in range(6):
  respiratory_count = 0
  for disease in DISEASE_COLUMNS:
    outbreak_count = int(100*np.random.rand())
    data[disease][i] = outbreak_count
    respiratory_count += outbreak_count

  respiratory_count += int(100*np.random.rand())
  data["Respiratory"][i] = respiratory_count
  total_count = respiratory_count + int(100*np.random.rand())
  data["Total"][i] = total_count

# Create a polars DataFrame
analysis_data = pl.DataFrame(data)

#### Save data ####
analysis_data.write_csv("data/00-simulated_data/simulated_data.csv")
