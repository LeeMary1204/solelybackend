#!/usr/bin/python3

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import sys
import datetime
import getData

def handleDB(objList=[]):
  #
  myClient = getData.client
  print("connect successfully")
  myDB = myClient['solelywebsite']
  print("connect successfully1")
  table = myDB['jobs']
  print("connect successfully2")
  print(objList)
  print("connect successfully4")
  for obj in objList:
    table.insert_one(obj)

  print("connect successfully5")
   

objList = []

def fun(role,jobType):
  # liList = web.find_elements(By.CSS_SELECTOR,'html.theme.theme--mercado.artdeco.windows body.render-mode-BIGPIPE.nav-v2.ember-application.boot-complete.icons-loaded div.application-outlet div.authentication-outlet div.scaffold-layout.scaffold-layout--breakpoint-xl.scaffold-layout--list-detail.scaffold-layout--reflow.scaffold-layout--has-list-detail.jobs-search-two-pane__layout div.scaffold-layout__inner.scaffold-layout-container.scaffold-layout-container--reflow div.scaffold-layout__row.scaffold-layout__content.scaffold-layout__content--list-detail main#main.scaffold-layout__main.scaffold-layout__list-detail div.scaffold-layout__list-detail-inner div.scaffold-layout__list div.jobs-search-results-list ul.scaffold-layout__list-container>li')
  liList = web.find_elements(By.CSS_SELECTOR,'html body div.base-serp-page div.base-serp-page__content main#main-content.two-pane-serp-page__results section.two-pane-serp-page__results-list ul.jobs-search__results-list>li')
  
  count = 0
  
  for li in liList:
    if count > 1:
      return
 
    # link = li.find_element(By.CSS_SELECTOR,'.artdeco-entity-lockup__subtitle.ember-view').click()
    link = li.find_element(By.XPATH,'./div').click()
    job = li.find_element(By.XPATH,'./div/div[2]/h3').text
    # job = li.find_element(By.CSS_SELECTOR,'.disabled.ember-view.job-card-container__link.job-card-list__title').text
       
    # company = li.find_element(By.CSS_SELECTOR,'.artdeco-entity-lockup__subtitle.ember-view span.job-card-container__primary-description').text
    company = li.find_element(By.XPATH,'./div/div[2]/h4/a').text

    # descriptionURL = web.find_element(By.CSS_SELECTOR,'html.theme.theme--mercado.artdeco.windows body.render-mode-BIGPIPE.nav-v2.ember-application.boot-complete.icons-loaded div.application-outlet div.authentication-outlet div.scaffold-layout.scaffold-layout--breakpoint-xl.scaffold-layout--list-detail.scaffold-layout--reflow.scaffold-layout--has-list-detail.jobs-search-two-pane__layout div.scaffold-layout__inner.scaffold-layout-container.scaffold-layout-container--reflow div.scaffold-layout__row.scaffold-layout__content.scaffold-layout__content--list-detail main#main.scaffold-layout__main.scaffold-layout__list-detail div.scaffold-layout__list-detail-inner div.scaffold-layout__detail.overflow-x-hidden.jobs-search__job-details div.jobs-search__job-details--wrapper div.jobs-search__job-details--container div.job-view-layout.jobs-details div div.jobs-details__main-content.jobs-details__main-content--single-pane.full-width div div.jobs-unified-top-card.t-14 div.relative.job-details-jobs-unified-top-card__container--two-pane div.job-details-jobs-unified-top-card__content--two-pane div.display-flex.justify-space-between.flex-wrap .ember-view').get_attribute('href')
    descriptionURL = web.find_element(By.XPATH,'/html/body/div[1]/div/section/div[2]/section/div/div[1]/div/a').get_attribute('href')
    time.sleep(1)
    
    count = count + 1
    
    now = datetime.datetime.now()
    date = now.strftime('%Y-%m-%d')

    obj = { 'job':job,'company':company,'descriptionURL':descriptionURL,'date':date,'role':role,'jobType':jobType}
    
    objList.append(obj)


