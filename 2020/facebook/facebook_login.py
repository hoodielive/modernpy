from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

browser = webdriver.Firefox()

browser.get("http://www.facebook.com")

username = browser.find_element_by_id("email")
username = browser.find_element_by_id("pass")
username = browser.find_element_by_id("loginbutton")

username.send_keys("nikudmusiq@gmail.com")
username.send_keys("binah123")

submit.click()
