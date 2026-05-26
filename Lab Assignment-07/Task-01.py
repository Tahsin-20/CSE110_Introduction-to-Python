arr=[]
n=int(input("Enter length: "))
for i in range(n):
    num=int(input("Enter a number: "))
    arr.append(num)

for i in range(len(arr)):
    print(f"{i}:{arr[i]}")
new=int(input("Enter another number: "))
arr.append(new)
print(arr)
