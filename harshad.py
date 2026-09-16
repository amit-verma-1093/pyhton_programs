n=int(input("enter the number"))
num=n
sum=0
digit=0
while num!=0:
    digit=num%10 
    num//=10   
    sum+=digit
if n%sum==0:
    print("its a harshad number")                
else:
    print("it is not a harshad number ")