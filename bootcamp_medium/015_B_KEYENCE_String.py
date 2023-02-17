s = input()
k = "keyence"
def f(s):
    if s[:7] == k or s[-7:] == k:
        return "YES"
    for i in range(1, 8):
        if s[:i] == k[:i] and s[-(7-i):] == k[-(7-i):]:
            return "YES"
    return "NO"
print(f(s))
