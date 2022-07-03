'''python中唯一的三元操作符'''
import random



'''x = 4
y = 5
small = x if x < y else y
print(small)'''

'''assert断言（提前自爆,异常总比false好）'''
'''assert 3>4'''

'''favourite = 'fishC'
for i in favourite:
    print(i,end=' ')'''
'''end是print的参数，可取消print添加的换行符'''

'''range([start,],stop,[,step=1])'''
# '''的换行打印
# print('''This is the first line
# This is the second line''')


# 格式化方法

# age = 15
# place = 'india'
# print('''my age is {0}
# my place is {1}'''.format(age,place))


# 添加方法
'''
a=[1,2,3,4]
a.append([2,3])
print(a)
a.append([6,8,9])      #append只能添加一个变量
print(a)
a.extend('hello')
print(a)               #extend也只能添加一个变量且hello是分开添加的

#插入方法
a.insert(3,100)
print(a)
#删除方法
del a[1]
print(a)
x1 = a.pop(2)
print(x1)
a.remove(1)      #remove用来删掉括号里面的值（所遇到的第一个值）
a.clear()        #清空a里面所有的元素，使之变成一个空列表


#判断语句（in)
9 in a           #只能判断第一层列表是否有9
9 in a[x]         #用来判断a里面的列表是否有9

#切片

a[1:3]         #注：前闭后开
'''
'''
num = int(input())
list=[num]
while num!=1:
    if num%2==1:
        num=num*3+1
        list.append(num)
    else:
        num=num//2
        list.append(num)
print(list)
'''

'''
#********** End **********#
s = input()

# 请在下面的 Begin-End 之间写出实现的代码
########## Begin ##########
s=s.split()
maxlen=max(len(word) for word in s)
c=[word for word in s if len(word)==maxlen]

print(f"输入句子中最长的单词是{c[0]}，长度是{maxlen}")


'''
########## End ###########
'''
s= input("Enter a string\n")

for x in s.upper():
    if(x==' '):
        print(' ',end='')
    elif(ord(x)-ord('A')+3 >= 26 ):
        print(chr(ord(x)-26+3).lower(), end='')
    else:
        print (chr(ord(x)+3).lower(), end='')
'''
'''
#liebiao-1
zifu_low=[]
zifu='0123456789_'
for i in range(ord('a'),ord('z')+1):
    zifu_low.append(chr(i))
zifu_up=list(map(lambda x:x.upper(),zifu_low))
zifu=list(zifu)+zifu_low+zifu_up
#print(zifu)
#tianzige-2
n=int(input("please input the times:"))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or i==n//2:
            print(random.choice(zifu),end='')
            if j==n-1:
                print('\n')
        elif j==0 or j==n//2:
            print(random.choice(zifu),end='')
        elif j==n-1:
            print(random.choice(zifu),end='\n')
        else:
            print(' ',end='')
'''
'''
num = int(input())


# 请在下面的 Begin-End 之间编写正确的代码
########## Begin ##########
def add(num):
    sum=0
    for i in range(1,num+1):
        sum = sum + i
    return sum
print(add(num))

########## End ##########
'''
'''
dd = eval(input())
# 请在下面的 Begin-End 之间编写正确的代码
########## Begin ##########
def change(dd):
    dd_new = {value:key for key,value in dd.items()}
    return dd_new
print(change(dd))
'''
'''
s = input()
# 请在下面的 Begin-End 之间编写正确的代码
########## Begin ##########
list1=[]
def f(s):
    for i in s:
        if i.isalpha():
            list1.append(i)
    return str(list1)
print(f(s))




########## End ##########




########## End ##########
'''
'''
l1 = eval(input())
l2 = eval(input())
# 请在下面的 Begin-End 之间编写正确的代码
########## Begin ##########
list1 = []
for i in len(l1):
    list.append(lambda x:max(l1[i],l2[i]))
print(list1)

########## End ########
'''
'''
a=10
b=20
c=30
g={'a':6,'b':8}
t={'b':100,'c':10}
print(eval('a+b+c',g,t))
'''
'''
n = input()
num = input()
p = input()
#------将类的定义写在下方--------
class Book:
    def __init__(self,n,num,p):
        self.n = n
        self.num = num
        self.p = p
    def __del__(self):
        print("Book destroyed-"+f"{n},{num},{p}")


#------------end----------------
b = Book(n, num, p)
del b'''

from math import sqrt
a1 = int(input())
b1 = int(input())
c1 = int(input())

#------将类的定义写在下方--------
class Equation:
    def __init__(self,a,b,c):
        self.a1 = a
        self.b1 = b
        self.c1 = c
    def getDiscriminant(self):
        return b1**2-4*a1*c1
    def getRoot1(self):
        if self.getDiscriminant(self)<0:
            return 0
        else:
            return ((-b1+math.sqrt(b1**2-4*a1*c1))/(2*a1))
    def getRoot2(self):
        if self.getDiscriminant(self)<0:
            return 0
        else:
            return ((-b1-math.sqrt(b1**2-4*a1*c1))/(2*a1))




#------------end----------------
e = Equation(a1, b1, c1)
print(e.getDiscriminant(), e.getRoot1(), e.getRoot2())
