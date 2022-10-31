s = input()
a = int(s[:2])
b = int(s[2:])
f = 0 <= a <= 99 and 1 <= b <= 12
g = 1<= a <= 12 and 0 <= b <= 99
if f and g:
    print("AMBIGUOUS")
elif f:
    print("YYMM")
elif g:
    print("MMYY")
else:
    print("NA")