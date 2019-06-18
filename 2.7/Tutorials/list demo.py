list1=["Hippo", 5, "Rex Sneeze"]
list2=[[1,2,3],[4,5,6],[7,8,9]]
print(list1)
#print(list1[0])
print(list2[0][0])


for x in list1:
    print(x)

for x in list2:
    for y in x:
        print(y)
