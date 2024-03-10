from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os
import wget

driver = webdriver.Chrome()
driver.get("https://www.pinterest.com/")

login_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="mweb-unauth-container"]/div/div/div[1]/div/div[2]/div[2]/button/div/div'))
)
login_button.click()
time.sleep(3)

username = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "id"))
)
password = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "password"))
)
login = driver.find_element(By.XPATH, '//*[@id="__PWS_ROOT__"]/div/div[1]/div[2]/div/div/div/div/div/div[4]/form/div[7]/button/div')

username.clear()
password.clear()
username.send_keys('你的帳號')
password.send_keys('你的密碼')
login.click()

search = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="searchBoxContainer"]/div/div/div[2]/input'))
)
keyword = "關鍵字"
search.send_keys(keyword)
search.send_keys(Keys.RETURN) 

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "hCL.kVc.L4E.MIw"))
)

count = 1
path = os.path.join(keyword)
os.mkdir(path) 
 
for i in range(5):  
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") 
    time.sleep(5)  
    
    imgs = driver.find_elements(By.CLASS_NAME, "hCL.kVc.L4E.MIw")
    
    for img in imgs:
        save_as = os.path.join(path, keyword + str(count) + '.jpg') 
        wget.download(img.get_attribute("src"), save_as) 
        count += 1