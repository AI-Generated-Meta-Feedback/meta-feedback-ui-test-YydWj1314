a = [(5, 3), (2, 1), (5, 2)]
n = len(a)

for i in range(1, n):
    x = a[i]
    j = i - 1
    while j >= 0 and (a[j][0] > x[0] or (a[j][0] == x[0] and a[j][1] > x[1])):
        a[j+1] = a[j]
        j -= 1
    a[j+1] = x

print(a)  # [(2, 1), (5, 2), (5, 3)]

