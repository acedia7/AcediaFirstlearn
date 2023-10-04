#创建一个函数，这个函数可以统计一个只有数字的列表中所有数字的个数，通过字典方式返回
def solution(lst):
    dic={}
    for i in lst:
        if i in dic:
            dic[i]=dic[i]+1
        else:
            dic[i]=1
    return dic

list=[1,1,2,3,44,4,5,6,4]
print(solution(list))