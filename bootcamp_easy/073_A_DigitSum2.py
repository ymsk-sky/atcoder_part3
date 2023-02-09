n = input()
ans = max(sum([int(v) for v in n]), (int(n[0]) - 1) + 9*(len(n) - 1))
print(ans)