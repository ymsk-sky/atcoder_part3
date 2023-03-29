import datetime

# 2022/01/01
s = input()

def daterange(st, ed):
    for n in range((ed - st).days):
        yield st + datetime.timedelta(n)

st = datetime.datetime.strptime(s, "%Y/%m/%d").date()
ed = datetime.datetime.strptime("4000/12/31", "%Y/%m/%d").date()
for i in daterange(st, ed):
    if len(set(str(i).replace("-", ""))) < 3:
        print(str(i).replace("-", "/"))
        break
