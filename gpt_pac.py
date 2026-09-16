# First Non-Repeating Element

n=[5,1,5]
for i in range(len(n)-1):
    lst=n[-1:i:-1]
    if n[i] not in lst:
        print(n[i])
        break

for i in n:
    if n.count(i) == 1:
        print(i)
        break
# Sum of Digits of All Numbers in List

# n=[12, 34, 5]
# lst=[]
# for num in n:
#     sum=0
#     for i in (str(num)):
#         sum+=int(i)
#     lst.append(sum)
# total=0
# for j in lst:
#     total+=j
# print(total)

# Find Peak Element

# n=[1, 3, 20, 4, 1, 0]
# print(max(n))

# Left Rotate by 1

# n=[1, 3, 20, 4, 1, 0]
# temp=n[0]
# for i in range(len(n)-1):
#     n[i]=n[i+1]
# n[-1]=temp
# print(n)

# Check Subarray Exists with Sum = 0
