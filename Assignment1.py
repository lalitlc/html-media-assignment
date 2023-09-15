#!/usr/bin/env python
# coding: utf-8

# ##Question no -1 
#  
#  What are the characteristics of the tuples? Is tuple immutable?

# In computer programming, a tuple is a data structure that is similar to a list or an array, but with a few key differences. Here are some characteristics of tuples:
# 
# 1) Tuples are ordered: Each element in a tuple has a specific position, or index, in the tuple.
# 2)Tuples are heterogeneous: Unlike lists or arrays, each element in a tuple can have a different data type.
# 3)Tuples are immutable: Once a tuple is created, its contents cannot be changed. This means that you cannot add or remove elements from a tuple, or modify the values of its existing elements.
# 4)Tuples can contain duplicates: Like lists or arrays, tuples can contain multiple elements with the same value
# Regarding immutability, yes, tuples are immutable data structures. Once a tuple is created, its contents cannot be changed. This means that you cannot add or remove elements from a tuple, or modify the values of its existing elements. If you need to modify a tuple, you would need to create a new tuple with the updated values.
# 

# ##Question 2
# 
# What are the two tuple methods in python? Give an example of each method. Give a reason why 
# tuples have only two in-built methods as compared to Lists

# In[7]:


##1)count: This method returns the number of times a specific element appears in a tuple.
##2)index: This method returns the index of the first occurrence of a specific element in a tuple.

##Example: 1) count

tup1 = (1, 2, 3, 2, 4, 2, 5)
tuple1 =tup1.count(2)
print(tuple1)


# In[10]:


## example: 2) index

tup1 = (1, 2, 3, 2, 4, 2, 5)
tuple1 = tup1.index(4)
print(tuple1)


# The reason why tuples have only two built-in methods as compared to lists is because tuples are immutable data structures. Since tuples cannot be modified once they are created, there is no need for methods that modify the contents of a tuple, such as append, insert, remove, etc. The count and index methods are sufficient for working with tuples because they allow you to access and search the contents of a tuple without modifying it. In contrast, lists have many built-in methods for modifying their contents because they are mutable data structures.

# ##Question - 3
# 
# Which collection datatypes in python do not allow duplicate items? Write a code using a set to remove 
# duplicates from the given list.
# 
# 
# List = [1,1,1,2,1,3,1,4,2,1,2,2,2,3,2,4,3,1,3,2,3,3,3,4,4,1,4,2,4,3,4,4]

# In Python, sets are the collection datatypes that do not allow duplicate items. Here's an example code using a set to remove duplicates from the given list:

# In[16]:


my_list = [1,1,1,2,1,3,1,4,2,1,2,2,2,3,2,4,3,1,3,2,3,3,3,4,4,1,4,2,4,3,4,4]
my_set = set(my_list)
my_list = list(my_set)
print(my_list)


# ##Question -4 
# 
# Explain the difference between the union() and update() methods for a set. Give an example of 
# each method
In Python, sets have two different methods for combining sets: union() and update(). The main difference between the two methods is how they handle the original sets.
The union() method returns a new set that contains all the unique elements from two or more sets. The original sets are not modified by the union() method.
# In[18]:


## example - union() 
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = set1.union(set2)
print(set3)


# In this example, we use the union() method to combine set1 and set2 into a new set set3. The resulting set contains all the unique elements from set1 and set2, but neither set1 nor set2 is modified.
# 
# The update() method adds all the unique elements from one set to another set. Unlike the union() method, the original set is modified by the update() method.

# In[19]:


## example - update()
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.update(set2)
print(set1)


# In this example, we use the update() method to add all the unique elements from set2 to set1. The resulting set is stored in set1, and now contains all the unique elements from both sets. The original set1 set is modified by the update() method.
# 
# In summary, the union() method creates a new set containing all the unique elements from multiple sets, while the update() method modifies an existing set to include all the unique elements from another set.

# ##Question 5
# 
# What is a dictionary? Give an example. Also, state whether a dictionary is ordered or unordered

# In Python, a dictionary is a collection data type that stores key-value pairs. Each key in a dictionary is associated with a value, and the keys must be unique. Dictionaries are also known as associative arrays or hash tables in other programming languages.
# Here's an example of a dictionary in Python:

# In[21]:


my_dict = {'apple': 1, 'banana': 2, 'orange': 3}
print(my_dict)


# In this example, we have a dictionary with three key-value pairs: 'apple': 1, 'banana': 2, and 'orange': 3. The keys in this dictionary are strings ('apple', 'banana', and 'orange'), and the values are integers (1, 2, and 3).
# 
# Dictionaries in Python are unordered, meaning that the order of the key-value pairs is not guaranteed. When you access the elements of a dictionary, they may be returned in a different order than they were originally defined. If you need to maintain the order of the elements in a collection, you can use a list or a tuple instead of a dictionary.

# ##Question 6
#  
#  Can we create a nested dictionary? If so, please give an example by creating a simple one-level 
# nested dictionary

# Yes, we can create a nested dictionary in Python. A nested dictionary is simply a dictionary where the values are also dictionaries. Here's an example of a simple one-level nested dictionary:

# In[23]:


my_dict = {'apple': {'color': 'red', 'price': 0.5},
    'banana': {'color': 'yellow', 'price': 0.25},
    'orange': {'color': 'orange', 'price': 0.75}}
print(my_dict)


# In this example, we have a dictionary with three key-value pairs, where each value is also a dictionary. Each inner dictionary contains two key-value pairs: 'color' and 'price', which are both strings and floats, respectively. The outer dictionary has keys 'apple', 'banana', and 'orange', each of which corresponds to an inner dictionary containing information about the color and price of that fruit.

# ##Question 7 
#  
#  Using setdefault() method, create key named topics in the given dictionary and also add the value of 
# the key as this list ['Python', 'Machine Learning’, 'Deep Learning']

# In[2]:


# Given dictionary
dict1 = {'language': 'Python', 'course': 'Data Science Masters'}

# Using setdefault() method to add a new key-value pair
dict1.setdefault('topics', ['Python', 'Machine Learning', 'Deep Learning'])

# Printing the updated dictionary
print(dict1)


# ##Question 8
# 
# What are the three view objects in dictionaries? Use the three in-built methods in python to display 
# these three view objects for the given dictionary.
# 
# 
# dict1 = {'Sport': 'Cricket' , 'Teams': ['India', 'Australia', 'England', 'South Africa', 'Sri Lanka', 'New Zealand']}

# dict.keys() - Returns a view object that contains the keys of the dictionary.
# 
# dict.values() - Returns a view object that contains the values of the dictionary.
# 
# dict.items() - Returns a view object that contains the key-value pairs of the dictionary as tuples.
# 
# Here's a Python program that displays all three view objects for the given dictionary:

# In[3]:


dict1 = {'Sport': 'Cricket', 'Teams': ['India', 'Australia', 'England', 'South Africa', 'Sri Lanka', 'New Zealand']}


keys_view = dict1.keys()
values_view = dict1.values()
items_view = dict1.items()

# Display the view objects
print("View object for keys:", keys_view)
print("View object for values:", values_view)
print("View object for items:", items_view)


# In[ ]:




