from array import array

int_arr = array('i',[])
float_arr = array('f',[])

int_arr.append(1)
int_arr.extend([1, 2, 3, 4,])
float_arr.append(1)
float_arr.extend([1, 2, 3, 4,])
print(int_arr, float_arr)


#when you add extend make sure to add the subscript operator [] and put a set in there.
#extend is a more extreme version of append.
#as good practice add the Type of array. So Prefix the attomic thing which in these tow case its int and float
##prefix it with the type. If you imagining a dog red_dog , big_dog, small_dog , endless types
##type goes first hence TYPE_SHIT 