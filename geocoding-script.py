#import dependencies
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from googlemaps import Client as GoogleMaps
import googlemaps
import gmaps


# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--window-size=1920,1080")


# Path to chromedriver executable
chromedriver_path = '/usr/local/bin/chromedriver'


# Set up Selenium driver
driver = webdriver.Chrome(executable_path=chromedriver_path, options=chrome_options)


# Load the website
url = 'https://internet.safaricom.co.ke/5g-wireless/coverage'
driver.get(url)


# Wait for the table to be loaded
wait = WebDriverWait(driver, 10)
table = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="5G-coverage"]/div[2]/div/div/div/div[2]/table')))


# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(table.get_attribute('outerHTML'), 'html.parser')

# Extract the table data using Pandas
dfs = pd.read_html(str(soup))
df = dfs[0]

#drop the County and Area columns
df = df.drop(['County', 'Area'] , axis=1)

# Separate the entries into rows
df = df['Place/Estate'].str.split(', ', expand=True).stack().reset_index(level=1, drop=True).to_frame('Place/Estate')

# Reset the index of the DataFrame
df = df.reset_index(drop=True)

#drop duplicate entries
df=df.drop_duplicates(keep='last')

# This is where we will need the API key
gmaps = googlemaps.Client(key='YOUR API KEY')


address = df.iloc[:, -1:].copy()  # Selecting the last column of the DataFrame and making a copy
address.loc[:, 'long'] = ""  # Setting empty values in the 'long' column
address.loc[:, 'lat'] = ""  # Setting empty values in the 'lat' column

# Iterate over the indices of the DataFrame 'address'
for x in range(len(address)):
    # Perform geocoding for the address at index 'x'
    geocode_result = gmaps.geocode(address.loc[x, 'Place/Estate'])
    
    # Check if a geocoding result is obtained
    if geocode_result:
        # Update the 'lat' column of 'addresses2' with the latitude value from the geocoding result
        address.at[x, 'lat'] = geocode_result[0]['geometry']['location']['lat']
        
        # Update the 'long' column of 'addresses2' with the longitude value from the geocoding result
        address.at[x, 'long'] = geocode_result[0]['geometry']['location']['lng']
    else:
        # Set the 'lat' column to None if no geocoding result is obtained
        address.at[x, 'lat'] = None
        
        # Set the 'long' column to None if no geocoding result is obtained
        address.at[x, 'long'] = None
        
# Data to add
data = [
    ('Karen', -1.31294888109111, 36.68288232510159),
    ('Utawala', -1.3334768985469356, 36.67656180973276),
    ('Ushirika', -1.2724597960984732, 36.84438912079378),
    ('Zimmerman', -1.2089039495782525, 36.898427146205144),
    ('Junction', -1.2985895292447076, 36.76320215391012),
    ('Lower Riat Estate', -0.053248757434864, 34.739411198093606),
    ('Mamboleo', -0.05796940333424934, 34.78539405944491),
    ('St Aloys Ojola', -0.05982833865938444, 34.65003218274472),
    ('Kirigiti', -1.1713665430229177, 36.841963772341195)
]

# Iterate over the data items
for item in data:
    # Unpack the item into place, longitude, and latitude variables
    place, longitude, latitude = item
    
    # Update the 'long' and 'lat' columns of 'address' where the 'Place/Estate' matches the 'place' value
    address.loc[address['Place/Estate'] == place, ['lat', 'long']] = latitude, longitude
    
    
    
    
        
