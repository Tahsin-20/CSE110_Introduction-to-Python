arr=[]
n=int(input("Enter length: "))
for i in range(n):
    num=int(input("Enter a number: "))
    arr.append(num)
print("Original array: ")
print(arr)

for i in range (len(arr)):
    if arr[i]>0:
        arr[i]=1
    elif arr[i]<0:
        arr[i]=0
print("After modifying: ")
print(arr)