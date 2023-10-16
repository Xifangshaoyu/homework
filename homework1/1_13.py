def f(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1,n+1,1):
        result *= i
    return result

n = int(input("请输入一个自然数:"))
result = f(n)
print("\n阶乘为:",result)