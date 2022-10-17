n = int(input())
if n % 2 == 1:
    exit()

def f(n):
    if n == 2:
        return ["()"]
    al = ["(" + a + ")" for a in f(n - 2)]
    bl = []
    tmp = {i: f(i) for i in range(2, n - 1, 2)}
    for i in range(2, n - 1, 2):
        for x in tmp[n - i]:
            for y in tmp[i]:
                bl.append(x + y)
    return sorted(list(set(al + bl)))

ans = f(n)
for an in ans:
    print(an)