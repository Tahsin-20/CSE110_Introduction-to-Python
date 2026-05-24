test=int(input("Enter test case:"))
while test>0:
    x=int(input("Enter a number:"))
    y=int(input("Enter no. of terms:"))
    sum=0
    count=0
    while count<y:
        if(x%2!=0):
            sum+=x
            count+=1
        x+=1
    test-=1
    print(sum)