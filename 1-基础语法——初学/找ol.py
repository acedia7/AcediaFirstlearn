str=input()
flag=str.find("ol")
if(flag==-1):
    print("该字符串不存在ol子字符串")
else:
    str1=str.replace("ol","fzu")
    print(str1[::-1])