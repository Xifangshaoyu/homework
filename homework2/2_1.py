n = int(input("请输入一个n:"))
arr = []
if n == 1:
    arr.append(1)
elif n % 3 == 0:
    for i in range(0,n // 3,1):
        arr.append(3)
elif n % 3 == 1:
    for i in range(0,n // 3 - 1,1):
        arr.append(3)
    arr.append(2)
    arr.append(2)
elif n % 3 == 2:
    for i in range(0,n // 3,1):
        arr.append(3)
    arr.append(2)
print("\n结果为:",arr)
