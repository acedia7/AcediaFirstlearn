from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
import csv


def save(lst):
    head = ('日期', "年份", '内容', '标题', '事件')
    with open("calender.csv", 'w', encoding='utf-8-sig', newline='') as file:
        # 1. 通过csv创建写入对象,写入文件对象,并且写入表头
        dic_writer = csv.DictWriter(file, fieldnames=head)

        # 3. 写入表头
        dic_writer.writeheader()

        # 2. 写入数据data，writerow，写⼊⼀⾏，writerows可以写⼊多⾏
        dic_writer.writerows(lst)


driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://baike.baidu.com/calendar/')
time.sleep(1)

now_month = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div[1]/div/div/div")
print(now_month.text[5:-1])
now_month1 = int(now_month.text[5:-1]) - 1
for i in range(0, now_month1):
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div[1]/div/div/a[1]/em").click()
    time.sleep(0.5)
# print("ok")
lists = []

for j in range(1, 13):
    li = []
    count = 0
    if j == 1 or j == 7 or j == 10:
        for l in range(1, 43):
            try:
                date = driver.find_elements(By.XPATH, f"/html/body/div[2]/div/div[1]/div[1]/div/ul[2]/li[{l}]/div[2]")
                date1 = date[0].text
                # print(date1)
                li.append(l)

            except IndexError:
                # print("error")
                pass
    else:
        date = driver.find_elements(By.XPATH, ".//div[@id='calendar']/ul[@class='days']/li")
        for k in date:
            try:
                count += 1
                date = k.find_element(By.XPATH, "./div[2]")
                date1 = date.text
                # print(date1)
                li.append(count)

            except NoSuchElementException:
                # print("error")
                pass

    # print(li)
    dic = {}
    for i in li:
        date2 = driver.find_element(By.XPATH, f"/html/body/div[2]/div/div[1]/div[1]/div/ul[2]/li[{i}]/div[2]")
        action = ActionChains(driver)
        action.move_to_element(date2)
        action.click()
        action.perform()
        time.sleep(0.5)
        day = driver.find_element(By.XPATH, f"/html/body/div[2]/div/div[2]/div/div/div/span")
        day1 = day.text
        dds = driver.find_elements(By.XPATH, f"/html/body/div[2]/div/div[2]/div/div/dl/dd")
        # print(len(dds))
        for dd in dds:
            dic["日期"] = day1
            year = dd.find_element(By.XPATH, f"./div[1]")
            year1 = year.text
            dic["年份"] = year1
            e = dd.find_element(By.XPATH, f"./div[3]/div[1]/div")
            e1 = e.text
            # print(e1)
            dic["内容"] = e1
            if e1[-2:-1] == "出生":
                dic["事件"] = "birth"
            elif e1[-2:-1] == "逝世":
                dic["事件"] = "death"
            else:
                dic["事件"] = "event"
            dic1=dic.copy()
            lists.append(dic1)
            print(dic)
            time.sleep(0.3)
            print(lists)
    if j == 12:
        break
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div[1]/div/div/a[2]/em").click()
    time.sleep(0.5)
print(lists)
save(lists)
