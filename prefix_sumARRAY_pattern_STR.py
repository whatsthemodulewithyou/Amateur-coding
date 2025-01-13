nums = "one", "two", "three", "four"

##this is soo cool so basically this is a prefix sum array. 
##this shows us the commulative sum of items.
##usually on the examples they use number datatypes but im different =p
##this is to demostrate usability and flexibility of this solution.

def prefixSum(nums):
    prefix = [nums[0]]
    for num in range(1, len(nums)):
        prefix.append(prefix[-1] + nums[num])
    return prefix
    

print((prefixSum(nums)))
