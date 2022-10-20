"""
マンハッタン距離は45度回転
(x,y)を45度回転させたときの座標(X,Y)は以下:
    X = x - y
    Y = x + y
また,回転後の(x1,y1)と(x2,y2)のマンハッタン距離は,
max(|x1-x2|,|y1-y2|)となる

点(X,Y)の最大マンハッタン距離は以下のようになる
max(|X-x1|,|Y-y1|,|X-x2|,|Y-y2|,...,|X-xn|,|Y-yn|)
よって,(45度回転させた後の)xmin,ymin,xmax,ymaxがわかればよい

計算量O(N+Q)
"""
n, q = map(int, input().split())
xyl = [list(map(int, input().split())) for _ in range(n)]
queries = [int(input()) - 1 for _ in range(q)]

# 45度回転
xyl = [[x - y, x + y] for x, y in xyl]
x_min = min(xyl, key=lambda p: p[0])[0]
y_min = min(xyl, key=lambda p: p[1])[1]
x_max = max(xyl, key=lambda p: p[0])[0]
y_max = max(xyl, key=lambda p: p[1])[1]

for i in queries:
    x, y = xyl[i]
    ans = max(abs(x - x_min), abs(y - y_min), abs(x - x_max), abs(y - y_max))
    print(ans)