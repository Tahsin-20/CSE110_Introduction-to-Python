while True:
    count=0
    num=int(input("Enter Number:"))
    for i in range (1,num+1):
        if(num%i==0):
            count+=1
    if(num%2!=0):
        break
    else:
        print(f"{num} has {count} divisors")
