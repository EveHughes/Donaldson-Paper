#### Preamble ####
# Purpose: Tests... [...UPDATE THIS...]
# Author: Rohan Alexander [...UPDATE THIS...]
# Date: 26 September 2024 [...UPDATE THIS...]
# Contact: rohan.alexander@utoronto.ca [...UPDATE THIS...]
# License: MIT
# Pre-requisites: [...UPDATE THIS...]
# Any other information needed? [...UPDATE THIS...]


#### Workspace setup ####
import polars as pl
import numbers
causative_agent_cleaned = pl.read_csv("data/02-analysis_data/causative_agent_cleaned.csv")
yearly_total_cleaned = pl.read_csv("data/02-analysis_data/yearly_total_cleaned.csv")

#### Test data ####
# Test that the dataset has 10 rows - one for each year between 2016-2025 inclusive
assert yearly_total_cleaned.shape[0] == 10, "Dataset does not have 10 rows"

# Test that the dataset has 6 columns
assert yearly_total_cleaned.shape[1] == 10, "Dataset does not have 6 columns"

# Test that the 'coronavirus' column is int
print(yearly_total_cleaned["Coronavirus"].dtype)
assert yearly_total_cleaned["Coronavirus"].dtype == pl.Int64, "Coronavirus column is not int type"

# Test that the 'influenza' column is int 
assert yearly_total_cleaned["Influenza"].dtype == pl.Int64, "Influenza column is not int type"

# Test that the 'Syncytial Virus' column is int 
assert yearly_total_cleaned["Syncytial Virus"].dtype == pl.Int64, "Syncytial Virus column is not int type"

# Test that the 'Norovirus' column is int
assert yearly_total_cleaned["Norovirus"].dtype == pl.Int64, "Norovirus column is not int type"

# Test that the 'Metapneumovirus' column is int
assert yearly_total_cleaned["Metapneumovirus"].dtype == pl.Int64, "Metapneumovirus column is not int type"

# Test that the 'Rhinovirus' column is int
assert yearly_total_cleaned["Rhinovirus"].dtype == pl.Int64, "Rhinovirus column is not int type"

# Test that the 'Parainfluenza' column is int
assert yearly_total_cleaned["Parainfluenza"].dtype == pl.Int64, "Parainfluenza column is not int type"

# Test that the 'Respiratory' column is int
assert yearly_total_cleaned["Respiratory"].dtype == pl.Int64, "Respiratory column is not int type"

# Test that the 'Total' column is int
assert yearly_total_cleaned["Total"].dtype == pl.Int64, "Total column is not int type"

# Test that there are no missing values in the dataset
assert yearly_total_cleaned.null_count().to_series().sum() == 0, "Dataset has missing values"

# Test that respiratory count <= total count
value = True
for row in yearly_total_cleaned.rows(named = True):
  assert row["Respiratory"] <= row["Total"], "Total is less than total respiratory"
