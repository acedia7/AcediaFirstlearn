import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

driver = webdriver.Chrome()
driver.maximize_window()

c=[]
n=[]
with open('data.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    for i in reader:
        print(i)
        driver.get(i['详情链接'])
        time.sleep(0.2)
        try:
            driver.find_elements(By.XPATH, "/html/body/div/div[2]/div[2]/form/div/div[1]/div/ul/li[1]/a")[0].click()
            count=driver.find_elements(By.XPATH,'/html/body/div/div[2]/div[2]/form/div/div[1]/div/ul/li[1]/span')
            c.append(count[0].text)
            name=driver.find_elements(By.XPATH,'/html/body/div/div[2]/div[2]/form/div/div[1]/div/ul/li[1]/a')
            n.append(name[0].text)
            time.sleep(2)
        except IndexError:
            pass

file="data.csv"
data = pd.read_csv(file, encoding='utf-8')
new_file = 'data_new.csv'
lenth=len(c)
for i in range(0,lenth):
    data['下载次数'] = data['下载次数'].mask(data['附件名'] == n[i], c[i])
data.to_csv(new_file, index=False)