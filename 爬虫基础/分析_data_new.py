import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt

path=r'./data_new.csv'
chunker = pd.read_csv(path,iterator= True)
loop = True
chunksize = 10000
chunks = []
while loop:
    try:
        chunk = chunker.get_chunk(chunksize)[['date','部门','详情链接','标题','下载链接','附件名','下载次数']]
        chunks.append(chunk)
    except StopIteration:
        loop = False
        print('以读取完毕')
#把上面的块合并
action = pd.concat(chunks,ignore_index=True)
# print(action.info())
