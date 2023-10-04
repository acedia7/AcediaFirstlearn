x=eval(input())
y=eval(input())
z=eval(input())
list1=[]
list1.append(x)
list1.append(y)
list1.append(z)
list1.sort(reverse=True)
for i in list1:
    print(i)