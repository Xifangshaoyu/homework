x,y,z,w = 0,0,0,0
x = int(input("输入第一个数字"))
y = int(input("输入第二个数字"))
z = int(input("输入第三个数字"))
if x > y:
    w = y
    y = x
    x = w
if y > z:
    w = z
    z = y
    y = w
if x > z:
    w = x
    x = y
    y = w
print(x,y,z)