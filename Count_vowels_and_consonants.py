str=input("eter the number: ")
vow=0
con=0
vowel="aeiouAEIOU"
for i in range(len(str)):
    if str[i] in vowel:
        vow+=1
    else:
        con+=1
print(vow,con)