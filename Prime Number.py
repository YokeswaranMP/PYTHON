list = []
n = int(input())
for i in range(2, n+1):
    for j in range(2, n+1):
        m = i * j
        list.append(m)
for i in range(2, n+1):
    if i not in list:
        print(i, end = " ")
