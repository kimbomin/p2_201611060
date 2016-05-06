import math
Locations=tuple()
myList=list()
(x1,y1)=(37.575821,126.973548)
Locations=[(37.576547,126.985429),(37.571619,126.976318),(37.574470,126.957779),(37.570167,126.983075),(37.565813,126.966629)]
mylist=list()
for i in Locations:
    mylist.append(math.sqrt((x1-i[0])**2+(y1-i[1])**2))
print min(mylist)