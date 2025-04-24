# from selenium import webdriver

# driver = webdriver.Chrome(executable_path=r'C:\Users\Dell\Desktop\scraping\chromedriver-win64\chromedriver.exe')


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
driver.get("https://www.google.com")

# 1 - Xpath method

# input = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[1]/div[2]/textarea')
# input.send_keys("Flipkart")

#2 - Class_name method
# input = driver.find_element(By.CLASS_NAME,'gLFyf').send_keys("Facebook")

# #2 tag method
search_box = driver.find_element(By.TAG_NAME,'textarea')
search_box.send_keys("Youtube")
#search_box.send_keys(Keys.RETURN)

time.sleep(20)

driver.find_element(By.XPATH,"/html/body/div[1]/div[2]").click()
time.sleep(2)

#driver.find_element(By.XPATH,"/html/body/div[2]/div[3]/div[1]/div/div/span/div[1]").click()
search_button = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]').click()