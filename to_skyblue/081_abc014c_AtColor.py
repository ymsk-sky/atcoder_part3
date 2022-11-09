n = int(input())
l = [0] * 1000002
for _ in [0] * n:
    a, b = map(int, input().split())
    l[a] += 1
    l[b + 1] -= 1
for i in range(1, 1000002):
    l[i] += l[i - 1]
print(max(l))