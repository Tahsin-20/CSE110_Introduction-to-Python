height=int(input("Enter height: "))
for i in range (1, height+1):
    for j in range(height-i):
        print(" ",end=" ")
    
    for j in range(1, 2*i):
        print(j, end=" ")
    
    print()