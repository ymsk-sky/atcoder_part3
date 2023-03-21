s = input()
if (sum([int(c) for c in s[:-1][::2]])*3 + sum([int(c) for c in s[1::2]]))%10 == int(s[-1]):
    print("Yes")
else:
    print("No")
