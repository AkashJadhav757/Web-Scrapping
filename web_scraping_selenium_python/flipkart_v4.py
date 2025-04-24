# Fetching all data from All pages ( 10 pages )

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd

print("[INFO] Script started...")

# Path to chromedriver.exe
service = Service(r"C:\Users\Dell\Desktop\scraping\chromedriver-win64\chromedriver.exe")

# Setting Options To AVOID getting browser close automatically
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--headless")

# Create the driver with the service
print("[INFO] Launching Chrome browser...")
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()

# link for webpage
url = "https://www.flipkart.com/search?q=smartwatch&sid=ajy%2Cbuh&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_na&as-pos=1&as-type=RECENT&suggestionId=smartwatch%7CSmart+Watches&requestId=86f906fd-b529-4f70-b969-e3cfc7a7e317&as-backfill=on"
print(f"[INFO] Opening URL: {url}")
driver.get(url)

# Creating empty list to store values and create df from it
watch_name = []
current_price = []
mrp = []
discount = []
description = []

for page_num in range(1, 11):
    print(f"\n[INFO] Scraping Page {page_num}")
    xpath_page_value = 11 if page_num == 1 else 12

    for i in range(1, 11):  # number of rows on page
        for j in range(1, 4):  # number of product in each row
            print(f"[DEBUG] Extracting row {i}, column {j}...")

            # 1 : Watch Name
            try:
                element = driver.find_element('xpath', f'/html/body/div/div/div[3]/div[1]/div[2]/div[{i}]/div/div[{j}]/div/div/a[1]')
                watch_name.append(element.text)
            except:
                watch_name.append("NIL")

            # 2 : Watch price
            try:
                element = driver.find_element('xpath', f'/html/body/div/div/div[3]/div[1]/div[2]/div[{i}]/div/div[{j}]/div/div/a[2]/div/div[1]')
                current_price.append(element.text)
            except:
                current_price.append("NIL")

            # 3 : MRP price
            try:
                element = driver.find_element('xpath', f'/html/body/div/div/div[3]/div[1]/div[2]/div[{i}]/div/div[{j}]/div/div/a[2]/div/div[2]')
                mrp.append(element.text)
            except:
                mrp.append("NIL")

            # 4 : Discount
            try:
                element = driver.find_element('xpath', f'/html/body/div/div/div[3]/div[1]/div[2]/div[{i}]/div/div[{j}]/div/div/a[2]/div/div[3]/span')
                discount.append(element.text)
            except:
                discount.append("NIL")

            # 5 : Description
            try:
                element = driver.find_element('xpath', f'/html/body/div/div/div[3]/div/div[2]/div[{i}]/div/div[{j}]/div/div/div[2]')
                description.append(element.text)
            except:
                description.append("NIL")

    # Next Page Click
    try:
        next_button_xpath = f'/html/body/div/div/div[3]/div[1]/div[2]/div[12]/div/div/nav/a[{xpath_page_value}]/span'
        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, next_button_xpath))
        )
        next_button.click()
        time.sleep(3)
        print(f"[INFO] Moving to next page...")
    except Exception as e:
        print(f"[ERROR] Could not click next page on page {page_num}: {e}")
        break

# Creating dictionary
print("\n[INFO] Creating DataFrame...")
data_records = {
    'watch_name': watch_name,
    'current_price': current_price,
    'mrp': mrp,
    'discount': discount,
    'description': description
}

# Creating DATAFRAME From dictionary
df = pd.DataFrame(data_records)

# Saving to Excel
timestamp = pd.Timestamp.now().strftime('%Y-%m-%d_%H-%M')
output_file = f'Output_records_{timestamp}.xlsx'
df.to_excel(output_file, index=False)
print(f"[INFO] Data saved to Excel file: {output_file}")
print("[INFO] Script completed successfully.")
