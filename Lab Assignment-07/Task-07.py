arr=[]
n=int(input("Enter length: "))
for i in range(n):
    num=int(input("Enter a number: "))
    arr.append(num)
print("Input array:")
print(arr)

new_arr=[]
seen=set()

for num in arr:
    if num not in seen:
        seen.add(num)
        new_arr.append(num)

print("New array:")
print(new_arr)