def hanoi(n,source,auxiliary,end):
    if n==1:
        print(f"move disk from {source} to {end}")
        return
    else:
        hanoi(n-1,source,end,auxiliary)
        print(f"move disk from {source} to {end}")
        hanoi(n-1,auxiliary,source,end)
num=int(input("sdd"))
hanoi(num,"A","B","C")