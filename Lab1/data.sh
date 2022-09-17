#!/bin/bash

for year in {2020..2022}; 
do wget  --content-disposition "https://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID=48549&Year=${year}&Month=2&timeframe=1&submit= Download+Data";
done;

python3 concatenate.py