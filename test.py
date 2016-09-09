import copy
year = raw_input("Please input year:")
dic = {"year": 0, "old": 0, "new": 1}
list = []
n = int(year)
for i in xrange(n+1):
    dic["year"] = i
    if i%2 == 0:
        try:
            dic["old"] = list[-1]["old"]+list[-1]["new"]
            dic["new"] = dic["old"]
            tmp = copy.copy(dic)
            list.append(tmp)
        except:
            tmp = copy.copy(dic)
            list.append(tmp)
    else:
        try:
            dic["old"] = list[-1]["old"]+list[-1]["new"]-list[-5]["new"]
            dic["new"] = 0
            tmp = copy.copy(dic)
            list.append(tmp)
        except:
            tmp = copy.copy(dic)
            list.append(tmp)
print list[-1]["new"]+list[-1]["old"]
