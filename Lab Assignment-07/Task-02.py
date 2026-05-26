arr=[]
n=int(input("Enter length: "))
for i in range(n):
    num=int(input("Enter a number: "))
    arr.append(num)
print("Before removing duplicates: ")
print(arr)

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if(arr[i]==arr[j]):
            arr[j]=0
print("After replacing duplicates with 0: ")
print(arr)
