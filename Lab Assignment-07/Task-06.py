#Task6(a)
arr=[]
n=int(input("Enter length: "))
for i in range(n):
    num=float(input("Enter a number: "))
    arr.append(num)
large=arr[0]
large_ind=-1
for i in range (len(arr)):
    if large<arr[i]:
        large=arr[i]
        large_ind=i
print(f"Maximum element {large} found at index {large_ind}")

#Task6(b)
small=arr[0]
small_ind=-1
for i in range (len(arr)):
    if small>arr[i]:
        small=arr[i]
        small_ind=i
print(f"Minimum element {small} found at index {small_ind}")

#Task6(c)
sum=sum(arr)
print("Summation:",sum)

#Task6(d)
avg=sum/len(arr)
print(f"Average: {avg:.2f}")