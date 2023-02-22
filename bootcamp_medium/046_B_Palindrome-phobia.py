s = input()
a = s.count("a")
b = s.count("b")
c = s.count("c")
if max(abs(a - b), abs(b - c), abs(c - a)) < 2:
    print("YES")
else:
    print("NO")
