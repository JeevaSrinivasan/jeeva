num_list=[]
list_1=[]
for l in range(1,31):
    num_list=[]
    for i in range(1,11):
        num_list.append(i*l)
    list_1.append(num_list)
for n in list_1:
    print(n)
"""i=[0,1,2,3]
j=[0]
j.append(i)
j.extend(i)
#i.clear()
i=[]
print(j)"""