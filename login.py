#!/usr/bin/python3

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
 

if __name__ == '__main__':

  print('login linkedin start') 

  web = webdriver.Firefox()

  web.get('https://www.linkedin.com/?trk=seo-authwall-base_nav-header-logo')
  time.sleep(5)

  web.find_element(By.XPATH,'//*[@id="session_key"]').send_keys('nasheezilvist@outlook.com')
  web.find_element(By.XPATH,'//*[@id="session_password"]').send_keys('dftKAhmg6M')
  web.find_element(By.XPATH,'/html/body/main/section[1]/div/div/form/div[2]/button').click()
  time.sleep(5)

  print('login linkedin end') 