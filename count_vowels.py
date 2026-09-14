# s=input("enter the string: ")
# count=0
# for i in s:
#     if i=='a' or i=='e'or i=='o' or i=='u' or i=='i'or i=='A' or i=='E'or i=='I' or i=='O' or i=='U' :
#         count+=1
# print(count)

# s=input("enter the string: ")
# count=0
# vowels="aeiouAEIOU"
# for i in s:
#     if i in vowels:
#         count+=1
# print(count)

s=input("enter the string: ")
count=0
vowels="aeiou"
for i in s.lower():
    if i in vowels:
        count+=1
print(count)