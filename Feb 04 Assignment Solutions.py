#!/usr/bin/env python
# coding: utf-8

# # QUESTION 1 :

# In[1]:


'''Ques 1. Create a python program to sort the given list of tuples based on integer value using a lambda function.
[('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli', 24936)]

Ans. Below is the python program to sort the given list of tuples based on integer value using a lambda function : '''

# Code line goes here :

list_of_players = [('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli', 24936)]

sorted_players = sorted(list_of_players, key = lambda x : x[1], reverse = False)

print("The list of players are sorted in ascending order based upon their runs scored : ")
print(sorted_players)


# Explanation ------------------------------------------------------------------------------------------------------------------------------------------------------------------
Explanation_1 = ''' In this program, we first define a list of tuples called list_of_players that contains the names of some cricketers and their total number of runs scored.
We then use the sorted() function to sort the players list based on the integer value of runs scored.
We use a lambda function as the key argument to specify that we want to sort the list based on the second element of each tuple (i.e., the integer value of runs scored).
We also set the reverse parameter to False to sort the list in ascending order.
Finally, we print the sorted list. '''


# # QUESTION 2 :

# In[2]:


'''Ques 2. Write a Python Program to find the squares of all the numbers in the given list of integers using lambda and map functions.
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Ans. Below is the Python Program to find the squares of all the numbers in the given list of integers using lambda and map functions : '''

# Code line goes here :

list_of_integers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(list(map(lambda sq : sq**2, list_of_integers)))


# Explanation ---------------------------------------------------------------------------------------------------------------------------
Explanation_2 = ''' In this program, we first define a list of integers called list_of_integers that contains some numbers.
We then use the map() function to apply a lambda function to each element of the list_of_integers list.
The lambda function takes a single argument sq and returns the square of sq
We convert the result of map() to a list using the list() function.
And then finally, we use print() function to avoid the error of not printing the result. '''


# # QUESTION 3 :

# In[3]:


'''Ques 3. Write a python program to convert the given list of integers into a tuple of strings. Use map and lambda functions

Given String: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Expected output: ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')

Ans. Below is the python program to convert the given list of integers into a tuple of strings using map and lambda functions : '''

# Code line goes here :

given_string = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Given String :", given_string)
print()
print("Output as Expected :", tuple(map(lambda x : str(x), given_string)))


# Explanation -------------------------------------------------------------------------------------------------------------
Explanation_3 = ''' In this program, we first define a list of integers called given_string that contains some numbers.
Then we print the given list and the message for the user to know about this program.
We then use the map() function to apply a lambda function to each element of the given_string list.
The lambda function takes a single argument x and returns a string representation of x using the str() function.
Finally, we convert the result of map() to a tuple using the tuple() function. '''


# # QUESTION 4 :

# In[4]:


'''Ques 4. Write a python program using reduce function to compute the product of a list containing numbers from 1 to 25.

Ans. Below is the python program to compute the product of a list containing numbers from 1 to 25 using reduce function : '''

# Code line goes here :

from functools import reduce

print("Please find below the product of numbers from 1 to 25 : ")
print(reduce(lambda x, y : x * y, list(range(1,26))))


# Explanation ----------------------------------------------------------------------------------------------
Explanation_4 = ''' In this program, we first import the reduce() function from the functools module.
Then we print the message for the user to know about this program.
We then create a list using the range() function that contains all the numbers from 1 to 25.
We use the reduce() function to compute the product of all the elements in the list.
The lambda function takes two arguments x and y, multiplies them, and returns the result.
And then finally, we use print() function to avoid the error of not printing the result. '''


# # QUESTION 5 :

# In[5]:


'''Ques 5. Write a python program to filter the numbers in a given list that are divisible by 2 and 3 using the filter function.

[2, 3, 6, 9, 27, 60, 90, 120, 55, 46]

Ans. Below is the python program to filter the numbers in a given list that are divisible by 2 and 3 using the filter function : '''

# Code line goes here :

given_list = [2, 3, 6, 9, 27, 60, 90, 120, 55, 46]

print("Given List :", given_list)
print("""
Numbers that are divisible by both 2 and 3 are below :""")
print(list(filter(lambda x : x % 2 == 0 and x % 3 == 0, given_list)))


# Explanation ----------------------------------------------------------------------------------------------
Explanation_5 = ''' In this program, we first define the list of numbers as given_list.
Then we print the given list and the message for the user to know about this program.
Then we use the filter() function to filter out the elements of the list that are divisible by 2 and 3.
The first argument of the filter() function is a lambda function that takes a number as input and returns True if the number is divisible by both 2 and 3.
The second argument of the filter() function is the list of numbers we want to filter.
We convert the filtered result into a list using the list() function.
Finally, we print the filtered list of numbers by using print() function to avoid the error of not printing the result. '''


# # QUESTION 6 :

# In[6]:


'''Ques 6. Write a python program to find palindromes in the given list of strings using lambda and filter function.

['python', 'php', 'aba', 'radar', 'level']

Ans. Below is the python program to find palindromes in the given list of strings using lambda and filter function : '''

# Code line goes here :

string = ['python', 'php', 'aba', 'radar', 'level']

print("Given String :", string)
print("""
Please find below the palindromes in the given list of string :""")

print(list(filter(lambda x : x == x[::-1], string)))


# Explanation ----------------------------------------------------------------------------------------------
Explanation_6 = ''' In this program, we define the list of strings as string.
Then we print the given list of strings and the message for the user to know about this program.
We use the filter() function to filter out the palindromes from the list.
The first argument of the filter() function is a lambda function that takes a string as input and checks if the string is equal to its reverse.
If the string is a palindrome, the lambda function returns True and the string is included in the filtered result.
The second argument of the filter() function is the list of strings we want to filter.
We convert the filtered result into a list using the list() function.
Finally, we print the list of palindromes by using print() function to avoid the error of not printing the result. '''


# In[ ]:




