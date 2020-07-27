from array import *
arr=array("i",[10,20,30,40,50])
# for i in arr:
#     print(i)
# b= single int 1 byte
#B=single int 1 byte
# c= 1byte of char
# I=unsign 2 byte
# f= floating 4byte
# d== 8 byte
print(arr[2])

# insertion
arr.insert(1,60)
print(arr)
# deletion
arr.remove(60)
print(arr)
#search
x=arr.index(30)
print(x)

#update
arr[0]=70
print(arr)
