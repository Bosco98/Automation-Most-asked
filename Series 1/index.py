import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
PATH = "/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome"

options = webdriver.ChromeOptions()
options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
chrome_driver_binary = "/Users/bosco.c/Desktop/Test JS/chromedriver"
driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)

driver.get('http://127.0.0.1:5500/index.html')

time.sleep(2)
dropdown = driver.find_element(By.ID, 'fruits')
select = Select(dropdown)

select.select_by_visible_text('Mango')
# select.deselect_by_visible_text("your text")
# select.deselect_by_value("your text")
# select.select_by_index("your text")
# select.deselect_all("your text")

time.sleep(2)
driver.quit()
