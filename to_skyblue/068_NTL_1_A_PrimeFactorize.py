def f(n):
    ans = []
    tmp = n
    for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
        if tmp % i == 0:
            cnt = 0
            while tmp % i == 0:
                cnt += 1
                tmp //= i
            ans.append([i, cnt])
    if tmp != 1:
        ans.append([tmp, 1])
    if tmp == []:
        ans.append([n, 1])
    return ans

n = int(input())
ans = f(n)
print(str(n) + ":", *[v for v, k in ans for _ in range(k)])