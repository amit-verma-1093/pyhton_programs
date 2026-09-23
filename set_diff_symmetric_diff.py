M=int(input())
arrm=set(map(int,input().split()))
N=int(input())
arrn=set(map(int,input().split()))
s1=arrn | arrm
l=[]
for i in s1:
    if i not in arrm & arrn:
        l.append(i)
l.sort()
for i in l:
    print(i)


# M = int(input())
# arrm = set(map(int, input().split()))

# N = int(input())
# arrn = set(map(int, input().split()))

# result = arrm ^ arrn   # symmetric difference

# for i in sorted(result):
#     print(i)