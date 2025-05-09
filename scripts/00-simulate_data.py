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

# months
months = [
    "January", "February", "March", "April", "May", "June", "July",
      "August", "September", "October", "November", "December"
]

# Generate the outbreak data using numpy and polars
outbreaks19 = []
outbreaks20 = []
outbreaks21 = []
outbreaks22 = []
outbreaks23 = []
outbreaks24 = []
total_outbreaks = []


for _ in range(12):
  outbreaks19.append(int(120* np.random.rand()))

for _ in range(12):
  outbreaks20.append(int(120* np.random.rand()))

for _ in range(12):
  outbreaks21.append(int(120* np.random.rand()))

for _ in range(12):
  outbreaks22.append(int(120* np.random.rand()))

for _ in range(12):
  outbreaks23.append(int(120* np.random.rand()))

for _ in range(12):
  outbreaks24.append(int(120* np.random.rand()))

for i in range(12):
  total = outbreaks19[i] + outbreaks20[i] + outbreaks21[i] + outbreaks22[i] + outbreaks23[i] + outbreaks24[i]
  total_outbreaks.append()


# Create a polars DataFrame
analysis_data = pl.DataFrame({
    "months": months,
    "2019": outbreaks19,
    "2020": outbreaks20,
    "2021": outbreaks21,
    "2022": outbreaks22,
    "2023": outbreaks23,
    "2024": outbreaks24
})


#### Save data ####
analysis_data.write_csv("data/00-simulated_data/simulated_data.csv")
