arr_raw = input("")
arr = [int(n) for n in arr_raw.split()]
print("\n初始:",arr)

length = len(arr)
for i in range(length-1,-1,-1):
    print(arr[i],end=' ')

print()

j = length - 1
while j >= 0:
    print(arr[j],end=' ')
    j -= 1