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

#constant variables
MONTHS = ["January", "February", "March", "April", 
                             "May", "June", "July", "August", "September", "October", "November", "December"]
YEARS = ["2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024", "2025"]

most_common = dict()

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
yearly_total_cleaned["Coronavirus"] = [0, ]*10
yearly_total_cleaned["Influenza"] = [0, ]*10
yearly_total_cleaned["Syncytial Virus"] = [0, ]*10
yearly_total_cleaned["Norovirus"] = [0, ]*10
yearly_total_cleaned["Metapneumovirus"] = [0, ]*10
yearly_total_cleaned["Rhinovirus"] = [0, ]*10
yearly_total_cleaned["Parainfluenza"] = [0, ]*10
yearly_total_cleaned["Respiratory"] = [0, ]*10
yearly_total_cleaned["Total"] = [0, ]*10

#### Clean data ####

#finding most common diseases to analyze
for i in range(2016, 2026):
    raw = pl.read_csv("data/01-raw_data/ob_report_" + str(i) + ".csv")
    for row in raw.rows(named = True):
        #getting causative agent
        if "Causative Agent-1" in row.keys():
            disease_one = row["Causative Agent-1"]
        else:
            disease_one = row["Causative Agent - 1"]
         
        if "Causative Agent-2" in row.keys():
            disease_two = row["Causative Agent-2"]
        else:
            disease_two = row["Causative Agent - 2"]

        #updating from agent 1
        if disease_one in most_common:
            most_common[disease_one] += 1
        else:
            most_common[disease_one] = 1

        #updating from agent 2
        if disease_two in most_common:
            most_common[disease_two] += 1
        else:
            most_common[disease_two] = 1

print(most_common)

count = 0
for key in most_common:
    if most_common[key] >= 50:
        count += 1
        print(most_common[key], key)
print(count)


# Analyzing more common outbreaks
#iterate through years with data
for i in range(2016, 2026):
    
    # reading & iterating through csv
    raw = pl.read_csv("data/01-raw_data/ob_report_" + str(i) + ".csv")
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
        index = i - 2016
        yearly_total_cleaned["Total"][index] += 1

        #updating yearly total respiratory count
        if "respiratory" in disease_type.lower():
            yearly_total_cleaned["Respiratory"][index] += 1

        #updating yearly total influenza count
        if (disease_one is not None and "influenza " in disease_one.lower()) or (
            disease_two is not None and "influenza " in disease_two.lower()):
            yearly_total_cleaned["Influenza"][index] += 1
        
        #updating yearly total coronavirus/covid count
        if (disease_one is not None and "covid" in disease_one.lower()) or (
            disease_two is not None and "covid" in disease_two.lower()):
            yearly_total_cleaned["Coronavirus"][index] += 1

        if (disease_one is not None and "corona" in disease_one.lower()) or (
            disease_two is not None and "corona" in disease_two.lower()):
            yearly_total_cleaned["Coronavirus"][index] += 1

        #updating yearly total Norovirus
        if (disease_one is not None and "norovirus" in disease_one.lower()) or (
            disease_two is not None and "norovirus" in disease_two.lower()):
            yearly_total_cleaned["Norovirus"][index] += 1

        #updating yearly total Metapneumovirus
        if (disease_one is not None and "metapneumovirus" in disease_one.lower()) or (
            disease_two is not None and "metapneumovirus" in disease_two.lower()):
            yearly_total_cleaned["Metapneumovirus"][index] += 1
        
        #updating yearly total Rhinovirus
        if (disease_one is not None and "rhinovirus" in disease_one.lower()) or (
            disease_two is not None and "rhinovirus" in disease_two.lower()):
            yearly_total_cleaned["Rhinovirus"][index] += 1

        #updating yearly total Parainfluenza
        if (disease_one is not None and "parainfluenza" in disease_one.lower()) or (
            disease_two is not None and "parainfluenza" in disease_two.lower()):
            yearly_total_cleaned["Parainfluenza"][index] += 1

         #updating yearly total Respiratory syncytial virus
        if (disease_one is not None and "syncytial" in disease_one.lower()) or (
            disease_two is not None and "syncytial" in disease_two.lower()):
            yearly_total_cleaned["Syncytial Virus"][index] += 1

### SAVE TO CSV ###
df = pl.DataFrame(yearly_total_cleaned)
df.write_csv("data/02-analysis_data/yearly_total_cleaned.csv")

