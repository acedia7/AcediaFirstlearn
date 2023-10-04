"""
创建类MyZoo，实现以下功能：

具有字典anmials，动物名称作为key，动物数量作为value

实例化对象的时候，输出"My Zoo!"

创建对象的时候可以输入字典进行初始化,若无字典传入，则初始化anmials为空字典

print(myzoooo) 输出 动物名称和数量

比较两个对象是否相等时，只要动物种类一样，就判断相等：

len(myzoooo) 输出所有动物总数
"""

class MyZoo:
    def __init__(self,animals=None):
        if animals is None:
            self.animals = {}
        else:
            self.animals = animals
        print("My Zoo!")

    def __str__(self):
        return str(self.animals)

    def __eq__(self, other):
        if isinstance(other, MyZoo):
            return self.animals.keys() == other.animals.keys()
        return False

    def __len__(self):
        return sum(self.animals.values())


myzoooo1 = MyZoo({"pig":5,'dog':6})
myzoooo2 = MyZoo()
print(myzoooo1)
print(myzoooo2)

myzoooo3 = MyZoo({'pig':1})
myzoooo4 = MyZoo({'pig':5})
print(myzoooo3 == myzoooo4)
print(myzoooo1 == myzoooo4)

print(len(myzoooo1))