from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
ser = Service("./chromedriver")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser)#, options=op)
#driver = webdriver.Chrome('./chromedriver')
driver.maximize_window()
driver.get("https://www.rahulshettyacademy.com/angularpractice/")
python_web_title = driver.title
#print(driver.current_url)
#! Selenium 3 !#

# driver.find_element_by_css_selector("input[name='name']").send_keys("Lana879")
# driver.find_element_by_name("email").send_keys("Lana_test@gmail.com")
# driver.find_element_by_id("exampleInputPassword1").send_keys("Abcd1234")
# driver.find_element_by_id("exampleCheck1").click()
# driver.find_element_by_xpath("//input[@type='submit']").click()
# alert_text=driver.find_element_by_class_name("alert-success").text

#! Selenium 4 !#

driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Lana879")
driver.find_element(By.NAME,"email").send_keys("Lana_test@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("Abcd1234")
driver.find_element(By.ID,"exampleCheck1").click()
driver.find_element(By.XPATH,"//input[@type='submit']").click()
select = driver.find_element(By.ID , "exampleFormControlSelect1")
select = Select(driver.find_element(By.ID , "exampleFormControlSelect1"))
select.select_by_visible_text("Female")
select.select_by_index(0)
# select.select_by_value("Male")
# time.sleep(2)
alert_text = driver.find_element(By.CLASS_NAME, "alert-success").text

if "Success! The Form has been submitted successfully!." in alert_text:
    print("Submitted Successfully ")

print(alert_text)
# Clear the page
# driver.find_element(By.CSS_SELECTOR, "input[name='name']").clear()
# driver.find_element(By.NAME,"email").clear()
# driver.find_element(By.ID, "exampleInputPassword1").clear()
# driver.find_element(By.CSS_SELECTOR , "input[class='ng-untouched ng-pristine ng-valid']").clear()
# driver.find_element(By.ID,"exampleCheck1").click()

# Navigate  to shop web page
driver.find_element(By.LINK_TEXT,"Shop").click()

for _ in range(3):
    driver.find_element(By.CSS_SELECTOR,"div.container div.row div.col-lg-9 app-card-list.row app-card.col-lg-3.col-md-6.mb-3:nth-child(1) div.card.h-100 div.card-footer:nth-child(3) > button.btn.btn-info").click()
    driver.find_element(By.XPATH,"/html[1]/body[1]/app-root[1]/app-shop[1]/div[1]/div[1]/div[2]/app-card-list[1]/app-card[3]/div[1]/div[2]/button[1]").click()
    driver.find_element(By.CSS_SELECTOR,"div.container div.row div.col-lg-9 app-card-list.row app-card.col-lg-3.col-md-6.mb-3:nth-child(2) div.card.h-100 div.card-footer:nth-child(3) > button.btn.btn-info").click()
items_in_cards = driver.find_element(By.PARTIAL_LINK_TEXT, "Checkout").text

items = int(items_in_cards.split(" ")[2])
if items == 9:
    print("Test completed successfully ! ")
time.sleep(6)
# dropdown = Select(driver.find_element(By.id("exampleFormControlSelect1")))
# dropdown.selectByIndex(1)
# driver.find_element(By.CSS_SELECTOR , "input[id='form-check-label']").click()
driver.close()
