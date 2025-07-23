''''
conditional statement is also called as a decission making statement.
if
else
elif
nested if 
the above 4 are the conditional statement
***
if the condition is true in if condition then 
statement1 will execute other wise it enters into
the elif statement2 and agains if the condition is 
true in elif contion then statement2 will be execute
other wise it enters into else statement3.

syntax for if ,elif ,else .
 
 if condition:
    print(statement1)
 elif condition:
    print(statement2)
 else:
    print(statement3)

***
nested if:
which we can write inside of the 
if statement of if condition is known as 
nested if 
 
syntax for nested if .
 
 if condition:
    print(statement)
    if condition:
       print(statement)
    else:
       print(statement)
 else:
    print(statement)

note: by using logical operaters
like {and ,or, not} we will check
two conditions in conditional statement 

'''
# if True:
#     print("nenu if")
# else:
#     print("nenu else")
   
    
# if False:
#     print("nenu if")
# else:
#     print("nenu else")
    
# if False:
#     print("nenu if")
# elif True:
#     print("nenu elif")   
# else:
#     print("nenu else")
 
# if False:
#     print("nenu if")
# elif False:
#     print("nenu elif")    
# else:
#     print("nenu else")
 ### nested if statements   
"""if True:
    print("outer if")
    if True:
        print("inner if")
    else:
        print("inner else")
else:
    print("outer else")    
    
if False:
    print("outer if")
    if True:
        print("inner if")
    else:
        print("inner else")
else:
    print("outer else")
    
if True:
    print("outer if")
    if False:
        print("inner if")
    else:
        print("inner else")
else:
    print("outer else") 
               
if False:
    print("outer if")
    if False:
        print("inner if")
    else:
        print("inner else")
else:
    print("outer else")        
 
"""
# write a python programm on eligible for vote
"""age=47
if  age>18:
    print("you can vote")
elif age==18:
    print("you can eligible for vote")
else:
    print("you can not eligible for  vote")
"""
#write a python programm on agge wise names
"""ge=21
if age>0 and age<12:
    print("you are a children")
elif age>13 and age <19:
    print("you are in teenage stage ")
elif age>20 and age<30:
    print("you are in adulthood stage")
elif age>31 and age<60:
    print("yor are a middel aged person")
else:
    print("you are a old man")
"""
