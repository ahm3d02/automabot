from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.firefox.options import Options
import os
import time

chrome_options = webdriver.ChromeOptions()
# options = Options()
# profile = webdriver.FirefoxProfile()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
# driver = webdriver.Firefox(firefox_profile = profile, options = options)

driver.get("https://www.google.com/")
time.sleep(5)
driver.quit()