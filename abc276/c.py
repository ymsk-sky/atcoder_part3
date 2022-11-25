# rs[i]: i!
rs = [1] * 101
for i in range(100):
    rs[i + 1] = rs[i] * (i + 1)

def kth_permutation(n, k):
    """
    長さnの(1,2,...,n)を並び替えてできる順列を
    辞書順で並べたときにk番目にくる順列を返す
    Params
    --------
    n: int
        順列の長さ
    k: int
        何番目か
    Returns
    --------
    l: list
        k番目の順列
    """
    s = [i for i in range(1, n + 1)]
    l = []
    for i in range(n):
        a = rs[n - 1 - i]
        j = k // a
        k %= a
        l.append(s[j])
        s = s[:j] + s[j + 1:]
    return l

def id_of_permutation(l):
    """
    順列lが辞書順で何番目かを返す
    Params
    --------
    l: list
        (長さがnのとき1~nを並び替えてできる)順列
    Returns
    --------
    k: int
        何番目か
    """
    k = 0
    while len(l) > 1:
        a = len([m for m in l if m < l[0]])
        k += a * rs[len(l) - 1]
        l = l[1:]
    return k

n = int(input())
pl = list(map(int, input().split()))

print(*kth_permutation(n, id_of_permutation(pl) - 1))