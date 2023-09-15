#!/usr/bin/env python
# coding: utf-8

# # QUESTION : 1

# In[1]:


''' Ques 1. Who developed Python Programming Language ?

Ans. Python programming language was developed by Guido van Rossum in the late 1980s, and its first public release was in 1991. Guido van Rossum named it after the British comedy group Monty Python. '''


# # QUESTION : 2

# In[2]:


''' Ques 2. Which type of programming does Python support ?

Ans. Python supports multiple programming paradigms, including object-oriented, functional, procedural, and aspect-oriented programming.
This makes it a versatile language that can be used for a variety of tasks, from web development to scientific computing, machine learning, and data analysis.
It also has a simple and easy-to-learn syntax, making it an ideal language for beginners to start with. '''


# # QUESTION : 3

# In[3]:


''' Ques 3. Is python case sensitive when dealing with identifiers ?

Ans. Yes, Python is case-sensitive when dealing with identifiers. This means that uppercase and lowercase letters are considered different in Python.

For example, the variable names "my_variable" and "My_Variable" would be considered two different variables in Python.
It's important to be consistent with our naming conventions to avoid errors when working with identifiers in Python. '''


# # QUESTION : 4

# In[4]:


''' Ques 4. What is the correct extension of the Python file ?

Ans. The correct extension of a Python file is ".py". When we save a Python script or program, we should give it a name and save it with the ".py" extension.

For example, if we have a Python script called "my_script", then we should save it as "my_script.py". This extension helps to identify the file as a Python script and allows the Python interpreter to recognize and execute it properly. '''


# # QUESTION : 5

# In[5]:


''' Ques 5. Is Python Code compiled or Interpreted ?

Ans. Python code is interpreted, which means that the source code is executed directly by the Python interpreter without being compiled into machine code beforehand. When we run a Python program, the interpreter reads the code line by line and executes each line as it goes. This makes the development process faster because we don't need to compile our code before running it.
However, this also means that Python can be slower than compiled languages like C++ for certain types of tasks. To address this issue, there are tools like PyPy and Numba that can speed up certain parts of Python code by using just-in-time (JIT) compilation or other techniques. '''


# # QUESTION : 6

# In[6]:


''' Ques 6. Name few blocks of code used to define in Python language ?

Ans. In Python, code blocks are defined using indentation rather than braces or other delimiters. The following are some of the most common types of code blocks used in Python:

1. Function blocks: Functions in Python are defined using the "def" keyword, followed by the function name and its arguments. The code block for the function is indented under the function definition and the code should be executed when the function is called.
For example:
def my_function(argument1, argument2):

2. Conditional blocks: Conditional statements in Python, such as "if", "elif", and "else", are used to execute different code blocks based on the result of a Boolean expression. The code block for each branch of the conditional is indented under the relevant keyword.
For example:
if x > 0:
# Code to be executed if x is greater than 0
elif x == 0:
# Code to be executed if x is equal to 0
else:
# Code to be executed if x is less than 0

3. Loop blocks: Loops in Python, such as "for" and "while", are used to execute a block of code repeatedly. The code block for the loop is indented under the loop definition.
For example:
for i in range(10):
# Code to be executed for each value of i in the range 0 to 9

while x > 0:
# Code to be executed as long as x is greater than 0

4. Class blocks: Classes in Python are defined using the "class" keyword, followed by the class name and any base classes. The code block for the class is indented under the class definition.

5. With blocks: The "with" statement in Python is used to manage resources like files, sockets, and locks, and ensures that they are properly closed or released when the block is exited. The code block for the "with" statement is indented under the statement itself.

These are just a few examples of code blocks used in Python. There are many other types of blocks, such as try/except blocks for handling errors among others. '''


# # QUESTION : 7

# In[7]:


# Ques 7. State a character used to give single-line comments in Python ?

''' Ans. In Python, the # character is used to give single-line comments. Any text that appears after the # symbol on a line is considered a comment and is ignored by the Python interpreter.

For example:
# I have used single line comment in this question statement.

Single-line comments are useful for providing context and explanations for our code, as well as temporarily disabling or commenting out lines of code for testing or debugging purposes. '''


# # QUESTION : 8

# In[8]:


