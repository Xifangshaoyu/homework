A = float(input("\n请输入一个数:"))
if A == 0:
    print("\n立方根为:0")
else:
    x0 = A/3
    while abs(x0**3 - A) > 0.0000001:
        x0 = 2/3 * x0 + A/(3 * x0 ** 2)
    print("\n立方根为:","%.6f"%x0)