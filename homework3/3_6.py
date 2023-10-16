grd = 0
grd = int(input("请输入你的成绩："))
if grd < 60:
    print("不合格")
elif grd < 75:
    print("合格")
elif grd < 90:
    print("良好")
else:
    print("优秀")