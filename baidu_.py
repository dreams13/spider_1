import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")

time.sleep(1)
driver.find_element_by_id('kw').send_keys('python')
time.sleep(1)
driver.find_element_by_id('su').click()
time.sleep(1)

all_h = driver.window_handles
print(all_h)
h3 = driver.find_element_by_xpath('//*[@id="1"]/h3/a')
h3.click()