number_list = [1, 2, 3, 4, 5, 6]

def find_sum(number_list):
    total_sum = 0 
    for num in number_list:
        total_sum += num
    return total_sum
sum_result = find_sum(number_list)
print(sum_result)

def find_difference(number_list):
    total_difference = 0
    for num in number_list:
        total_difference -= num
    return total_difference
difference_result = find_difference(number_list)
print(difference_result)


def find_product(number_list):
    total_product = 1
    for num in number_list:
        total_product *= num
    return total_product
product_result = find_product(number_list)
print(product_result)

def find_division(number_list):
    total_division = 1
    for num in number_list:
        total_division /= num
    return total_division
division_result = find_division(number_list)
print(division_result)

#This function adds up the numbers in the number_list and returns a TOTAL SUM. 
#The parameter is intentionally named "number_list" rather than just "list" to avoid confusion with built in names.
#It is also good practice to specify what type of value is inside a list.
#The print(result) function is used to display the result of the find_sum function.

#-------------------------------------------------------------------------#
##When "total_product" was equal to 0 the product result was to zero.
##After changing the value to 1 the console provided me with "720" as a response
##This is because the identity of multiplication is 1. a*1 is = a.
##The same identity principle applies to division. a/1 is = a.
