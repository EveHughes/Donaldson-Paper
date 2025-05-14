#### Preamble ####
# Purpose: Simulates a yearly_dataset of Australian electoral divisions, including the 
  # state and party that won each division.
# Author: Evelyn Hughes
# Date: 13 May 2025
# Contact: evelyn.hughes@utoronto.ca
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
COMPOSITION_COLUMNS = ["Coronavirus", "Other", "Unknown"]

# Generate the yearly outbreak data using numpy and polars
#creating dictionary w/ columns
yearly_data = dict()
yearly_data["Year"] = YEARS
for column in DISEASE_COLUMNS:
  yearly_data[column] = [0, ]*6
yearly_data["Respiratory"] =[0, ]*6
yearly_data["Total"] = [0, ]*6

#generating random values for yearly data
for i in range(6):
  respiratory_count = 0
  for disease in DISEASE_COLUMNS:
    outbreak_count = int(100*np.random.rand())
    yearly_data[disease][i] = outbreak_count
    respiratory_count += outbreak_count

  respiratory_count += int(100*np.random.rand())
  yearly_data["Respiratory"][i] = respiratory_count
  total_count = respiratory_count + int(100*np.random.rand())
  yearly_data["Total"][i] = total_count


# Generate disease count data using numpy and polars
#creating dictionary w/ columns
disease_count = dict()
disease_count["Year"] = YEARS
for column in COMPOSITION_COLUMNS:
  disease_count[column] = [0, ]*6
disease_count["Total"] = [0, ]*6

#generating random values for disease count
for i in range(6):
  total_count = 0
  for disease in COMPOSITION_COLUMNS:
    outbreak_count = int(100*np.random.rand())
    disease_count[disease][i] = outbreak_count
    total_count += outbreak_count
  disease_count["Total"][i] = total_count

# Create a polars yearly_dataFrame
analysis_yearly_data = pl.DataFrame(yearly_data)
analysis_count_data = pl.DataFrame(disease_count)

#### Save yearly_data ####
analysis_yearly_data.write_csv("data/00-simulated_data/simulated_yearly_count.csv")
analysis_count_data.write_csv("data/00-simulated_data/simulated_disease_count.csv")
