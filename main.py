from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.common.by import By

"""Simple web scraper to find first 3 flights and prices between requested airports and date """

# input data for seeking
print("You are welcome in Flight Scrap!")
from_aeroport = input("Input please departure airport: ")
to_aeroport = input("Input please destinations airport: ")
dispatch_date = input("Input please the dispatch date: ")

# initiation scraper
driver = webdriver.Chrome()
driver.get('https://fly2.emirates.com/CAB/IBE/SearchAvailability.aspx')

# need to accept cookies by click on appropriate button
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="onetrust-accept-btn-handler"]'))).click()

# cause the cookies question need to initiate New Search by clicking
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'ts-session-expire--link'))).click()
sleep(3)

# first of all need to choose One Way type of ticket
driver.find_element(By.ID, 'ctl00_c_CtWNW_ltOneway').click()

# then find the form for dispatch airport and put there our data
input_FROM_aeroport = driver.find_element(By.ID, 'ctl00_c_CtWNW_ddlFrom-suggest')
input_FROM_aeroport.send_keys(from_aeroport)

# in the same way find arrival airport place and put there already our data
input_TO_aeroport = driver.find_element(By.CSS_SELECTOR, '#ctl00_c_CtWNW_ddlTo-suggest')
input_TO_aeroport.send_keys(to_aeroport)

# the same case with date field
driver.implicitly_wait(10)
driver.find_element(By.ID, 'txtDepartDate').click()
xpath_for_date = f"//*[@id='day-{dispatch_date}']"
driver.find_element(By.XPATH, xpath_for_date).click()

# click on search button
driver.find_element(By.ID, 'ctl00_c_IBE_PB_FF').click()

# Working with results
print("Your results are next:")

# Dictionary for keep results
dict_for_results = {'flight time': '', 'flight cost': ''}

# find prices on the flights page
res_cost = driver.find_elements(By.XPATH, "//*[contains(text(), 'PriceResult')]")
print(res_cost)

# close the driver
driver.quit()
