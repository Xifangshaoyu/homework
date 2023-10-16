import math
pai = math.pi
print(pai)

i = 1
value1 = 0
while abs(value1 - pai) > 0.0000000001:
    value1 += 4/i
    i = -i
    if i > 0:
        i = i + 2
    else:
        i = i - 2
print(value1)

i = 2
value2 = 2
while abs(value2 - pai) > 0.00000000001:
    value2 *= i*i/(i*i - 1)
    i += 2
print(value2)

i = 0
value3 = 0
while abs(value3 - pai) > 0.00000000001:
    value3 += (1/16**i)*(4 / (8*i + 1) - 2 / (8 * i +4) -1 / (8 * i + 5) - 1 / (8 * i +6))
print(value3)