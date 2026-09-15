
   
number = int(input())
width = len(bin(number)[2:])

for i in range(1, number + 1):
    d = str(i)
    o = oct(i)[2:]
    h = hex(i)[2:].upper()
    b = bin(i)[2:]
        
    print(d.rjust(width), o.rjust(width), h.rjust(width), b.rjust(width))