''' Ques 8. Mention functions which can help us to find the version of python that we are currently working on ?

Ans. In Python, there are several ways to find the version of the Python interpreter that we are currently working on. Below are a few examples of functions that can help us to accomplish this:

1. sys.version - This function returns a string containing the version number of the Python interpreter, as well as additional information about the build.
We can use it like this:

import sys
print(sys.version)
Output:
3.10.9 | packaged by Anaconda, Inc. | (main, Mar  1 2023, 18:18:15) [MSC v.1916 64 bit (AMD64)]

2. platform.python_version() - This function returns a string containing the version number of the Python interpreter, without any additional information.
We can use it like this:

import platform
print(platform.python_version())
Output:
3.10.9

3. sys.version_info - This function returns a tuple containing detailed information about the version of the Python interpreter, including the major and minor version numbers, as well as the micro and release level numbers.
 We can use it like this:

import sys
print(sys.version_info)
Output:
sys.version_info(major=3, minor=10, micro=9, releaselevel='final', serial=0)

These are just a few examples of functions that can help us find the version of Python that we are currently working on ! '''


# # QUESTION : 9

# In[9]:


''' Ques 9. Python supports the creation of anonymous functions at runtime, using a Construct called ........

Ans. Python supports the creation of anonymous functions at runtime, using a construct called "lambda" or "lambda function". The lambda function is a small, anonymous function that can have any number of arguments, but can only have one expression. It is defined using the lambda keyword, followed by the function's arguments and the expression to be evaluated. Below is an example of a lambda function that takes two arguments and returns their sum:

add = lambda x, y: x + y
result = add(3, 4)
print(result)
# Output: 7

Lambda functions are commonly used as arguments to higher-order functions like map(), filter(), and reduce(). They can also be used as a quick way to define simple functions without giving them a name. '''


# # QUESTION : 10

# In[10]:


''' Ques 10. What does pip stand for python ?

Ans. In Python, pip stands for "Pip Installs Packages" or "Pip Installs Python". It is a package manager that is used to install and manage software packages (also known as "libraries" or "modules") written in Python. pip is included with most Python installations, and is used to download and install packages from the Python Package Index (PyPI) and other sources.
Using pip, we can install, upgrade, and remove Python packages, as well as list installed packages and their dependencies.

For example, to install the popular NumPy package using pip, we can use the following command:
pip install numpy

This will download and install the latest version of NumPy and its dependencies. We can then import NumPy in our Python code and use its functions and classes. '''


# # QUESTION : 11

# In[1]:


''' Ques 11. Mention a few built-in functions in python ?

Ans. Python provides a large number of built-in functions that are always available to use in any Python program.
Below are a few examples of some commonly used built-in functions in Python :

1. print() - This function is used to print output to the console or terminal. It can be used to print text strings, numbers, variables, and more.
For example:
print("Hello Mentor ! \n Nice to meet you Sir ^.^ ")

2. len() - This function is used to get the length of a string, list, tuple, or other iterable object.
For example:
my_list = [1, 2, 3, 4, 5]
print(len(my_list))
# Output : 5

3. input() - This function is used to get input from the user via the console or terminal. It can be used to prompt the user for text or numerical input.
For example:
name = input("What is your name : ?")
print("Hello, " + name + "!")

4. type() - This function is used to get the type of an object in Python. It can be used to check the type of a variable or value.
For example:
x = 5
print(type(x))
# Output : <class 'int'>

5. range() - This function is used to generate a range of numbers, which can be used in for loops or other iterations.
For example:
for i in range(1, 6):
    print(i)
# Output:
1
2
3
4
5

These are just a few examples of the many built-in functions available in Python. '''


# # QUESTION : 12

# In[12]:


''' Ques 12. What is the maximum possible length of an identifier in Python ?

Ans. In Python, the maximum possible length of an identifier (i.e., a variable name, function name, etc.) is technically unlimited. However, it is generally recommended to keep identifier names reasonably short and descriptive, to make the code more readable and easier to understand.

According to the official Python documentation, an identifier can be any length and can consist of letters (uppercase and lowercase), digits, and underscores (_). However, it must begin with a letter or underscore, and it cannot be a reserved keyword (such as if, while, def, etc.) or a built-in function or module name (such as print, str, list, etc.).

Below is an example of a valid Python identifier with a long name:
this_is_a_very_long_and_descriptive_variable_name = 16
type(this_is_a_very_long_and_descriptive_variable_name)
# Output : int

However, using such a long identifier can make the code harder to read and write, so it is generally recommended to keep identifiers shorter and more concise, while still being descriptive enough to convey their meaning. '''


# # QUESTION : 13

# In[13]:


