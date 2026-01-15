from selenium import webdriver

browser = webdriver.Firefox()
# browser.get("https://the-internet.herokuapp.com/windows")
# title = browser.title
# print(title)
browser.get("https://google.com")
current_url = browser.current_url
print(current_url)
browser.quit()
