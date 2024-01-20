n = int(input("请输入一个整数\n"))
m = float(n)
if n == 1:
    print("不是", end='')
m = int(m**0.5)
i = 2
while i <= m:
    if n % i == 0:
        print("不是",end = '')
        break
    i += 1
print("质数")