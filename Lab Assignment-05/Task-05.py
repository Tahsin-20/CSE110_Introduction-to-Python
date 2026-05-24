row=int(input("Enter row:"))
col=int(input("Enter column:"))
for i in range (col):
    for j in range(1, row+1):
        print(f"{j}", end=" ")
    print()