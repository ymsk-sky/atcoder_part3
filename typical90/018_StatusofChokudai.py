from math import cos, sin, atan, pi, degrees

t = int(input())
l, x, y = map(int, input().split())
q = int(input())
el = [int(input()) for _ in range(q)]
for e in el:
    # e:rad = t:2pi <=> rad = 2*e*pi/t より角度を求める
    ye = l / 2 *cos(-(pi / 2 + 2 * e * pi / t))
    ze = l / 2 *sin(-(pi / 2 + 2 * e * pi / t)) + l/2
    d = ((y - ye) ** 2 + x ** 2) ** 0.5
    # 底辺d,高さzeの三角形の角度[degree]
    ans = degrees(atan(ze / d))
    print(ans)