N=9
M=27
for i in range(N//2):
    pattern = ".|." * (2*i + 1)
    print(pattern.center(M, "-"))
print("wellcome".center(M,"-"))
for i in range((N//2)-1,-1,-1):
    pattern = ".|." * (2*i + 1)
    print(pattern.center(M, "-"))