n = int(input())
l = [0] * n
for _ in range(n):
    a = int(input())
    l[a - 1] += 1
x = y = -1
for i in range(n):
    if l[i] == 2:
        x = i + 1
    if l[i] == 0:
        y = i + 1
if x == y:
    print("Correct")
else:
    print(x, y)
