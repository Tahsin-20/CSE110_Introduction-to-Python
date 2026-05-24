num=int(input("Enter an Integer:"))

for i in range (num+1):
    if(i%5==0 and i%3!=0):
        print(i)