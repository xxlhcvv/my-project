score = int(input("请输入学生成绩:"))
if score >= 90:
    print("等级为A")
elif 80 <= score < 90:
    print("成绩等级为B")
elif 70 <= score < 80:
    print("成绩等级为C")
elif 60 <= score < 70:
    print("成绩等级为D")
else:
    print("成绩等级为E")
