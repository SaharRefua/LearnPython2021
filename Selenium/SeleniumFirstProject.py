from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#driver = webdriver.Chrome('./chromedriver')  C:\\PythonProjects\\LearnPython2021\\Selenium\\
driver = webdriver.Firefox(executable_path="./geckodriver")
driver.maximize_window()
driver.get("https://www.python.org")
python_web_title = driver.title
print(driver.current_url)
driver.get("https://stackoverflow.com/questions/64717302/deprecationwarning-executable-path-has-been-deprecated-selenium-python")

driver.back()
if python_web_title != driver.title:
    print("You got back to python website !")

else:
    assert ("Test failed !")
driver.refresh()


# search_bar = driver.find_element_by_name("q")
# search_bar.clear()
# search_bar.send_keys("getting started with python")
# search_bar.send_keys(Keys.RETURN)
# print(driver.current_url)
#driver.close() # close current window
#driver.quit() # close multipule windows