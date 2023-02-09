x = int(input())
if x < 100:
    print(0)
    exit()

for i in range(5, 0, -1):
    n = (x%100)//i
    x -= 100*n
    x -= i*n
    if x < 0:
        print(0)
        exit()
if x%100 == 0:
    print(1)
else:
    print(0)