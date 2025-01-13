def prefix_sum(array):
    prefix = []
    sum    =  0
for num in array:
    current_sum += sum
    prefix.append(array)
return prefix



----the following information below this line represents how the PREFIX SUM Pattern works.


 INDEX                 0   1  2  3   4
             
 input:  array      [ -2,  0, 3, -5, 2  ]
 
 output: prefix_sum [ -2, -2, 1, -4, -2 ]
 
 we want to find the prefix_sum of the array INDEX 0-4
 
 This is saying we want to find the running sum of -2, 0, 3, -5, and 2 in the input array that you see within 
 these [ ] brackets.
 

 prefix sum
 
 this calculates the CUMULATIVE sum of the entire(array) index 0-4
 
 from 0 the sum is -2 because -2 ~~~~~~~~~ = -2
 from 0 to 1 the sum is -2 because -2 +  0 = -2
 from 1 to 2 the sum is  1 because -2 +  3 =  1
 from 2 to 3 the sum is -4 because  1 + -5 = -4
 from 3 to 4 the sum is -2 because -4 + -2 = -2
 
 prefix_sum ~ [ -2, -2, 1, -4, -2 ]
 