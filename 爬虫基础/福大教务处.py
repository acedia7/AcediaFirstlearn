import requests
from lxml import etree
from lxml import html
import re
import time
from html.parser import HTMLParser
from lxml.html import fromstring, tostring
import csv

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
}


def get(url):
    res = requests.get(url=url, headers=header)
    res.encoding = 'utf-8'
    tree = etree.HTML(res.text)

    uls = tree.xpath("//div[@class='box-gl clearfix']/ul[@class='list-gl']")
    uls1 = html.tostring(uls[0], encoding='utf-8').decode('utf-8')
    # print(uls1)
    for ul in uls:
        lis = ul.xpath(".//li")
        for li in lis:
            dic = {}
            try:
                date = li.xpath("./span[@class='doclist_time']/font/text()")[0]
            except IndexError:
                date = li.xpath("./span[@class='doclist_time']/text()")[0]
                # print(date)
            dic["date"] = date.strip()
            bumen = li.xpath("./text()")[1]
            # print(bumen)
            dic["部门"] = bumen.strip()
            a = li.xpath("./a/@href")[0]
            new_url = "https://jwch.fzu.edu.cn/" + a.replace("../", "")
            dic["详情链接"] = new_url.strip()
            # print(a)
            # print(new_url)
            title = li.xpath("./a/@title")[0]
            # print(title)
            dic["标题"] = title.strip()
            res1 = requests.get(url=new_url, headers=header)
            res1.encoding = 'utf-8'
            tree1 = etree.HTML(res1.text)
            # tree2 = html.tostring(tree1[0], encoding='utf-8').decode('utf-8')
            # print(tree2)
            uls1 = tree1.xpath("//ul[@style='list-style-type:none;']")
            for ul1 in uls1:
                lis1 = ul1.xpath("./li")
                for li1 in lis1:
                    href = "https://jwch.fzu.edu.cn/" + li1.xpath("./a/@href")[0]
                    # print(href)
                    dic["下载链接"] = href
                    # name = li1.xpath("./a/text()")[0]
                    # print(name)
                    dic["附件名"] = ''
                    dic["下载次数"] = ""

            time.sleep(0.05)
            lst.append(dic)


def save(lst):
    head = ('date', "部门", '详情链接', '标题', '下载链接', '附件名', "下载次数")
    with open("data.csv", 'w', encoding='utf-8-sig', newline='') as file:
        # 1. 通过csv创建写入对象,写入文件对象,并且写入表头
        dic_writer = csv.DictWriter(file, fieldnames=head)

        # 3. 写入表头
        dic_writer.writeheader()

        # 2. 写入数据data，writerow，写⼊⼀⾏，writerows可以写⼊多⾏
        dic_writer.writerows(lst)


lst = []
for page in range(184, 179, -1):
    if (page == 184):
        url = "https://jwch.fzu.edu.cn/jxtz.htm"
        get(url)
    else:
        url = f"https://jwch.fzu.edu.cn/jxtz/{page}.htm"
        get(url)
print(lst)
save(lst)
