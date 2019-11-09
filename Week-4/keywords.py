'''
keywords.py

Create functions that use keyword arguments
with default values.
'''

def welcome_message(user_name = None, place = None):
    if (user_name == None) and (place == None):
        return 'Hello and welcome'
    elif (user_name != None) and (place == None):
        return ('Hello, ' + user_name + ', and welcome')
    elif (user_name == None) and (place != None):
        return ('Hello and welcome to ' + place)
    else:
        return ('Hello, ' + user_name + ', and welcome to ' + place)    
# Create a function called welcome_message():
# if no input argument is provided
# it returns the string 'Hello and welcome'
# if a keyword argument called user_name is provided
# it returns 'Hello, <user_name>, and welcome'
# if a keyword argument called place is provided
# it returns 'Hello and welcome to <place>'
# if both user_name and place are provided
# it returns 'Hello, <user_name>, and welcome to <place>

def list_average(num_list = None, avg_type = None):
    if num_list == None or len(num_list) == 0:
        return 0
    if avg_type == 'mean' or avg_type == None:
        return sum(num_list)/len(num_list)
    if avg_type == 'mode':
        return max(num_list, key = str(int(num_list.count)))
    if avg_type == 'median':
        n = len(num_list)
        num_list.sort()
        if n == 0:
            return False
        if n % 2 == 0:
            median1 = num_list[n//2]
            median2 = num_list[n//2 - 1]
            median = (median1 + median2) / 2
        else:
            median = num_list[n//2]
        return median
        
        





# Create a function called list_average()
# without using any libraries to do the maths for you 
# (the point of this exercise is to practice interacting 
# with lists)
# the first argument is a list of numbers
# the second optional keyword arguemt is called avg_type
# if nothing for avg_type provided, return the mean of the list
# if avg_type='mode', return the mode of the list 
# (return list of all modes if there is a tie between multiple values)
# if avg_type='mean', return the mean of the list
# if avg_type='median', return the median of this list