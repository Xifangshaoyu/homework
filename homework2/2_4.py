x2 = 2
x1 = 1
x0 = (x1 + x2)/2
value = x0*x0
value_diffirence = abs(value - 2)
while value_diffirence > 0.0000001:
    if value > 2:
        x2 = x0
    else:
        x1 = x0
    x0 = (x1 + x2) / 2
    value = x0 * x0
    value_diffirence = abs(value - 2)
print("%.6f"%x0)