from selenium import webdriver
import time

driver = webdriver.Chrome()
url = 'https://mail.163.com/'
driver.get(url)
#  //*[contains(@id,'x-URS-iframe')]
#  //*[@id='scoreIndexPopIfm']

# iframe = driver.find_element_by_xpath('//*[@id="loginDiv"]/iframe')
iframe = driver.find_element_by_xpath("//*[contains(@id,'x-URS-iframe')]")

driver.switch_to.frame(iframe)
print(iframe)
driver.find_element_by_name('email').send_keys('hansononlyone')
driver.find_element_by_name('password').send_keys('wangyi852963')
driver.find_element_by_id('dologin').click()