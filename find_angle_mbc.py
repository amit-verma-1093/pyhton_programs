import math

ab=int(input())
bc=int(input())


result=math.atan(ab/bc)
result=math.degrees(result)
print(f"{round(result)}\u00b0")
