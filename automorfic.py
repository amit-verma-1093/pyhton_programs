n=int(input("enter the number"))
num=n
count=0
while num!=0:
    num//=10
    count+=1

sq=n**2
morfic= n%10**count
print(morfic)
if n==morfic:
    print("it is a automorfic number ")
else:
    print("it is not a automorfic number ")
