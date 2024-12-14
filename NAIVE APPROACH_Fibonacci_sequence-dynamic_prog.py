#This function does two things: 
# first - it calculates the postion of the n position of the fib sequence and the related value. 
# second - displays the calculation.

def fib(n) :
    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
    
n = 17
result = fib(n)
print(f"The Fibonacci number at position {n} is: {result}")


#THIS SCRIPT IS THE NAIVE APPROACH

#This is the least effective way to solve the problem because it will UNECESSARILY repeat a particular sequence.
#The analogy I will use is an "Anaphora" is a rhetorical and poetic tool. Lets assume MLK is dealing with machines instead of Humans.
#MLK "I have a dream speech" reiterates "I have a dream" and throught the speech he repeats it over and over.
#If we ran the speech as an algorithm the "I have a dream" part of the speech would be the inefficiency.(overly simplified for example sake)
#This is because of OVERLAPPING SUBCASES through the re-itterating phase.Lack of MEMOIZATION or CACHING.


#Problem here? - It is very slow in getting results above a particular n input.

# (TIME COMPLEXITY) : O(2n) due to the recomputation of already identified subproblems.
 
# (SPACECOMPLEXITY): O(n) due to the call stack used for recursion. At any time, the maximum depth of the recursion stack is proportional to n


#The solution to this particular problem in Dynamic Program and its called : memoization

#How does memoization work? - Memoization works by caching the reiterations that have already been computed.



