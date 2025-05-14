#### Preamble ####
# Purpose: Tests Simulated Data
# Author: Evelyn Hughes
# Date: 13 May 2025
# Contact: evelyn.hughes@mail.utoronto.ca
# License: MIT
# Pre-requisites: 
  # - `polars` must be installed (pip install polars)
  # - 'unittest' must be installed
  # -  00-simulate_data.py must have been run

#### Workspace setup ####
import polars as pl
import unittest

class TestSimulated(unittest.TestCase):
  def setUp(self):
    self.disease_count = pl.read_csv("data/00-simulated_data/simulated_disease_count.csv")
    self.yearly_disease_count = pl.read_csv("data/00-simulated_data/simulated_yearly_count.csv")

  def test_diseaseCount(self):

    #### Test disease_count data ####
    # Test that there are no missing values in the dataset
    self.assertEquals(self.disease_count.null_count().to_series().sum(), 0)

    #Test all columns are int type
    for type in self.disease_count.dtypes:
      self.assertEquals(type, pl.Int64)

    #Test counts add to total
    for row in self.disease_count.rows(named = True):
      self.assertEquals(row["Coronavirus"] + row["Other"] + row["Unknown"], row["Total Agents"])

  def test_yearlyCount(self):
      #### Test yearly_disease_count data ####
      # Test that the dataset has 10 rows - one for each year between 2016-2025 inclusive
      self.assertEquals (self.yearly_disease_count.shape[0], 6)

      # Test that the dataset has 6 columns
      self.assertEquals(self.yearly_disease_count.shape[1], 9)

      # Test that the all columns are int
      categories = ["Coronavirus", "Influenza", "Syncytial Virus", 
                   "Metapneumovirus", "Rhinovirus", "Parainfluenza", "Respiratory", "Total"]
      for category in categories:
        self.assertEquals(self.yearly_disease_count[category].dtype, pl.Int64)

      # Test that there are no missing values in the dataset
      self.assertEquals(self.yearly_disease_count.null_count().to_series().sum(), 0)

      # Test that respiratory count <= total count
      for row in self.yearly_disease_count.rows(named = True):
        self.assertLessEqual(row["Respiratory"], row["Total"])

if __name__ == "__main__":
  unittest.main()