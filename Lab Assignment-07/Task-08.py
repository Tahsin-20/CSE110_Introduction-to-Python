n1 = int(input("Please enter the length of array 1: "))
print("Please enter the elements of the arr1:")
arr1 = []
for i in range(n1):
    arr1.append(int(input()))

n2 = int(input("Please enter the length of array 2: "))
print("Please enter the elements of the arr2:")
arr2 = []
for i in range(n2):
    arr2.append(int(input()))

    is_subset = True

for element in arr2:
    if element not in arr1:
        is_subset = False
        break 

if is_subset:
    print("Array 2 is a subset of Array 1.")
else:
     print("Array 2 is NOT a subset of Array 1.")