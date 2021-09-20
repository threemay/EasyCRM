from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


driver = webdriver.Remote(
   command_executor='http://localhost:4444/wd/hub',
   desired_capabilities=DesiredCapabilities.FIREFOX)

driver.get("http://0.0.0.0:8090/login")


username = driver.find_element_by_name('username')
password = driver.find_element_by_name('password')
username.clear()
username.send_keys("test@gmail.com")
password.clear()
password.send_keys("shh")
driver.find_element_by_xpath('//input[@type="submit"]').click()