from selenium import webdriver
driver=webdriver.Chrome()
url="https://www.youtube.com/"
driver.get(url)
timesleep(3)
driver.maximize_window()
driver.save_screenshot("foto.png")
driver.close()