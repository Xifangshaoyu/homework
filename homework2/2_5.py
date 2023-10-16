x0 = float(input("\n请输入一个数:"))
while abs(x0**2 - 2) > 0.0000001:
    x0 = 0.5 * x0 + 2/(2 * x0)
print("\n根号2为:","%.6f"%x0)