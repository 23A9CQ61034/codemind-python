import math
input_str = input()
a_str, b_str = input_str.split()
a = int(a_str)
b = int(b_str)
c=math.sqrt(pow(a,2)+pow(b,2))
print(f"{c:.2f}")