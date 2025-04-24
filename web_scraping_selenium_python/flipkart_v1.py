from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.by import By
import time

# 
# 
# stars_element
# rating_element
# review_element
# next_page_element

# Path to chromedriver.exe
service = Service(r"C:\Users\Dell\Desktop\scraping\chromedriver-win64\chromedriver.exe")

#Setting Options To AVOID getting browser close automatically
chrome_options = Options()
chrome_options.add_experimental_option("detach",True)

# Create the driver with the service
driver = webdriver.Chrome(service=service,options=chrome_options)
driver.maximize_window()
# link for webpage
driver.get("https://www.flipkart.com/search?q=smartwatch&sid=ajy%2Cbuh&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_na&as-pos=1&as-type=RECENT&suggestionId=smartwatch%7CSmart+Watches&requestId=86f906fd-b529-4f70-b969-e3cfc7a7e317&as-backfill=on")

# 1 : Watch Name
watch_name_element = driver.find_element('xpath','/html/body/div/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/div/div/a[1]')
watch_name = watch_name_element.text

# 2 : Watch price
current_price_element = driver.find_element('xpath','/html/body/div/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/div/div/a[2]/div/div[1]')
current_price = current_price_element.text

#3 : mrp_price_element

mrp_element = driver.find_element('xpath','/html/body/div/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/div/div/a[2]/div/div[2]')
mrp = mrp_element.text

#4 : Discount

discount_element = driver.find_element('xpath','/html/body/div/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/div/div/a[2]/div/div[3]/span')
discount = discount_element.text

#5 Description

description_element = driver.find_element('xpath','/html/body/div/div/div[3]/div/div[2]/div[2]/div/div[1]/div/div/div[2]')
description = description_element.text




                            
print("=====================")

print('watch name: ',watch_name)
print('current_price: ',current_price)
print('mrp: ',mrp)
print('discount: ',discount)
print('description:',description)

print("=====================")
