# 用所学的知识写一个斗地主随机发牌程序，
# 将每个人的发牌以及多的三张牌的结果分别按照从大到小的顺序输出到
# player1.txt，player2.txt，player3.txt，others.txt四个文件中

from random import shuffle
F = ('♠', '♥', '♣', '♦')
V = tuple(str(i) for i in range(2,11))+('J','Q','K','A')
P = [f+v for f in F for v in V] + ['joker','JOKER']
print(P)
shuffle(P)
list1=P[0:17]
list2=P[17:34]
list3=P[34:51]
list4=P[51:55]
table = {str(x): x for x in range(3, 11)}
table.update({'J': 11, 'Q': 12, 'K': 13, 'A': 14, '2': 15, 'oker': 16, 'OKER': 17})
list1=sorted(list1,key=lambda item: table[item[1:]],reverse=True)
list2=sorted(list2,key=lambda item: table[item[1:]],reverse=True)
list3=sorted(list3,key=lambda item: table[item[1:]],reverse=True)
list4=sorted(list4,key=lambda item: table[item[1:]],reverse=True)

with open("player1.txt","w",encoding="utf-8") as f1:
    for i in list1:
        f1.write(i)
        f1.write("  ")
    f1.close()

with open("player2.txt","w",encoding="utf-8") as f2:
    for i in list2:
        f2.write(i)
        f2.write("  ")
    f2.close()

with open("player3.txt","w",encoding="utf-8") as f3:
    for i in list1:
        f3.write(i)
        f3.write("  ")
    f3.close()

with open("others.txt","w",encoding="utf-8") as f4:
    for i in list4:
        f4.write(i)
        f4.write("  ")
    f4.close()