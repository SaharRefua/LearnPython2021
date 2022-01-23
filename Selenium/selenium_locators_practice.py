from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('./chromedriver')
driver.maximize_window()
driver.get("https://www.rahulshettyacademy.com/angularpractice/")
python_web_title = driver.title
print(driver.current_url)
# Selenium 3 #
# driver.find_element_by_css_selector("input[name='name']").send_keys("Lana879")
# driver.find_element_by_name("email").send_keys("Lana_test@gmail.com")
# driver.find_element_by_id("exampleInputPassword1").send_keys("Abcd1234")
# driver.find_element_by_id("exampleCheck1").click()
# driver.find_element_by_xpath("//input[@type='submit']").click()
# alert_text=driver.find_element_by_class_name("alert-success").text

# Selenium 4 #
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Lana879")
driver.find_element(By.NAME,"email").send_keys("Lana_test@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("Abcd1234")
driver.find_element(By.ID,"exampleCheck1").click()
driver.find_element(By.XPATH,"//input[@type='submit']").click()
alert_text=driver.find_element(By.CLASS_NAME, "alert-success").text

# dropdown = driver.find_element(By.id("exampleFormControlSelect1"))
# dropdown.selectByIndex(1)
driver.find_element(By.CSS_SELECTOR , "input[id='form-check-label']").click()

print(alert_text)
