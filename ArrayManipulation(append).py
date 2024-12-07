from array import array
##This is how we add an element to an Array
## a goofy way of thinking about it like adding
## APPend app end. Whatever you w
## the data type is i= int f=float u=unicode 
arr = array('i',[1, 2, 3, 4, 5, 6, 7, 8, 9,])
arr1 = array('u',['a', 'b', 'c', 'd', 'e', 'f','g', 'h','i'])
arr2 = array('f',[1, 2, 3, 4, 5, 6, 7, 8, 9, 0,])

arr.append(0)
arr.append(23)
arr.append(29)
arr.append(30)
arr.append(31)
arr.append(22)
print(arr, arr1, arr2)



