n = int(input())
al = list(map(int, input().split()))
ans = float("inf")
for c in range(-100, 101):
    tmp = sum([(a - c)**2 for a in al])
    ans = min(ans, tmp)
print(ans)