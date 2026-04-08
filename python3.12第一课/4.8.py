#结合循环语句增加猜数字次数，让自己猜中数字
import random

x = random.randint(0, 100)  #随机生成0~100的数
print(x)
while True:  #一直循环
    y = int(input("请输入数字："))
    if x < y:
        print("大了")
    elif x > y:
        print("小了")
    else:  # y==x
        print("猜对了！")
        break  #结束循环

#问题：使用for循环输出所有3位整数中的素数
#问题拆解：1，循环输出三位整数；2，如何判断一个数是素数
#素数；这个数只能被1和自己整除（%）
for i in range(100,1000):
    print(i)

#输入一个数，判断是不是素数
x=int(input("请输入一个数字:"))
for i in range(2,x):#循环2~x-1
    if x%i==0:
        print("不是素数")
        break
    elif i ==x-1:
        print("素数")
    else:
        pass

for x in range(100,1000):
    flag = True
    for i in range(2, x):
        if x % i == 0:
            flag = False
            break
    if flag:
        print(x)

