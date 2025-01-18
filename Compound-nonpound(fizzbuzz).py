for i in range(1, 200):
    if i % 2 == 0 and i % 4 == 0:
        print("ComPound")
    elif i % 2 == 0:
        print("Com")
    elif i % 4 == 0:
        print("Pound")
    else:
        print(i)



#The for-loop iterates through the numbers presented in the presented range.
    
    ###if the first condition that contains two requirements are met , it executes the command for that condition
  #  elif the condition is not met it proceeds to the two other edgecases which is i % 2 or i % 4. and lastly an exit 
#    condition for cases that dont meet any of the requirements.###

##this is my own variation of the famously known "fizzbuzz" problem.
##i changed the orginal compound word to demostrate my understanding is beyond reiteration and copy-paste.