#!/usr/bin/env python

import csv, requests

# Data sources (coronakartan.se)
corona_deaths_url = "https://raw.githubusercontent.com/elinlutz/gatsby-map/master/src/data/time_series/time_series_deaths-deaths.csv"
corona_confirmed_url = "https://raw.githubusercontent.com/elinlutz/gatsby-map/master/src/data/time_series/time_series_confimed-confirmed.csv"

# HTTP requests
corona_deaths_req = requests.get(corona_deaths_url)
corona_confirmed_req = requests.get(corona_confirmed_url)

# Iterate CSV
def parse_csv(corona_csv):
  reader = corona_csv.iter_lines()
  result = csv.DictReader(reader, delimiter=',')
  return result

corona_deaths_csv = parse_csv(corona_deaths_req)
corona_confirmed_csv = parse_csv(corona_confirmed_req)

# Extract values from csv
def extract_from_csv(corona_stats):
  listsplit = list(corona_stats.split("\n"))
  value = int(listsplit[-1])
  return value

# Get number of deaths
for row in corona_deaths_csv:
  corona_total_deaths=(row["Today"])
corona_total_deaths = extract_from_csv(corona_total_deaths)

# Get number ofconfirmed & hospitalized
for row in corona_confirmed_csv:
  corona_total_confirmed=(row["Today"])
  corona_at_hospital=(row["At_Hospital"])
  corona_at_icu=(row["At_ICU"])

corona_total_confirmed = extract_from_csv(corona_total_confirmed)
corona_at_hospital_total = extract_from_csv(corona_at_hospital)
corona_at_icu_total = extract_from_csv(corona_at_icu)
# Calculate number of hospitalized (hospital + icu)
corona_total_hospitalized = int(corona_at_hospital_total) + int(corona_at_icu_total)

# Print Naemon style
print "INFO: Deaths: " + str(corona_total_deaths) + " Confirmed: " + str(corona_total_confirmed) + " Hospitalized: " + str(corona_total_hospitalized) + " | deaths=" + str(corona_total_deaths) + " confirmed=" + str(corona_total_confirmed) + " hospitalized=" + str(corona_total_hospitalized)
