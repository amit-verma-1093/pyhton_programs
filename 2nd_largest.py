#2nd largest number without using sort()
lst=[10,5,34,22,67]
maxl=lst[0]
for i in lst:
    if i>maxl:
        maxl=i
        print(i)
print(maxl)#incomplete