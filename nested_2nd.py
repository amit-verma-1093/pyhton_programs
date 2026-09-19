# lst=[]
# for _ in range(int(input())):
#     name = input()
#     score = float(input())
#     lst.append([name, score])

# scores = sorted(set([i[1] for i in lst]))
# second_lowest = scores[1]
    
# names = sorted([i[0] for i in lst if i[1] == second_lowest])
    
# for n in names:
#     print(n)
n=int(input())
for i in range(1,n+1):
    print("*"*i)