from math import atan, degrees

a, b, x = map(int, input().split())
# 傾けていくと中身は直方体->台形の柱->三角柱の形で遷移する

if a * a * b / 2 > x:
    """三角柱
    底面の長方形をy*aとすると a*y*b/2=x より y=2*x/(a*b)
    するとtanθ=b/yよりθ=atan(b/y)=atan((a*b*b)/(2*x))
    """
    r = atan(a * b * b / (2 * x))
else:
    """台形の柱
    つくられる台形の短いほうをyとすると y=2*b-2*x/a**2
    (y+b)*a*a/2 = x
    y+b = 2*x/a**2
    y = 2*x/a**2 - b
      y_
    ／  | a
    ----
     b
    するとtanθ=(b-y)/a = (b - (2*x/a**2 - b))/a
    = (2*b - 2*x/a**2)/a
    θ = atan((2*b - 2*x/a**2) / a)
    """
    r = atan((2*b - 2*x / (a*a)) / a)
ans = degrees(r)
print(ans)


"""
1<=a,b<=100
1<=x<=a*a*b

底a*a,高さb
"""
