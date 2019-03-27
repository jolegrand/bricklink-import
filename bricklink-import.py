import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import Select

# Using Chrome to access web
driver = webdriver.Firefox()

# Open the website
driver.get('https://www.bricklink.com/v2/wanted/upload.page?utm_content=subnav')

# Select the id box
id_box = driver.find_element_by_name('frmUsername')
# Send id information
id_box.send_keys('jolegrand@no-log.org')

# Select the id box
pass_box = driver.find_element_by_name('frmPassword')
# Send id information
pass_box.send_keys('f2bricklink')

# Find login button
login_button = driver.find_element_by_id('blbtnLogin')
# Click login
login_button.click()

# Wait till the page is loaded
driver.implicitly_wait(3) 
select = Select(driver.find_element_by_id('wantedlist_select'))
select.select_by_value("-1") # Create New Wanted List


name_box = driver.find_element_by_name('newWantedMore')
name_box.send_keys('toto')

driver.implicitly_wait(3) 
send_box = driver.find_element_by_name('file')
send_box.send_keys("/home/joel/bricklink-export/2087582.bsx")


send_box = driver.find_element_by_id('button-add-all')
send_box.click()

driver.implicitly_wait(3) 

button = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[1]/div/div/div/div[2]/span/button")
button.click()
