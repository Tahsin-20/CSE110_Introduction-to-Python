num=int(input("Input number of terms:"))
count=0
sum=0
i=1
print("The odd numbers are:")

while count<num:
    print(i)
    sum+=i
    i+=2
    count+=1
print(f"The Sum of odd Natural Numbers up to {num} terms is:",sum)