if __name__ == '__main__':

  role = sys.argv[1]
  jobType = sys.argv[2]
  print('exec python start') 
  

  web = webdriver.Firefox()

  # web.get('https://www.linkedin.com/?trk=seo-authwall-base_nav-header-logo')
  # time.sleep(5)

  # web.find_element(By.XPATH,'//*[@id="session_key"]').send_keys('nasheezilvist@outlook.com')
  # web.find_element(By.XPATH,'//*[@id="session_password"]').send_keys('dftKAhmg6M')
  # web.find_element(By.XPATH,'/html/body/main/section[1]/div/div/form/div[2]/button').click()
  # time.sleep(5)

  web.get('https://www.linkedin.com/jobs/search/?currentJobId=3748246488')
  time.sleep(3)
  
  #role
  # web.find_element(By.CSS_SELECTOR,'.jobs-search-box__text-input.jobs-search-box__keyboard-text-input').send_keys(role)
  # web.find_element(By.CSS_SELECTOR,'html.theme.theme--mercado.artdeco.windows body.render-mode-BIGPIPE.nav-v2.ember-application.boot-complete.icons-loaded div.application-outlet header#global-nav.global-nav.global-alert-offset-top.global-nav--hide-text.global-nav--visible div.global-nav__content div#global-nav-search.global-nav__search.global-nav__search--jobs div div.jobs-search-box__container.jobs-search-box button.jobs-search-box__submit-button.artdeco-button.artdeco-button--2.artdeco-button--secondary').click()

  web.find_element(By.ID,'job-search-bar-keywords').send_keys(role)
  web.find_element(By.XPATH,'/html/body/div[1]/header/nav/section/section[2]/form/button').click()

  time.sleep(3)
  web.find_element(By.XPATH,'/html/body/div[1]/section/div/div/div/form/ul/li[6]/div/div/button').click()
  # web.find_element(By.CSS_SELECTOR,'.artdeco-pill.artdeco-pill--slate.artdeco-pill--choice.artdeco-pill--2.search-reusables__filter-pill-button.search-reusables__all-filters-pill-button').click()
  time.sleep(1)
  # web.find_element(By.XPATH,'/html/body/div[3]/div/div/div[2]/ul/li[2]/fieldset/div/ul/li[1]/label').click()
  # internship

  if jobType == 'internship':
    web.find_element(By.ID,'f_E-0').click()
    # web.find_element(By.XPATH,'/html/body/div[3]/div/div/div[2]/ul/li[4]/fieldset/div/ul/li[1]/label').click()
    time.sleep(1)# entry level
  elif jobType == 'entry level':
    web.find_element(By.ID,'f_E-1').click()
    # web.find_element(By.XPATH,'/html/body/div[3]/div/div/div[2]/ul/li[4]/fieldset/div/ul/li[2]/label').click()
    time.sleep(1)# mid-senior level
  else:
    web.find_element(By.ID,'f_E-3').click()
    # web.find_element(By.XPATH,'/html/body/div[3]/div/div/div[2]/ul/li[4]/fieldset/div/ul/li[4]/label').click()
    time.sleep(1)
  
  # web.find_element(By.CSS_SELECTOR,'.reusable-search-filters-buttons.search-reusables__secondary-filters-show-results-button.artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view').click()
  web.find_element(By.XPATH,'/html/body/div[1]/section/div/div/div/form/ul/li[6]/div/div/div/button').click()
  time.sleep(3)

   
  fun(role,jobType)
  
  handleDB(objList)

  print('exec python end') 
  # js = "var q = document.querySelector('.jobs-search-results-list').scrollHeight"
  # height = searchList.execute_script(js)

  # searchList.execute_script('window.scrollTo(0,document.body.scrollHeight)')
  # time.sleep(5)
  
  # t1 = int(time.time())
  # status = True
  # num = 0

  # while status:
  #   t2 = int(time.time())
  #   if t2 - t1 < 30:
  #     new_height = web.execute_script(js)
  #     if new_height > height:
  #       time.sleep(1)
  #       web.execute_script('window.scrollTo(0,document.body.scrollHeight)')
  #       height = new_height
  #       t1 = int(time.time())
  #     elif num < 3:
  #       time.sleep(3)
  #       num = num + 1
  #     else:
  #       status = False
  #       web.execute_script('window.scrollTo(0,0)')
  #       break
  

  print('____________')  
  
  web.quit()
  time.sleep(5)