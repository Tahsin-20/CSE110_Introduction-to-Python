start=int(input("Start:"))
end=int(input("End:"))
for i in range (start,end+1):
    num=i
    num_r=num
    count=0
    sum=0
    while(num>0):
        num=num//10
        count+=1
    div=10**(count-1)
    while(num_r>0):
        digit=num_r//div
        sum=sum+(digit**count)
        num_r=num_r%div
        div=div//10
    if(sum==i):
        print(i)
