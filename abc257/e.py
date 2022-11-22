"""
でかい数字 -> 桁が多い ->
一旦, clの中の最小値のみで繰り替えした場合で考えると, 最高桁数がわかる
"""
n = int(input())
cl = list(map(int, input().split()))

# 最小値でのみ繰り返すことで最高桁数がわかる
m = min(cl)
l = n // m  # 最大桁数

ans = []
for i in range(l):
    # (l-i)桁目において, cl[j - 1]を大きい順で試してみる
    for j in range(9, 0, -1):
        # 残りのほかの桁はすべて最小値とする(上の桁が大きいほど数字は大きくなるので優先)
        if m * (l - 1 - i) + cl[j - 1] <= n:
            n -= cl[j - 1]
            ans.append(j)
            break
print(*ans, sep="")