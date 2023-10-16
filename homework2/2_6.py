A = float(input("\n请输入一个数:"))
if A == 0:
    print("\n平方根为:0")
else:
    x0 = A/2
    while abs(x0**2 - A) > 0.0000001:
        x0 = 1/2 * x0 + A/(2 * x0 ** 1)
    print("\n平方根为:","%.6f"%x0)