num=int(input("Enter a number:"))
count=0
pc=0
prime=2
while pc<num:
    count=0
    for i in range(1,prime+1):
        if(prime%i==0):
            count+=1

    if(count==2):
        print(prime)
        pc+=1
    prime+=1