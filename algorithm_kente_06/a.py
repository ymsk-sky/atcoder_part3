s = input()
for i in range(8):
    if i == 3:
        if s[i] != "-":
            print("No")
            exit()
    else:
        if not s[i].isdecimal():
            print("No")
            exit()
print("Yes")
