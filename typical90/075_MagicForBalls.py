n = int(input())

def factorization(n):
    arr = []
    tmp = n
    for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
        if tmp % i == 0:
            cnt = 0
            while tmp % i == 0:
                cnt += 1
                tmp //= i
            arr.append([i, cnt])
    if tmp != 1:
        arr.append([tmp, 1])
    if arr == []:
        arr.append([n, 1])
    return arr

k = sum([y for _, y in factorization(n)])
ans = 0
while k > 1:
    k = -(-k // 2)
    ans += 1
print(ans)