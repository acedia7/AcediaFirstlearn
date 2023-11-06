import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

driver = webdriver.Chrome()
driver.maximize_window()

c = []
n = []
h = []
with open('data.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    for i in reader:
        Name = []
        Count = []
        # print(i)
        driver.get(i['详情链接'])
        time.sleep(0.2)
        try:
            lis = driver.find_elements(By.XPATH, ".//ul[@style='list-style-type:none;']/li")
            for li in lis:
                # li.find_element(By.XPATH, './a').click()
                name = li.find_element(By.XPATH, './a').text
                Name.append(name)
                count = li.find_element(By.XPATH, "./span").text
                Count.append(count)
            n.append(Name)
            c.append(Count)
            h.append(i['详情链接'])
        except IndexError:
            pass
    print(n)
    print(c)
    print(h)

N = []
for i in n:
    aa = ""
    for j in i:
        if j == '':
            aa = ""
        else:
            aa += j + "\n"
    N.append(aa)

C = []
for i in c:
    bb = ""
    for j in i:
        if j == '':
            bb = ""
        else:
            bb += j + "\n"
    C.append(bb)

print(C)
print(N)

file = "data.csv"
data = pd.read_csv(file, encoding='utf-8')
new_file = 'data_new.csv'
lenth = len(c)
for i in range(0, lenth):
    data['下载次数'] = data['下载次数'].mask(data['详情链接'] == h[i], C[i])
    data['附件名'] = data['附件名'].mask(data['详情链接'] == h[i], N[i])
data.to_csv(new_file, index=False)
