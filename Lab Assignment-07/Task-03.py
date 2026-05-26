#Task3(a)
arr=[]
n=int(input("Enter length: "))
for i in range(n):
    num=int(input("Enter a number: "))
    arr.append(num)
new_arr=[]

for i in range (len(arr)-1, -1 , -1):
    new_arr.append(arr[i])
print(new_arr)

i=0
j=len(arr)-1

while i<j:
    a=arr[i]
    arr[i]=arr[j]
    arr[j]=a
    i+=1
    j-=1
print(arr)