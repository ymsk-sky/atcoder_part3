n = int(input())
left = 1
right = n
for _ in range(10):
    mid = (left + right) // 2
    print(f"? {left} {mid} 1 {n}")
    t = int(input())
    if t == mid - left + 1:
        left, right = mid + 1, right
    else:
        left, right = left, mid
x = left
left = 1
right = n
for _ in range(10):
    mid = (left + right) // 2
    print(f"? 1 {n} {left} {mid}")
    t = int(input())
    if t == mid - left + 1:
        left, right = mid + 1, right
    else:
        left, right = left, mid
y = left
print(f"! {x} {y}")