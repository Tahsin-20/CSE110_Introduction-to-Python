#Task11(a)
num=int(input("Enter a number:"))
count=0
for i in range(1,num+1):
    if(num%i==0):
        count+=1
if(count==2):
    print(num,"is a prime number")
else:
    print(num,"is not a prime number")
sum=0
for i in range(1,num):
    if(num%i==0):
        sum+=i
if(sum==num):
    print(num,"is a perfect number")
else:
    print(num,"is not a perfect number")