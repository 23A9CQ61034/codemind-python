a=int(input())
b=a//3600
c=(a%3600)//60 
d=(a%3600)%60
print(f"H:M:S-{b}:{c}:{d}")