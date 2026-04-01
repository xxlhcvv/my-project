#选择结构语句if
score = 91
if score >= 90 and score <= 100:
    print("该成绩等级为A！")  #拥有相同的缩进属于if的代码块
    print("成绩为:", score)
print("该成绩等级为B！")

# if...elif...else多路分支语句
# 数字猜大小
import random
x = random.randint(0, 100)  #随机生成0~100的数
print(x)
y = int(input("请输入数字："))
if x < y:
    print("大了")
elif x > y:
    print("小了")
else:  #y==x
    print("猜对了！")

#【任务4-1】实现考试成绩等级划分
score = float(input("请输入成绩："))
if score < 0 or score > 100:
    print("成绩无效")
elif score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("E")

