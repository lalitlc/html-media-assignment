#!/usr/bin/env python
# coding: utf-8

# ## 3rd Feb Assignment

# ```
# Q1. Which keyword is used to create a function? Create a function to return a list of odd numbers in the range of 1 to 25.
# 
# Ans. 'def' keyword is used to create a fuction.
# ```

# In[1]:


def odd_num():
    odds = []
    for i in range(1,26):
        if i%2 != 0:
            odds.append(i)
    return odds


# In[2]:


odd_num()


# ---

# ```
# Q2. Why *args and **kwargs is used in some functions? Create a function each for *args and **kwargs to demonstrate their use.
# 
# Ans. *args and **kwargs are used in functions to pass a variable number of arguments to the function.
# 
# *args is used to send a non-keyworded variable length argument list to the function. It allows the function to receive a dynamic number of non-keyword arguments, and these arguments are packed into a tuple.
# 
# **kwargs allows a keyworded, variable-length argument list. It passes keyworded variable length of arguments to a function. The arguments are passed in the form of key-value pairs and packed into a dictionary.
# ```

# In[3]:


# Example

def test_func(*args, **kwargs):
    print("This is a test function")
    print("Non-keyworded arguments:", args)
    print("Keyworded arguments:", kwargs)


# In[4]:


# Call the function with non-keyworded and keyworded arguments

test_func(1, 2, 3, 4, 5, name="Yogesh", age=21)


# ---

# ```
# Q3. What is an iterator in python? Name the method used to initialise the iterator object and the method used for iteration. Use these methods to print the first five elements of the given list [2, 4, 6, 8, 10, 12, 14, 16, 18, 20].
# 
# Ans. An iterator in Python is an object that implements the iterator protocol. It must define two methods: __iter__() and __next__(). __iter__() returns the iterator object itself and the __next__() method returns the next item from the sequence of elements.
# 
# Here's an example of how you can use the iter() method to initialize the iterator object and the next() method to iterate over the elements:
# ```

# In[5]:


l = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
it = iter(l)

for i in range(5):
    print(next(it))


# ---

# ```
# Q4. What is a generator function in python? Why yield keyword is used? Give an example of a generator function.
# 
# Ans. A generator function in Python is a special type of function that returns a generator iterator. It uses the yield keyword instead of return to return multiple values one at a time, instead of all at once.
# 
# The yield keyword is used to return a value from the generator function and pause its execution. When the function is called again, it resumes execution immediately after the yield statement. This allows the generator function to generate an iterable sequence of values, which can be iterated over in a for loop or using the next() method.
# 
# Here's an example of a generator function that generates the sequence of numbers from 0 to n:
# ```

# In[6]:


def generator_function(n):
    i = 0
    while i < n:
        yield i
        i += 1


# In[7]:


gen = generator_function(5)
for i in gen:
    print(i)


# ---

# ```
# Q5. Create a generator function for prime numbers less than 1000. Use the next() method to print the first 20 prime numbers.
# ```

# In[8]:


# Q5 Answer
def prime_number():
    for n in range(1,1000):
        for i in range(2,n):
            if(n%i==0):
                break
        else:
            yield n     


# In[9]:


prime_gen = prime_number()
for i in range(21):
    print(next(prime_gen))

