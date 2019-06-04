from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Datetime
import datetime
import time

# Raw data
from raw import berlin_to_munich



# Bus Transportation
flixbus_url = 'https://global.flixbus.com/'

# Volatile path
browser = webdriver.Chrome(executable_path=r"C:/Users/varun/Documents/Selenium/chromedriver.exe")

browser.get(flixbus_url)

# Starting Destination 
starting_field = browser.find_element_by_xpath(xpath = '//*[@id="search-mask-component"]/div/div[1]/div/div[1]/div/div[1]/div[1]/div/input')

# To Destination
destination_field = browser.find_element_by_xpath(xpath = '//*[@id="search-mask-component"]/div/div[1]/div/div[2]/div/div[1]/div/input')

search_field = browser.find_element_by_xpath(xpath = '//*[@id="search-mask-component"]/div/div[4]/div/button')

starting_field.send_keys('Berlin')
starting_field.send_keys(Keys.ENTER)
destination_field.send_keys('Munich')
destination_field.send_keys(Keys.ENTER)

# Ensure that fields are entered appropriately
search_field.click()


time.sleep(5)

price_tree = browser.find_element_by_xpath('//*[@id="results-group-container-direct"]')


"""
elem = browser.find_element_by_css_selector('.entry-content > ol:nth-child(15) > li:nth-child(1) > a:nth-child(1)')

elem.text

elem.click()
browser.quit()
"""

# if __name__ == "__main__":
