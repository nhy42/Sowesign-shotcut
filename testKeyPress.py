from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from time import sleep

s = Service("chromedriver.exe")
print("Launching driver")
driver = webdriver.Chrome(service=s)
sleep(1)
print("Going to truc")
driver.get("file:///D:/Sowesign-shotcut/testKeyPress.html")
sleep(1)
print("Typing School Code : ")
ActionChains(driver).send_keys(Keys.NUMPAD0).perform()
