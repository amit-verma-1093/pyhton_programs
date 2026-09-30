str="aa dd aa bb ccc"
str=str.replace(" ","")
val=set(str)
for i in val:
    count=0
    for j in range(0,len(str)):
        if i==str[j]:
            count+=1
    print(i,"=",count)
