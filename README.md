# Geocoding_with_Selenium_and_Google_Maps


This repository contains a Python script that demonstrates how to perform geocoding using Selenium and Google Maps API. The script scrapes a website for location data, extracts the addresses, and geocodes them to obtain latitude and longitude coordinates.

## Prerequisites

Before running the script, make sure you have the following dependencies installed:

- Python (version 3.x)
- pandas
- selenium
- beautifulsoup4
- googlemaps
- gmaps

You will also need to have the Chrome web browser and the corresponding ChromeDriver installed.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/kaluka/Geocoding_with_Selenium_and_Google_Maps.git
   
2. Install the required Python dependencies:  

 ``` pip install -r requirements.txt   ```

3. Obtain a Google Maps API key by following the instructions [here.([url](https://developers.google.com/maps/documentation/geocoding/get-api-key))]
4. Replace the placeholder 'YOUR API KEY' in the code with your actual Google Maps API key.

Usage
Open a terminal and navigate to the cloned repository:

``
cd your-repository  ``

Run the Python script:

``
python geocoding_script.py  ``

The script will scrape the website, extract the addresses, geocode them, and update the latitude and longitude values in the DataFrame.
