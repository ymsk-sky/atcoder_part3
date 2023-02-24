n, a, b, c, d = map(int, input().split())
s = input()
if c < d:
    if "##" in s[a:c] or "##" in s[b:d]:
        print("No")
    else:
        print("Yes")
else:
    if "##" in s[a:c] or not "..." in s[b-2:d+1]:
        print("No")
    else:
        print("Yes")
