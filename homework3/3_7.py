a = int(input("\n请输入第一个正整数"))
b = int(input("\n请输入第二个正整数"))

if a < b:
    a,b = b,a
while b != 0:
    a = a%b
    a, b = b, a
print("\n最大公约数为:",a)