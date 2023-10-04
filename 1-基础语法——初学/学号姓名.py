#创建一个字典（dict），
#为字典添加几个键为学号，值为姓名元素，删除学号尾号为偶数的元素，输出字典
dic1={}
lst1=[]
while(1):
    x=input("输入学号姓名，空格分隔，输入0结束")
    if(x=='0'):
        break
    lst=x.split()
    number=int(lst[0])
    name=lst[1]
    dic1[number]=name
for i in dic1.keys():
    if i%2==0:
        lst1.append(i)
for i in lst1:
    dic1.pop(i)
print(dic1)

