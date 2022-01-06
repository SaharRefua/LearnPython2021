from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
driver = webdriver.Chrome('chromedriver')
driver.get("https://www.linkedin.com/")
driver.maximize_window() #set_window_size(1890, 1300)

user_name= driver.find_element(By.ID, "session_key")
password= driver.find_element(By.ID,"session_password")

user_name.send_keys("refua.sahar@gmail.com")
password.send_keys("citso2016")
submit= driver.find_element(By.XPATH,'''//*[@id="main-content"]/section[1]/div/div/form/button''').click()
print(driver.title)
if "Linkin" in driver.title :
    print("Link in successfully ! ")

#assert "Python" in driver.title
#time.sleep(2)
driver.get("https://www.linkedin.com/learning/?trk=nav_neptune_learning")
search_bar = driver.find_element(By.XPATH, '''/html/body/div[3]/div[1]/nav[1]/div/div[2]/div/div/ul[1]/li[2]/div/div/div[1]/div/input''')
search_bar.send_keys("post man")
search_button = driver.find_element(By.XPATH , '''//*[@id="ember1388"]/div/input''')
search_button.click()
time.sleep(2)

driver.close()



# import unittest
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
#
# class PythonOrgSearch(unittest.TestCase):
#
#     def setUp(self):
#         self.driver = webdriver.Chrome()
#
#     def test_search_in_python_org(self):
#         driver = self.driver
#         driver.get("http://www.python.org")
#         self.assertIn("Python", driver.title)
#         elem = driver.find_element_by_name("q")
#         elem.send_keys("pycon")
#         elem.send_keys(Keys.RETURN)
#         assert "No results found." not in driver.page_source
#
#
#     def tearDown(self):
#         self.driver.close()
#
# if __name__ == "__main__":
#     unittest.main()