arr = input("")
k = None
result = "\n不存在连续字符"
for i in arr:
    if i == k:
        result = "\n存在连续字符"
        break
    k = i
print(result)