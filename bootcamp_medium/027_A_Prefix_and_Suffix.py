n = int(input())
s = input()
t = input()

for i in range(n, 0, -1):
    if s[-i:] == t[:i]:
        print(2*n - i)
        exit()
print(2*n)
