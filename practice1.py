#List smaller than 10

lists=[1,2,3,4,7,8,44,43,53,64,77,11,12,10]
newlist=[]
for list in lists:
    if list < 10:
        newlist.append(list)

print(newlist)
