arr=[]
n=int(input("Enter length: "))
for i in range(n):
    num=int(input("Enter a number: "))
    arr.append(num)
tar=int(input("Enter the number you want to find: "))
found=False
index=-1
for i in range (len(arr)):
    if(arr[i]==tar):
        index=i
        found=True
        break
if(found):
    print(tar,"is at index", index)
else:
    print("Element not found")

