lst=[1,2,3,4,5,6,7,8,9]
target=int(input())
for i in lst:
    for j in lst:
        two_sum=i+j
        if two_sum==target:
            print(f"{i}+{j}")
        
