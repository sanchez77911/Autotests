from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(3)

driver.get("https://www.google.ru/")

sleep(1)
driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').click()

sleep(1)
driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys("калькулятор")

sleep(1)
driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys(Keys.ENTER)

sleep(1)
driver.find_element_by_xpath("//*[@id='rso']/div[1]/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[3]/td[2]/div/div").send_keys(Keys.ENTER)

sleep(1)
driver.find_element_by_xpath("//*[@id='rso']/div[1]/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[3]/td[4]/div/div").send_keys(Keys.ENTER)

sleep(1)
driver.find_element_by_xpath("//*[@id='rso']/div[1]/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[2]/td[3]/div/div").send_keys(Keys.ENTER)

sleep(1)
driver.find_element_by_xpath("//*[@id='rso']/div[1]/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[5]/td[3]/div/div").send_keys(Keys.ENTER)

sleep(1)
driver.find_element_by_xpath("//*[@id='rso']/div[1]/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[4]/td[4]/div/div").send_keys(Keys.ENTER)

sleep(1)
driver.find_element_by_xpath("//*[@id='rso']/div[1]/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[4]/td[1]/div/div").send_keys(Keys.ENTER)

sleep(1)
driver.find_element_by_xpath("//*[@id='rso']/div[1]/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[3]/td[2]/div/div").send_keys(Keys.ENTER)

sleep(1)
driver.find_element_by_xpath("//*[@id='rso']/div[1]/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[5]/td[3]/div/div").send_keys(Keys.ENTER)

sleep(1)
driver.find_element_by_xpath("//*[@id='rso']/div[1]/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[2]/td[4]/div/div").send_keys(Keys.ENTER)

sleep(1)
driver.find_element_by_xpath("//*[@id='rso']/div[1]/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[3]/td[3]/div/div").send_keys(Keys.ENTER)

sleep(1)
driver.find_element_by_xpath("//*[@id='rso']/div[1]/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[5]/td[3]/div/div").send_keys(Keys.ENTER)

sleep(5)
driver.close()
