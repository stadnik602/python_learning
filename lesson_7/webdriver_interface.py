from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.fullscreen_window()
browser.get("https://the-internet.herokuapp.com/")
browser.get("https://google.com")
browser.back()
browser.forward()
browser.refresh()
browser.quit()
