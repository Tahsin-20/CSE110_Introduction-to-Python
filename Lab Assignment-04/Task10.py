num=int(input("Enter a number:"))
num_r=num
count=0
while(num>0):
    num=num//10
    count+=1
div=10**(count-1)
while(num_r>0):
    print(num_r//div, end="")

    if(div>1):
        print(",",end="")
    num_r=num_r%div
    div=div//10
