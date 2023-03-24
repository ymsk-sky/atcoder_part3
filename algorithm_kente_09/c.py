n = int(input())
ans = {chr(i): -1 for i in range(65, 71)}
for i in range(1, n + 1):
    p, v = input().split()
    if v == "AC" and ans[p] == -1:
        ans[p] = i

for k in ans:
    print(ans[k])
