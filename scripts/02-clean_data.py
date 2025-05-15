#### Preamble ####
# Purpose: Cleans the raw data from Outbreaks in Toronto Healthcare Institutions
# Author: Evelyn Hughes
# Date: 13 May 2025
# Contact: evelyn.hughes@mail.utoronto.ca
# License: MIT
# Pre-requisites: 
  # -  02-download_data.py must have been run
  # - `polars` must be installed (pip install polars)

#### Workspace setup ####
import polars as pl
from datetime import datetime

#constant variables
date = str(datetime.today()).split()[0]
MONTHS = ["January", "February", "March", "April", 
                             "May", "June", "July", "August", "September", "October", "November", "December"]
YEARS = ["2019", "2020", "2021", "2022", "2023", "2024"]
DISEASE_COLUMNS = ["Coronavirus", "Influenza", "Syncytial Virus", 
                   "Metapneumovirus", "Rhinovirus", "Parainfluenza", "Respiratory", "Total"]

#initializing dictionaries
disease_count = dict()
disease_count["Year"] = YEARS
disease_count["Coronavirus"] = [0, ]*6
disease_count["Other"] = [0, ]*6
disease_count["Unknown"] = [0, ]*6
disease_count["Total Agents"] = [0, ]*6

#general disease -> list of # of outbreaks in each year
yearly_disease_count = dict()
yearly_disease_count["Year"] = YEARS
for column in DISEASE_COLUMNS:
  yearly_disease_count[column] = [0, ]*6
yearly_disease_count["Respiratory"] =[0, ]*6
yearly_disease_count["Total"] = [0, ]*6

#### Clean data ####

## Finding composition based on primary causative agents ##

for year in range(2019, 2025):
    raw = pl.read_csv("data/01-raw_data/" + date + "_ob_report_" + str(year) + ".csv")
    for row in raw.rows(named = True):
       #index
        index = year - 2019

       #getting disease type, only check common respiratory
        disease_type = row["Type of Outbreak"]
        if disease_type != "Respiratory":
            continue
       
        #getting causative agents
        if "Causative Agent-1" in row.keys():
            disease_one = row["Causative Agent-1"]
        else:
            disease_one = row["Causative Agent - 1"]

        if "Causative Agent-2" in row.keys():
            disease_two = row["Causative Agent-2"]
        else:
            disease_two = row["Causative Agent - 2"]
         
        #updating count from disease_one
        disease_count["Total Agents"][index] += 1
        if "covid" in disease_one.lower() or "corona" in disease_one.lower():
            disease_count["Coronavirus"][index] += 1
        elif "unable" in disease_one.lower():
            disease_count["Unknown"][index] += 1
        else:
            disease_count["Other"][index] += 1
        
        if disease_two != None and disease_two != "" and disease_two != "None":
            disease_count["Total Agents"][index] += 1
            if "covid" in disease_two.lower() or "corona" in disease_two.lower():
                disease_count["Coronavirus"][index] += 1
            elif "unable" in disease_two.lower():
                disease_count["Unknown"][index] += 1
            else:
                disease_count["Other"][index] += 1

## summing total cases for the year
for year in range(2016, 2026):
    if year not in [2019, 2020, 2021, 2022, 2023, 2024]:
        continue

    # reading & iterating through csv
    raw = pl.read_csv("data/01-raw_data/" + date + "_ob_report_" + str(year) + ".csv")
    for row in raw.rows(named = True):
        #getting disease type
        disease_type = row["Type of Outbreak"]

        #getting causative agent
        if "Causative Agent-1" in row.keys():
            disease_one = row["Causative Agent-1"]
        else:
            disease_one = row["Causative Agent - 1"]
         
        if "Causative Agent-2" in row.keys():
            disease_two = row["Causative Agent-2"]
        else:
            disease_two = row["Causative Agent - 2"]

        #updating yearly total count
        index = year - 2019
        yearly_disease_count["Total"][index] += 1

        #updating yearly total respiratory count
        if "respiratory" in disease_type.lower():
            yearly_disease_count["Respiratory"][index] += 1

        #updating yearly total influenza count
        if (disease_one is not None and "influenza " in disease_one.lower()) or (
            disease_two is not None and "influenza " in disease_two.lower()):
            yearly_disease_count["Influenza"][index] += 1
        
        #updating yearly total coronavirus/covid count
        if (disease_one is not None and "covid" in disease_one.lower()) or (
            disease_two is not None and "covid" in disease_two.lower()):
            yearly_disease_count["Coronavirus"][index] += 1

        if (disease_one is not None and "corona" in disease_one.lower()) or (
            disease_two is not None and "corona" in disease_two.lower()):
            yearly_disease_count["Coronavirus"][index] += 1

        #updating yearly total Metapneumovirus
        if (disease_one is not None and "metapneumovirus" in disease_one.lower()) or (
            disease_two is not None and "metapneumovirus" in disease_two.lower()):
            yearly_disease_count["Metapneumovirus"][index] += 1
        
        #updating yearly total Rhinovirus
        if (disease_one is not None and "rhinovirus" in disease_one.lower()) or (
            disease_two is not None and "rhinovirus" in disease_two.lower()):
            yearly_disease_count["Rhinovirus"][index] += 1

        #updating yearly total Parainfluenza
        if (disease_one is not None and "parainfluenza" in disease_one.lower()) or (
            disease_two is not None and "parainfluenza" in disease_two.lower()):
            yearly_disease_count["Parainfluenza"][index] += 1

         #updating yearly total Respiratory syncytial virus
        if (disease_one is not None and "syncytial" in disease_one.lower()) or (
            disease_two is not None and "syncytial" in disease_two.lower()):
            yearly_disease_count["Syncytial Virus"][index] += 1

### SAVE TO CSV ###
#saving respiratory diseases with high count
df = pl.DataFrame(disease_count)
df.write_csv("data/02-analysis_data/disease_count.csv")

#saving yearly respiratory disease counts
df = pl.DataFrame(yearly_disease_count)
df.write_csv("data/02-analysis_data/yearly_disease_count.csv")



