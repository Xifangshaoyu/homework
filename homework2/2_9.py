import  random
import  math

sum = 0
for i in range(1,10000):
    a = random.uniform(2,3)
    sum += a * (a + 4 * math.sin(a))
sum = sum/10000
print(sum)