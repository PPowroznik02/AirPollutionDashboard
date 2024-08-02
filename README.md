# Real-Time Air Pollution Dashboard

## Overview
This project provides a [Real-Time Air Pollution Dashboard](https://agh-ust.maps.arcgis.com/apps/dashboards/9f43cb8a004e487b86a8ce1f40ff52e6) for Poland using data from the [GIOS](https://www.gios.gov.pl/pl/) API. The data is read and processed using a Python script and uploaded to an [ArcGIS](https://www.arcgis.com) server every hour.

## Usage
- Edit the configuration file 'logowanie.json' to provide your ArcGis login and password.

```
{
  "login": "user_name",
  "haslo": "password"
}
```

- Script initiate_upload.py

This script is used to create and upload the initial hosted layer on the ArcGIS server. Run this script before running the upload_data.py script.
```bash
python initiate_upload.py
```

- Script upload_data.py

This script reads the real-time air pollution data from the GIOS API, processes it, and uploads it to the ArcGIS server. This script is intended to be run every hour.
```
python upload_data.py
```

## Dashboard Features

The real-time air pollution dashboard includes the following visualization sections:

- Map with Sensor Layer: Displays the locations of air quality sensors across Poland.
- Legend: Provides information on the symbols and colors used in the map.
- Parameter Selector: Allows users to select different air quality parameters to view (e.g., PM2.5, PM10, NO2).
- List of Measured Values: Shows the current measured values for selected parameters.
- Attribute Table: Contains detailed information about each sensor and its readings.
- Concentration Value Chart: Displays a time-series chart of concentration values for the selected parameter.
- Pie Chart of the Percentage Distribution of Sensors: Shows the distribution of sensors.
![Dashboard](/dashboard.png)