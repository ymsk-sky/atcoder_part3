"""コーナーケースを確認
2x2のみ条件がある
->高さ1,幅1のところでは2個以上置いても条件に関与しない
"""
h, w = map(int, input().split())
ans = (-h // 2) * (-w // 2)
if h == 1 or w == 1:
    ans = h * w
print(ans)