"""自己解決
しゃくとり法: O(N)
連続部分列の要素の種類と各個数を辞書(defaultdict)で管理
"""
from collections import defaultdict

n, k = map(int, input().split())
al = list(map(int, input().split()))
s = defaultdict(int)  # 連続部分列を管理
l = 0  # 現在の種類数

def add(v):
    global l
    s[v] += 1
    if s[v] == 1:
        l += 1

def addable(v):
    # 既にvが1つ以上存在: 種類は増えない
    if s[v] > 0:
        return True
    # vはないが種類が増えてもk種類以下を保持
    if l + 1 <= k:
        return True
    else:
        return False

ans = 0
right = 0
for left in range(n):
    while right < n and addable(al[right]):
        add(al[right])
        right += 1
    ans = max(ans, right - left)
    if left == right:
        right += 1
    else:
        s[al[left]] -= 1
        if s[al[left]] == 0:
            l -= 1
print(ans)