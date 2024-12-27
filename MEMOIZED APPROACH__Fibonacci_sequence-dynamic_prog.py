#This function does three things: 
# first - it calculates the postion of the n position of the fib sequence and the related value. 
# second - stores every recoursive value that was gathered throughtout the calculation into globalized memoization list.
# third - displays the calculation.
memo_globalized = {}
def fib(n) :
    if n in memo_globalized:
        return memo_globalized[n]
    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
n = 0
result = fib(n)
print(fib(20))


#THIS SCRIPT IS THE MEMOIZED APPROACH

#This is a better approach than the naive approach. All recoursions get stored into the list represented by memo = {} This makes the calculation
#Faster because the machine does not re-process the values stored into into the list.

#Problem here? - Although faster at processing than naive. It can cost a bit of memory because of the storage in memo = {}

# (TIME COMPLEXITY) : O(n) due to the caching of already scanned recoursions.
 
# (SPACECOMPLEXITY): O(n) due to the call stack used for recursion. At any time, the maximum depth of the recursion stack is proportional to n

#How does memoization work? - Memoization works by caching the reiterations that have already been computed.

#I wrote 2 of the same functions but I made one with a GLOBAL memo_list and a LOCAL memo_list. To display knowledge of variable placement.

def fib(n) :
    if n in memo_localized:
        return memo_localized[n]
    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
memo_localized = {}
n = 0
result = fib(n)
print(fib(21))



