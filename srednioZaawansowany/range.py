list=list(range(10))
print('List',list,type(list))

print(list[:-1])

colors=['red','green','blue','black','white']   


def categories(colors,numberOfCategories):
    return colors[:numberOfCategories]


for i in range(1,len(colors)+1):
    print(categories(colors,i))

