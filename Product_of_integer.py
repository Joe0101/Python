def product(n):
    pro=1
    while(n!=0):
        pro=pro*(n%10)
        n=n//10
    return pro
n=int(input())
print(product(n))
