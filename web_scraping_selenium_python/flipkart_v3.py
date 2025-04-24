# Fetching all data from All pages ( 10 pages )

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd




# Path to chromedriver.exe
service = Service(r"C:\Users\Dell\Desktop\scraping\chromedriver-win64\chromedriver.exe")

#Setting Options To AVOID getting browser close automatically
chrome_options = Options()
chrome_options.add_experimental_option("detach",True)
chrome_options.add_argument("--headless")

# Create the driver with the service
driver = webdriver.Chrome(service=service,options=chrome_options)
driver.maximize_window()
# link for webpage
driver.get("https://www.flipkart.com/search?q=smartwatch&sid=ajy%2Cbuh&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_na&as-pos=1&as-type=RECENT&suggestionId=smartwatch%7CSmart+Watches&requestId=86f906fd-b529-4f70-b969-e3cfc7a7e317&as-backfill=on")

#Creating empty list to store values and create df from it.
watch_name = []
current_price = []
mrp = []
discount = []
description = []

for page_num in range(1, 11):
    xpath_page_value = 11 if page_num == 1 else 12
    for i in range(1,11): # number of rows on page
        for j in range(1,4): # number of product in each row
            # 1 : Watch Name
            try:
                watch_name_element = driver.find_element('xpath',f'/html/body/div/div/div[3]/div[1]/div[2]/div[{i}]/div/div[{j}]/div/div/a[1]')
                watch_name.append(watch_name_element.text)
            except:
                watch_name.append("NIL")

            # 2 : Watch price
            try:
                current_price_element = driver.find_element('xpath',f'/html/body/div/div/div[3]/div[1]/div[2]/div[{i}]/div/div[{j}]/div/div/a[2]/div/div[1]')
                current_price.append(current_price_element.text)
            except:
                current_price.append("NIL")


            #3 : mrp_price_element
            try:
                mrp_element = driver.find_element('xpath',f'/html/body/div/div/div[3]/div[1]/div[2]/div[{i}]/div/div[{j}]/div/div/a[2]/div/div[2]')
                mrp.append(mrp_element.text)
            except:
                mrp.append("NIL")

            #4 : Discount
            try:
                discount_element = driver.find_element('xpath',f'/html/body/div/div/div[3]/div[1]/div[2]/div[{i}]/div/div[{j}]/div/div/a[2]/div/div[3]/span')
                discount.append(discount_element.text)
            except:
                discount.append("NIL")

            #5 Description
            try:
                description_element = driver.find_element('xpath',f'/html/body/div/div/div[3]/div/div[2]/div[{i}]/div/div[{j}]/div/div/div[2]')
                description.append(description_element.text)
            except:
                description.append("NIL")

                                            
    
    try:
        next_button_xpath = f'/html/body/div/div/div[3]/div[1]/div[2]/div[12]/div/div/nav/a[{xpath_page_value}]/span'
        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, next_button_xpath))
        )
        next_button.click()
        time.sleep(3)  # let the next page load
    except Exception as e:
        print(f"Could not click next page: {e}")
        break



#Creating dictionary
data_records = {'watch_name': watch_name,
                'current_price':current_price,
                'mrp':mrp,
                'discount': discount,
                'description': description}

df = pd.DataFrame(data_records)
df.to_excel('Output_records.xlsx', index=False)