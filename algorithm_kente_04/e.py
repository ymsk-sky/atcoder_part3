from itertools import permutations

n = int(input())
s = input()

for per in permutations(s):
    t = "".join(per)
    if s == t or s[::-1] == t:
        continue
    print(t)
    break
else:
    print("None")
