# Following are the basic operations supported by an array.

# Traverse − print all the array elements one by one.

# Insertion − Adds an element at the given index.

# Deletion − Deletes an element at the given index.

# Search − Searches an element using the given index or by the value.

# Update − Updates an element at the given index.

from array import *
# arrayName = array(typecode, [Initializers])
arr = array("i" , [ 10, 20 ,30 ,50]) #creating Array
for i in arr:
    print(i)

#accesing array element
print(arr[0])
print(arr[3])

#insert element in array
arr.insert(1,60)
print(arr)

#deleting elemnt in array
arr.remove(30)
print(arr)

# searching on array

print(arr.index(10))
#update operation
arr[2]=200
print(arr)