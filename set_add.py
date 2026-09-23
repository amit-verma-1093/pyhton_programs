n=int(input())
set1=set()
for i in range(n):
    val=input()
    set1.add(val)
count=0
for j in set1:
    count+=1
print(count)