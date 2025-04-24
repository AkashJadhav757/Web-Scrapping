from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.by import By
import time


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

for i in range(1,11):
    for j in range(1,4):
        # 1 : Watch Name
        try:
            watch_name_element = driver.find_element('xpath',f'/html/body/div/div/div[3]/div[1]/div[2]/div[{i}]/div/div[{j}]/div/div/a[1]')
            watch_name = watch_name_element.text
        except:
            watch_name = ""

        # 2 : Watch price
        try:
            current_price_element = driver.find_element('xpath',f'/html/body/div/div/div[3]/div[1]/div[2]/div[{i}]/div/div[{j}]/div/div/a[2]/div/div[1]')
            current_price = current_price_element.text
        except:
            current_price = ""


        #3 : mrp_price_element

        try:
            mrp_element = driver.find_element('xpath',f'/html/body/div/div/div[3]/div[1]/div[2]/div[{i}]/div/div[{j}]/div/div/a[2]/div/div[2]')
            mrp = mrp_element.text
        except:
            mrp = ""
        #4 : Discount

        try:
            discount_element = driver.find_element('xpath',f'/html/body/div/div/div[3]/div[1]/div[2]/div[{i}]/div/div[{j}]/div/div/a[2]/div/div[3]/span')
            discount = discount_element.text
        except:
            discount = ""

        #5 Description
        try:
            description_element = driver.find_element('xpath',f'/html/body/div/div/div[3]/div/div[2]/div[{i}]/div/div[{j}]/div/div/div[2]')
            description = description_element.text
        except:
            description = ""





                            
        print("=====================")

        print('watch name: ',watch_name)
        print('current_price: ',current_price)
        print('mrp: ',mrp)
        print('discount: ',discount)
        print('description:',description)

        print("=====================")
