a = input()
n = len(a)
if n%3 == 0:
    print(a[:3] + chr(96 + n//3 - 1))
else:
    print(a[:n%3] + chr(96 + n//3))
