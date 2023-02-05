n, a, b = map(int, input().split())
s = input()
passed_a = 0
passed_b = 0
for c in s:
    if c == "a":
        if passed_a + passed_b < a + b:
            print("Yes")
            passed_a += 1
        else:
            print("No")
    elif c == "b":
        if passed_a + passed_b < a + b and passed_b + 1 <= b:
            print("Yes")
            passed_b += 1
        else:
            print("No")
    elif c == "c":
        print("No")
