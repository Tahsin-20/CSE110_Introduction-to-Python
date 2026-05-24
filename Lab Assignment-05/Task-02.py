n=int(input("The value of N:"))
result=0
sum=0
while n>0:
    for i in range (1,n+1):
        sum+=i
    result-=sum
    sum=0
    n-=1
print("The value of y:",result)