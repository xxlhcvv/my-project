while True:
    age = input("请输入你家狗狗的年龄：")
    if age.isdecimal():  #isdecimal十进制
        age = int(age)
        if age <= 0:
            print("你在逗我吧!")
        elif age == 1:
            print("相当于14岁的人。")
        else:  #否则如果
            human = 22 + (age -2)*5
            print("相当于人类的年龄:", human)
    elif age.upper()=='Q':  #.upper可以把输入的字母变为大写，==比较运算符
        print("计算结束！")
        break  #立刻跳出并结束当前的循环
    else:
        print("请输入数字，按Q键退出！")