''' Ques 13. What are the benefits of using Python ?

Ans. This question can not be answered in just a single line or few because Python is a very popular programming language that is used in a wide variety of applications, from web development and data analysis to scientific computing and artificial intelligence.

Below I am explaining some of the most significant advantages of using Python :

1. Easy to learn and use: Python has a simple syntax that is easy to read and write, making it a great language for beginners. It also has a large standard library with many pre-built functions and modules, making it easier to write complex programs with less code.

2. High-level language: Python is a high-level language, which means that it abstracts away many low-level details of the computer system, making it easier to focus on the problem being solved rather than the implementation details.

3. Cross-platform: Python is a cross-platform language, which means that it can run on many different operating systems, including Windows, macOS, and Linux.

4. Large community and ecosystem: Python has a large and active community of developers, who have contributed many third-party packages and modules that extend the language's capabilities. This means that there are many resources available for learning and using Python.

5. Versatile: Python is a versatile language that can be used for many different purposes, including web development, scientific computing, data analysis, artificial intelligence, machine learning, and more.

6. Interpreted language: Python is an interpreted language, which means that it can execute code without the need for a compiler. This makes it easier to develop and test code quickly.

7. Open-source: Python is an open-source language, which means that the source code is freely available and can be modified and distributed by anyone. This encourages collaboration and innovation within the community.

Overall, Python's ease of use, versatility, and large ecosystem make it a popular choice for a wide range of applications and industries, from education and research to finance and technology. '''


# # QUESTION : 14

# In[14]:


''' Ques 14. How is memory managed in python ?

Ans. Memory management in Python is handled by the Python interpreter, which uses a technique called reference counting. In reference counting, the interpreter keeps track of the number of references to each object in memory, and when an object's reference count reaches zero, it is automatically deleted.

However, reference counting alone is not enough to handle all memory management needs, particularly when dealing with circular references (i.e., two or more objects that reference each other). To handle circular references, Python also uses a technique called garbage collection.

Garbage collection is a process by which the interpreter periodically searches for and deletes any objects that are no longer being used by the program. This process is triggered automatically when the Python interpreter detects that the available memory is running low, or when the program explicitly requests a garbage collection using the gc.collect() function.

In addition to reference counting and garbage collection, Python also provides several tools and libraries for managing memory, including:

The sys.getsizeof() function, which returns the size of an object in memory.
The tracemalloc module, which allows you to trace memory usage and identify memory leaks in your program.
The gc module, which provides control over garbage collection settings and behavior.

Overall, Python's automatic memory management system makes it easy to write programs without worrying about low-level memory management details, while still providing efficient and effective memory usage and designed to be automatic and transparent to the user, while still providing some control and flexibility when needed. '''


# # QUESTION : 15

# In[15]:


''' Ques 15. How to install Python on windows and set path variables ?

Ans. Below are the steps to install Python on Windows and set path variables :

Download Python: Go to the official Python website at https://www.python.org/downloads/ and download the latest version of Python for Windows. Now we need to choose the appropriate installer based on the system architecture (32-bit or 64-bit) and the version of Python we want to install.

Run the installer: Once we have downloaded the installer, double-click on it to run it. We need to follow the on-screen instructions to install Python on your system. Choose the options which we want to install and the location where we want to install Python.

Add Python to PATH: By default, Python is installed in the C:\PythonXX folder (where XX is the version number), which is not added to the PATH environment variable. To add Python to the PATH, we need to follow the below steps:

a. Right-click on "This PC" and select "Properties".

b. Click on "Advanced system settings".

c. Click on "Environment Variables".

d. Under "System Variables", scroll down and find "Path" and click "Edit".

e. Click "New" and enter the path to the Python installation directory, for example, C:\PythonXX or C:\PythonXX\Scripts (where XX is the version number). Click "OK" to close all the windows.

Verify the installation: Open a Command Prompt and type python. If the installation was successful, then we should see the Python interpreter prompt, which looks like >>>. You can exit the interpreter by typing exit().

Congratulations, we have successfully installed Python on Windows and set the PATH variables. '''


# # QUESTION : 16

# In[16]:


''' Ques 16. Is indentation required in python ?

Ans. Yes, indentation is required in Python. Unlike other programming languages that use curly braces or keywords to denote code blocks, Python uses whitespace indentation to group statements into code blocks.

In Python, a block of code is defined by its indentation level. All statements within the same block must have the same indentation level. The standard indentation level in Python is four spaces, although we can use a different number of spaces or a tab character, as long as we are consistent.

Here's an example of a code block in Python using indentation :
if x > 0:
    print("x is positive")
else:
    print("x is zero or negative")

In this example, the if statement and the else statement are in different code blocks. The if block is indented with four spaces, and the else block is also indented with four spaces.

Indentation in Python is important for maintaining readability and consistency in our code. It also helps to avoid errors that can occur when mixing different indentation styles or when using the wrong number of spaces.

So, it is important to maintain the correct indentation in Python to ensure the correct execution of the code. '''


# In[ ]:




