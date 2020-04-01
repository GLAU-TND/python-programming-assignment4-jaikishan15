x = input()
y = list(map(str,input().split( )))
a = []
for i in y:
    if x == i[0:2]:
        a.append(i)
print(a)
