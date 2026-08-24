l=[1,2,3,2,3,5,4,3,6]
nl=[]
for i in l:
    if i not in nl:
        nl.append(i)
print(nl)


l=[1,2,3,2,3,5,4,3,6]
unique=list(set(l))
print(unique)