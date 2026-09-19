n=int(input("enter the number"))

sq=n*n
sum=0
while sq!=0:
    digit=sq%10
    sq//=10
    sum+=digit

print(sum)
if sum==n:
    print("its a neon number")
else:
    print("its not a neon number")