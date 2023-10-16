arr = []
arr.append(int(input("请输入第一个数")))
arr.append(int(input("请输入第二个数")))
arr.append(int(input("请输入第三个数")))
arr.append(int(input("请输入第四个数")))
i = 0
while i < 4:
    j = i
    while j < 3:
        if arr[j] < arr[j + 1]:
            arr[j],arr[j + 1] = arr[j +1],arr[j]
        j = j + 1
    i = i + 1
print(arr)