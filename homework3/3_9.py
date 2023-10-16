arr1_raw = input("")
arr1 = [int(n) for n in arr1_raw.split()]
arr1_len = len(arr1)

arr2 = []
for i in range(0,arr1_len,1):
    result = 1
    for j in range(0,arr1_len,1):
        if j == i:
            continue
        result *= arr1[j]
    arr2.append(result)
print("\n原数组为:",arr1)
print("结果为：",arr2)