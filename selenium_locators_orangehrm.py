from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
#from sys import executable
import time
from utility import highlighter
from selenium.webdriver.common.by import By

service = Service(executable_path= "chromedriver.exe")
driver = webdriver.Chrome(service = service)
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

driver.implicitly_wait(2)

#Username
name = driver.find_element(By.NAME,"username")
highlighter.highlight(name)
name.send_keys("Admin")
time.sleep(2)

#Password
password = driver.find_element(By.NAME, "password")
highlighter.highlight(password)
password.send_keys("admin123")
time.sleep(2)

#Login button
login_button = driver.find_element(By.CSS_SELECTOR, ".oxd-button.oxd-button--medium.oxd-button--main.orangehrm-login-button")
highlighter.highlight(login_button)
#login_button.click()
time.sleep(2)#

#driver.execute_script("windows.scroll,(0, 1250)")

#Forgot password
forgot_pw = driver.find_element(By.CSS_SELECTOR, ".oxd-text.oxd-text--p.orangehrm-login-forgot-header")
highlighter.highlight(forgot_pw)
#forgot_pw.click()
time.sleep(2)



#CSS SELECTOR
icons = driver.find_element(By.CSS_SELECTOR, "div a:nth-child(1)")
#for icon in icons:
highlighter.highlight(icons)
time.sleep(5)


print("Login successful (if your credentials didn’t fail you).")








