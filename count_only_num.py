s=input("enter : ")
max=0
digits="1234567890"
for i in s:
    if i in digits:
        num=int(i)
        if num>max:
            max=num
if max==0:
    print("no digit")
else:
    print(max)
