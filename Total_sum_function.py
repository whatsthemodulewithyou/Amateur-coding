def find_sum(number_list):
    total_sum = 0 
    for num in number_list:
        total_sum += num
    return total_sum

number_list = [1, 2, 3, 4, 5, 6]
result = find_sum(number_list)
print(result)


#This function adds up the numbers in the number_list and returns a TOTAL SUM. 
#The parameter is intentionally named "number_list" rather than just "list" to avoid confusion with built in names.
#The print(result) function is used to display the result of the find_sum function.