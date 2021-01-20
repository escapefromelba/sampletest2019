from selenium import webdriver
from chromedriver_py import binary_path
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome(executable_path=binary_path)

browser.get("https://www.amazon.com/")
browser.maximize_window()
browser.find_element_by_id("nav-link-accountList").click()
browser.find_element_by_name("email").send_keys("username" + Keys.ENTER)
browser.find_element_by_name("password").send_keys("password" + Keys.ENTER)

# browser.switch_to_window('https://www.amazon.com/gp/help/customer/display.html?nodeId=508510&ref_=nav_cs_help')
# assert "Jacob - Google Search" == browser.title
# second commit
