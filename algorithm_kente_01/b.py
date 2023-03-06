n = int(input())
bef = int(input())
for _ in range(n - 1):
    crt = int(input())
    dif = crt - bef
    if dif == 0:
        print("stay")
    elif dif < 0:
        print("down", -dif)
    else:
        print("up", dif)
    bef = crt
