#### Preamble ####
# Purpose: Tests Cleaned Disease Count Data & Yearly Disease Count Data
# Author: Evelyn Hughes
# Date: 13 May 2025
# Contact: evelyn.hughes@mail.utoronto.ca
# License: MIT
# Pre-requisites: 
  # - `polars` must be installed (pip install polars)
  # -  02-download_data.py must have been run
  # -  03-clean_data.py must have been run


#### Workspace setup ####
import polars as pl
import unittest

if __name__ == "__main__":
  
  unittest.main()


#### Test disease_count data ####
class TestAll(unittest.TestCase):
  def setUp(cls):
    cls.disease_count = pl.read_csv("data/02-analysis_data/disease_count.csv")
    cls.yearly_disease_count = pl.read_csv("data/02-analysis_data/yearly_disease_count.csv")

  def test_disease_count_data(self):
    # Test that there are no missing values in the dataset
    self.assertEqual(self.disease_count.null_count().to_series().sum(), 0)

    #Test all columns are int type
    for type in self.disease_count.dtypes:
      self.assertEqual(type, pl.Int64)

    #Test counts add to total
    for row in self.disease_count.rows(named = True):
      self.assertEqual(row["Coronavirus"] + row["Other"] + row["Unknown"], row["Total Agents"])

#### Test yearly_disease_count data ####
  def test_yearly_disease_count():
    ## Test that the dataset has 10 rows - one for each year between 2016-2025 inclusive
    assert yearly_disease_count.shape[0] == 6, "Dataset does not have 6 rows"

    # Test that the dataset has 6 columns
    assert yearly_disease_count.shape[1] == 9, "Dataset does not have 9 columns"

    # Test that the 'Coronavirus' column is int
    assert yearly_disease_count["Coronavirus"].dtype == pl.Int64, "Coronavirus column is not int type"

    # Test that the 'Influenza' column is int 
    assert yearly_disease_count["Influenza"].dtype == pl.Int64, "Influenza column is not int type"

    # Test that the 'Syncytial Virus' column is int 
    assert yearly_disease_count["Syncytial Virus"].dtype == pl.Int64, "Syncytial Virus column is not int type"

    # Test that the 'Metapneumovirus' column is int
    assert yearly_disease_count["Metapneumovirus"].dtype == pl.Int64, "Metapneumovirus column is not int type"

    # Test that the 'Rhinovirus' column is int
    assert yearly_disease_count["Rhinovirus"].dtype == pl.Int64, "Rhinovirus column is not int type"

    # Test that the 'Parainfluenza' column is int
    assert yearly_disease_count["Parainfluenza"].dtype == pl.Int64, "Parainfluenza column is not int type"

    # Test that the 'Respiratory' column is int
    assert yearly_disease_count["Respiratory"].dtype == pl.Int64, "Respiratory column is not int type"

    # Test that the 'Total' column is int
    assert yearly_disease_count["Total"].dtype == pl.Int64, "Total column is not int type"

    # Test that there are no missing values in the dataset
    assert yearly_disease_count.null_count().to_series().sum() == 0, "Dataset has missing values"

    # Test that respiratory count <= total count
    for row in yearly_disease_count.rows(named = True):
      assert row["Respiratory"] <= row["Total"], "Total is less than total respiratory"