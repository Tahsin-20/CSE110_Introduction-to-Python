num=int(input("Enter an integer:"))
non_neg=0
neg=0

for i in range(1, num+1):
    a=int(input(f"Enter number {i}: "))

    if(a>=0):
        non_neg+=1
    else:
        neg+=1
print(non_neg,"Non-negative Numbers")
print(neg,"Negative Numbers")