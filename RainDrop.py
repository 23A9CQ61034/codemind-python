N = int(input())
if N % 3 == 0 and N % 5 != 0 and N % 7 != 0:
    print("Pling")
elif N % 5 == 0 and N % 3 != 0 and N % 7 != 0:
    print("Plang")
elif N % 7 == 0 and N % 3 != 0 and N % 5 != 0:
    print("Plong")
elif N % 3 == 0 and N % 5 == 0 and N % 7 != 0:
    print("PlingPlang")
elif N % 3 != 0 and N % 5 == 0 and N % 7 == 0:
    print("PlangPlong")
elif N % 3 == 0 and N % 5 != 0 and N % 7 == 0:
    print("PlingPlong")
elif N % 3 != 0 and N % 5 != 0 and N % 7 != 0:
    print(N)