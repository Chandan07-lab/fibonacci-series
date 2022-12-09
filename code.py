
def fibo(a,b,n):
    if n==0:
        return b
    else:
        print(a+b)
        return fibo(b,a+b,n-1)
n=int(input("enter how many terms you want:"))
print(0)
print(1)
fibo(0,1,n-2)
