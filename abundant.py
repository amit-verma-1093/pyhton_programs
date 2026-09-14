n=int(input("enter the number"))
sum=0
for i in range(1,n):
    if n%i==0:
        sum+=i
print(sum)
if sum>n:
    print("its a abudant number")
else:
    print("its not a abuduant number")