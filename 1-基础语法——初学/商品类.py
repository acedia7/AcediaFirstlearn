# 设计⼀个商品类，它具有的私有数据成员是商品序号、商品名、单价、总数量和剩余数量。
# 具有的 公有成员函数是：初始化商品信息的构造函数__init__，
# 显示商品信息的函数display，计算已售出 商品价值income，修改商品信息的函数setdata

class items:
    def __init__(self,num,name,price,sum,lsum):
        self.__num=num
        self.__name=name
        self.__price=price
        self.__sum=sum
        self.__lsum=lsum

    def display(self):
        income=self.__price*(self.__sum-self.__lsum)
        return income

    def setdata(self,renum,rename,reprice,resum,relsum):
        self.__num = renum
        self.__name = rename
        self.__price = reprice
        self.__sum = resum
        self.__lsum = relsum
