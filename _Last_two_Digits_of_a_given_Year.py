a = int(input())
if a % 100 == a % 10:
    print("0" + str(a % 10))
else:
    print(a % 100)
