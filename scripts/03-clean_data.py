#### Preamble ####
# Purpose: Cleans the raw plane data recorded by two observers..... [...UPDATE THIS...]
# Author: Rohan Alexander [...UPDATE THIS...]
# Date: 6 April 2023 [...UPDATE THIS...]
# Contact: rohan.alexander@utoronto.ca [...UPDATE THIS...]
# License: MIT
# Pre-requisites: [...UPDATE THIS...]
# Any other information needed? [...UPDATE THIS...]

#### Workspace setup ####
import polars as pl
import numpy as np

#constant variables
MONTHS = ["January", "February", "March", "April", 
                             "May", "June", "July", "August", "September", "October", "November", "December"]
YEARS = ["2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024", "2025"]


#initializing dictionaries
#type -> list of # of outbreaks in each month
disease_type_cleaned =dict()
disease_type_cleaned["Month"] = MONTHS

#agent -> list of # of outbreaks in each month
causative_agent_cleaned = dict()
causative_agent_cleaned["Month"] = MONTHS

#general disease -> list of # of outbreaks in each year
yearly_total_cleaned = dict()
yearly_total_cleaned["Year"] = YEARS
yearly_total_cleaned["Influenza"] = [0, ]*10
yearly_total_cleaned["Covid"] = [0, ]*10
yearly_total_cleaned["Total"] = [0, ]*10

#### Clean data ####
outbreak_counts = (0,)*12
for i in range(2016, 2026):
    
    # reading & iterating through csv
    raw = pl.read_csv("data/01-raw_data/ob_report_" + str(i) + ".csv")
    for row in raw.rows(named = True):
        #getting month of start
        start_date = row["Date Outbreak Began"]
        start_month = int(start_date[5:7]) - 1

        #getting disease type
        disease_type = row["Type of Outbreak"]
        if "Causative Agent-1" in row.keys():
            disease_one = row["Causative Agent-1"]
        else:
            disease_one = row["Causative Agent - 1"]
         
        if "Causative Agent-2" in row.keys():
            disease_two = row["Causative Agent-2"]
        else:
            disease_two = row["Causative Agent - 2"]

        #updating yearly total dictionary
        index = i - 2016
        yearly_total_cleaned["Total"][index] += 1
        
        #updating total influenza count
        if (disease_one is not None and "influenza" in disease_one.lower()) or (
            disease_two is not None and "influenza" in disease_two.lower()):
            yearly_total_cleaned["Influenza"][index] += 1
        
        #updating total covid count
        if (disease_one is not None and "covid" in disease_one.lower()) or (
            disease_two is not None and "covid" in disease_two.lower()):
            yearly_total_cleaned["Covid"][index] += 1

        #updating type outbreak count dictionary // each disease_type is a key
        if disease_type in disease_type_cleaned:
            disease_type_cleaned[disease_type][start_month] += 1
        else:
            disease_type_cleaned[disease_type] = [0, ]*12
            disease_type_cleaned[disease_type][start_month] += 1

        #updating causative agent dictionary from agent 1
        if disease_one in causative_agent_cleaned:
            causative_agent_cleaned[disease_one][start_month] += 1
        else:
            causative_agent_cleaned[disease_one] = [0, ]*12
            causative_agent_cleaned[disease_one][start_month] += 1

        #updating causative agent dictionary from agent 2
        if disease_two in causative_agent_cleaned:
            causative_agent_cleaned[disease_two][start_month] += 1
        else:
            causative_agent_cleaned[disease_two] = [0, ]*12
            causative_agent_cleaned[disease_two][start_month] += 1

#fixing NoneType values
if None in causative_agent_cleaned:
    causative_agent_cleaned["None"] = causative_agent_cleaned[None]
    del causative_agent_cleaned[None]

### SAVE TO CSV ###
df = pl.DataFrame(disease_type_cleaned)
df.write_csv("data/02-analysis_data/disease_type_cleaned.csv")

df = pl.DataFrame(causative_agent_cleaned)
df.write_csv("data/02-analysis_data/causative_agent_cleaned.csv")

df = pl.DataFrame(yearly_total_cleaned)
df.write_csv("data/02-analysis_data/yearly_total_cleaned.csv")

