"""自己回答
b*** より a*** のほうが***に関係なく辞書順で先
よって, 先頭文字から決定していく

i文字目で選べるのは(i-1)文字目の次 ~ (n-k+i)文字目
例) 10文字から3文字選ぶ場合
1文字目: 1 ~ 8
2文字目: max(2, (1文字目位置)+1) ~ 9
3文字目: max(3, (1文字目位置)+1) ~ 10

全探索するとO((N-K+1)K)でLTE

使える文字の最小を効率よく探索する必要
-> 優先度付きキューで文字をkeyとして同時にindexも所持
ひとつ前の文字より後に出てくる最小の文字を選んでいく
-> 計算量O(N)で可能

全体でO(N)
"""

import heapq

n, k = map(int, input().split())
s = input()

sl = []
heapq.heapify(sl)
for i in range(n - k):
    heapq.heappush(sl, [s[i], i])

ans = []
bef = -1  # (i-1)文字目のインデックス
for i in range(n - k, n):
    heapq.heappush(sl, [s[i], i])
    while 1:
        a, ai = heapq.heappop(sl)
        if ai > bef:
            break
    ans.append(a)
    bef = ai

print(*ans, sep="")