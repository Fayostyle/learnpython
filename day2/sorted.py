r = sorted([23, -45, 54, 0, 34, -5], key=abs)
print(r)

r1 = sorted(['Ted', 'adm', 'bob', 'Zed'], key=str.lower)
print(r1)

###############
L = [('Bob', 75), ('Adam', 92), ('Bart', 77), ('Lisa', 88)]
#按姓名排序
def by_name(t):
    return t[0]
print(sorted(L, key=by_name, reverse=True))
#按成绩排序
def by_score(t):
    return int(t[1])
print(sorted(L, key=by_score))

