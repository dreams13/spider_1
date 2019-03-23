from selenium import webdriver
import time

url = "https://www.douban.com/"
driver = webdriver.Chrome()
driver.get(url)
iframe = driver.find_element_by_xpath("//*[@class='login']/iframe")
driver.switch_to.frame(iframe)
btn = driver.find_element_by_xpath("//html/body/div[1]/div[1]/ul[1]/li[2]").click()
username = driver.find_element_by_xpath('//*[@id="username"]')
username.send_keys('13021113571')
password = driver.find_element_by_xpath('//*[@id="password"]')
password.send_keys('douban852963')
login_btn = driver.find_element_by_xpath("//*[@class='btn btn-account btn-active']")
login_btn.click()

