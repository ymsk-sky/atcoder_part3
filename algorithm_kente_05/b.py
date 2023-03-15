n = int(input())
s = input()
t = ""
for c in s:
    t = t.replace(c, "") + c

print(t)
