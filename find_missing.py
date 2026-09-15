#find the missing number
n = [2,3,4,5]

total = (len(n)+1)*(len(n)+2)//2
actual = sum(n)

print(total - actual)