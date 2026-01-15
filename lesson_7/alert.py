from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

js_alert_button_element = "//li[1]/button"
js_confirm_button_element = "//li[2]/button"
js_prompt_button_element = "//li[3]/button"
result_text_element = "result"

browser = webdriver.Firefox()
def open_page():
    browser.get("https://the-internet.herokuapp.com/javascript_alerts")
def click_on_js_alert_button():
    browser.find_element(By.XPATH, js_alert_button_element).click()
def click_on_js_confirm_button():
    browser.find_element(By.XPATH, js_confirm_button_element).click()
def click_on_prompt_button():
    browser.find_element(By.XPATH, js_prompt_button_element).click()
def get_result_text():
    text = browser.find_element(By.ID, result_text_element).text
    print(text)
def accept_alert():
    alert = browser.switch_to.alert
    print(alert.text)
    alert.accept()
    get_result_text()
def dismiss_alert():
    alert = browser.switch_to.alert
    print(alert.text)
    alert.dismiss()
    get_result_text()
def send_prompt_in_alert():
    alert = browser.switch_to.alert
    print(alert.text)
    alert.send_keys("Test")


open_page()
click_on_js_alert_button()
accept_alert()

click_on_js_confirm_button()
dismiss_alert()

click_on_js_confirm_button()
accept_alert()

click_on_prompt_button()
send_prompt_in_alert()
dismiss_alert()

click_on_prompt_button()
send_prompt_in_alert()
accept_alert()

browser.quit()