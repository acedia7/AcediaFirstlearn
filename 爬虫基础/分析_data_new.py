import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import colors

path = r'./data_new.csv'
chunker = pd.read_csv(path, iterator=True)
loop = True
chunksize = 10000
chunks = []
while loop:
    try:
        chunk = chunker.get_chunk(chunksize)[['date', '部门', '详情链接', '标题', '下载链接', '附件名', '下载次数']]
        chunks.append(chunk)
    except StopIteration:
        loop = False
        # print('以读取完毕')
# 把上面的块合并
action = pd.concat(chunks, ignore_index=True)
# print(action.info())

action['date'] = pd.to_datetime(action['date'])
# action.info()

# print(action)

df1 = action.fillna(value=0)
# print(df1)

df1=df1.drop(['下载次数'], axis=1).join(df1['下载次数'].str.split('\n', expand=True).stack().reset_index(level=1, drop=True).rename('下载次数'))
df=df1[["部门","下载次数"]]
df=df.dropna()
# print(df)

df["下载次数"]=df["下载次数"].astype(int)
# print(df)

pd.set_option('display.unicode.east_asian_width',True)

df_fa=df["部门"].value_counts()
df_sum=df.groupby(['部门'])['下载次数'].apply(lambda x:x.sum())
df_fa=df_fa.to_frame()
df_sum=df_sum.to_frame()
# print(df_fa)
# print(df_sum)
df_1=pd.merge(df_fa,df_sum,on="部门")
# print(df_1)
df_1["mean"]=round((df_1["下载次数"]*1.0)/(1.0*df_1["count"]),2)
print(df_1)
plt.rcParams["font.family"]="SimHei"

plt.figure(figsize=(6,3),dpi=100)
plt.bar(df_1.index,df_1["mean"],color="b",alpha=0.5)

for x,y in enumerate(df_1["mean"]):
    plt.text(x,y+30,"%s"%y,ha="center")
plt.show()

plt.bar(df_1.index,df_1["下载次数"],color="r",alpha=0.5)
for x,y in enumerate(df_1["下载次数"]):
    plt.text(x,y+50,"%s"%y,ha="center")
plt.show()

plt.bar(df_1.index,df_1["count"],color="g",alpha=0.5)
for x,y in enumerate(df_1["count"]):
    plt.text(x,y+0.2,"%s"%y,ha="center")
plt.show()

'''
附件下载次数与通知人有关，
当通知人为实践科时，平均下载次数最高，总下载次数也最多，说明此通知人最受师生关注。
而平均下载次数最少的是质量办，总下载次数最少的是教材中心，考虑到教材中心发布的通知最少，
我们可以推测出教材中心的通知受关注度大于质量办的通知关注度。
所以我们得知最受师生关注的通知人为实践科，师生关注度最低的为质量办。
'''

ddf=df1.dropna()
print(ddf)
ddf_fa=ddf["date"].value_counts()
ddf_fa=ddf_fa.to_frame()
print(ddf_fa)

sizes=[i*30 for i in ddf_fa['count']]
colors=np.random.rand(len(ddf_fa['count']))
plt.scatter(ddf_fa.index,ddf_fa['count'],s=sizes,c=colors,alpha=0.5,cmap="viridis")
plt.title("时间——count")
plt.xlabel("时间")
plt.ylabel("count")
plt.colorbar()
plt.show()

'''
由图可知，通知密集的时间段为六月到七月，八月到九月，不难发现其密集的原因为
师生们的开学和放假以及放假前的期末考这三个时间段。
'''