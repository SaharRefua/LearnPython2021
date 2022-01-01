from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('./chromedriver')
driver.get("https://www.askpython.com/")
print(driver.title)
search_bar = driver.find_element_by_css_selector("#search-2 > form > label > input")
search_bar.send_keys("random")
driver.click()

# search_bar.clear()
# search_bar.send_keys(Keys.RETURN)
# print(driver.current_url)
# driver.close()