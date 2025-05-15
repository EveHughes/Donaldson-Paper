#### Preamble ####
# Purpose: Downloads and saves the data from Outbreaks in Toronto Healthcare Institutions
# Author: Evelyn Hughes
# Date: 14 May 2025
# Contact: evelyn.hughes@mail.utoronto.ca
# License: MIT
# Pre-requisites: 
  # - `polars` must be installed (pip install polars)
  # - `numpy` must be installed (pip install numpy)
  # - `io` must be installed (pip install io)

#### Workspace setup ####
import polars as pl
from io import StringIO
from datetime import datetime

#### Download data ####
import requests

# Toronto Open Data is stored in a CKAN instance. It's APIs are documented here:
# https://docs.ckan.org/en/latest/api/

# To hit our API, you'll be making requests to:
base_url = "https://ckan0.cf.opendata.inter.prod-toronto.ca"

# Datasets are called "packages". Each package can contain many "resources"
# To retrieve the metadata for this package and its resources, use the package name in this page's URL:
url = base_url + "/api/3/action/package_show"
params = { "id": "outbreaks-in-toronto-healthcare-institutions"}
package = requests.get(url, params = params).json()

# To get resource data:
date = str(datetime.today()).split()[0]
year = int(date[:4])
for idx, resource in enumerate(package["result"]["resources"]):

       # for datastore_active resources:
       if resource["datastore_active"]:
            # To get all records in CSV format:
            url = base_url + "/datastore/dump/" + resource["id"]
            resource_dump_data = requests.get(url)

            # Writing raw data to CSV
            analysis_data = pl.read_csv(StringIO(resource_dump_data.text))
            analysis_data.write_csv("data/01-raw_data/" + date + "_ob_report_" + str(year) + ".csv")
            year-=1