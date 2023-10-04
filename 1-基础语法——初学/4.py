s = input("输入：(输入空格分隔，输入回车结束)")
lit1=s.split()
lst2=[]
for i in lit1:
    if(i.isdigit()):
        lst2.append(int(i))
lst2.sort(reverse=False)
print(lst2)