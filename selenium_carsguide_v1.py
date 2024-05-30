import os, sys, csv, time, glob, re, datetime,subprocess
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from tqdm import tqdm
import numpy as np
import pandas as pd
import random

############ SETUP
CURR_PATH = os.getcwd()
input_file = 'Sample data_veh.xlsx'
options = Options()
# options.add_argument("--headless")

############ FUNCTIONS

# write pandas dataframe to csv file
def dataframe_to_csv(filename, DataFrame):
    """Export entire DataFrame to csv."""
    output = DataFrame
    output.to_csv(filename, index=False)

# get html source source
def get_html(filename, url, browser):
    if os.path.exists(filename):  # CHANGE for euro / champions / europa / world cup
        pass
    else:
        try:
            browser.get(url)  # navigate to start url
            time.sleep(2)
            html = browser.page_source  # extract the HTML source code of start url
            with open(filename, 'w', encoding='utf8') as f:
                f.write(html)
        except:
            pass
def find_indices(main_list, search_strings):
    return [i for i, item in enumerate(main_list) if item.text in search_strings]
# ----------------------------------------------------------------------------------------------------------------------

## 1) Tennis-Category-Year Data (dataframe of all tournaments in that tennis category - cat_name, tourn_name, tourn_url, tourn_years, year_urls)

# Establish web connection and maximise the window
browser = webdriver.Chrome(options=options)  # establish web connection
browser.maximize_window()  # maximize the browser window
time.sleep(0.5)

# Travel to Base URL for Carsguide
base_url = 'https://www.carsguide.com.au/price'
browser.get(base_url)  # navigate to base site
time.sleep(1)

# Read in the input dataframe
input_df = pd.read_excel(CURR_PATH + '/' + input_file, header=0)

# For each row of the input dataframe
for i in range(0,len(input_df)):
    make = input_df.iloc[i,0]
    model = input_df.iloc[i, 1]
    year = input_df.iloc[i, 2]
    browser.get(base_url)  # navigate to base site
    time.sleep(1)
    element = browser.find_element(By.NAME, 'vehicle_make')
    select = Select(element) # Initialize the Select class with the dropdown element
    select.select_by_visible_text(str(make.title())) # Select the option by visible text
    element = browser.find_element(By.NAME, 'vehicle_model_group')
    select = Select(element)  # Initialize the Select class with the dropdown element
    select.select_by_visible_text(str(model.title()))  # Select the option by visible text
    element = browser.find_element(By.NAME, 'vehicle_years')
    select = Select(element)  # Initialize the Select class with the dropdown element
    select.select_by_visible_text(str(year))  # Select the option by visible text
    element = browser.find_element(By.ID, 'search-site-section')
    time.sleep(2)
    # So we are now at the page that looks like https://www.carsguide.com.au/mitsubishi/lancer/price/2019
    # Next, you need to find the element/inspect the table and iterate through the values in the table to choose e.g. the cheapest one and then "click()" to travel to that url
    # Finally, we scrape the data required from the webpages that look like: https://www.carsguide.com.au/mitsubishi/lancer/price/2019/gsr-sportback?id=BlTMFFkV



element5 = WebDriverWait(element2, 3).until(expected_conditions.visibility_of_elements_located((By.CLASS_NAME, 'class-row')))

countries = browser.find_element(By.XPATH,'/html/body/div[6]/div/div[1]/div[3]/div/div/table').find_elements(By.CLASS_NAME,'table-row')



# ----------------------------------------------------------------------------------------------------------------------

