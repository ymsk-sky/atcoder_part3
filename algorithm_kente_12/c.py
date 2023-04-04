pl = [list(map(int, input().split())) for _ in range(3)]
ans = [0] * 18
for i in range(6):
    for j in range(6):
        for k in range(6):
            n = i + j + k + 3
            ans[n - 1] += pl[0][i]*pl[1][j]*pl[2][k]
for an in ans:
    print(f"{an/1000000:.6f}")
