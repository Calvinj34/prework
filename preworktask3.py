#1. 
#Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.
def hello_name(username):
 print("Hello, " +username.title() + "!" )
 
hello_name("Username")
#2. Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing
def odd_numbers(n):
    return [x for x in range(1, n+1) 
        if x % 2 != 0]

print(odd_numbers(100))


#3.
#Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.
def max_num_in_list( list ):

    max = list[0]
    for a in list:
	    if a > max:
                max = a
    return max
print(max_num_in_list([1,3,76,8,9]))

#4.Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. 
# The return should be boolean Type (true/false). 
def leap_year(y):
    if y % 400 == 0:
        return True
    if y % 100 == 0:
        return False
    if y % 4 == 0:
        return True
    else:
        return False
print(leap_year(2000))

#5. Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. 
# The return should be boolean Type.
def is_consecutive(nums):

    sorted_list = sorted(nums)
    range_list =list(range(min(nums), max(nums)+1))
    print(range_list)
    if sorted_list == range_list:
        return True
    else:
         return False
      
print(is_consecutive([1,2,4,5]))
