#!/usr/bin/env python
# coding: utf-8

# # QUESTION 1️ : Explain Class and Object with respect to Object-Oriented Programming. Give a suitable example.

# In[1]:


''' Ans. In Python, classes and objects are the fundamental building blocks of Object-Oriented Programming (OOP). 
A class is a blueprint or template for creating objects, which are instances of the class. 
An object is a specific instance of a class that can have its own unique state and behavior.

To create a class in Python, we use the class keyword followed by the name of the class. 
The class definition can contain variables, methods, and other attributes that define the behavior and properties of the objects that will be created from it.

Below is an example of a class named Person: '''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def SayHello(self):
        print("Hi, my name is " + self.name + " :) and I am " + str(self.age) + " years old.")
        print()

''' In this example, the Person class has two attributes name and age, and one method SayHello() that prints a greeting message.
We need to convert the variable self.age into string because age is a number and we can only concatenate string to string, not int to string.


> Now, to create an object from the Person class, we use the class name followed by parentheses to call its constructor method (__init__()): '''

person1 = Person("vinay", 21)
person2 = Person("jivan", 21)

'''In this example, person1 and person2 are two different objects created from the Person class, each with their own unique name and age attributes.


> Now, to call a method on an object, we use dot notation and call the method like this: '''

person1.SayHello()
person2.SayHello()

Explanation_1  = '''In summary, a class is a template for creating objects, and an object is a specific instance of a class that has its own unique state and behavior. 
We can create multiple objects from a single class, and each object can have its own values for the attributes defined in the class. '''

print(Explanation_1)


# # QUESTION 2️ : Name the four pillars of OOPs.

# In[66]:


''' Ans. The four pillars of Object Oriented Programming (OOPs) are: '''

Explanation_2 = ''' 1. Encapsulation: Encapsulation is the practice of hiding internal details of an object and only exposing a public interface. 
This helps to prevent accidental modification of internal data and ensures that objects are used correctly by external code.

2. Inheritance: Inheritance is the process by which a new class is created from an existing class, inheriting all the attributes and methods of the parent class. 
This allows for code reuse and allows for more specific classes to be created from more general ones.

3. Polymorphism: Polymorphism is the ability of objects to take on many forms or have multiple behaviors. 
In OOPs, polymorphism is often achieved through method overriding and method overloading.

4. Abstraction: Abstraction is the practice of focusing on essential features of an object and ignoring its non-essential or implementation details. 
It allows for complex systems to be modeled in a simpler way and makes code easier to understand and maintain. '''

print(Explanation_2)


# # QUESTION 3️ : Explain why the `__init__()` function is used. Give a suitable example.

# In[67]:


''' Ans. In Python, the __init__() function is a special method that is called when an object is created from a class. 
It is used to initialize the attributes of the object with the values passed to it as arguments. 
The self parameter in the __init__() method refers to the object being created, and is used to set the object's attributes.

Below is the example of a class that uses the __init__() function: '''

class bank_account :

    def __init__(self, balance):            # Private function
        self.__balance = balance            # we have used double underscore here in variable "self.__balance" , that's why function is private and hidden from the user.
    
    def deposit(self, deposit_amount):      # Public function
        self.__balance = self.__balance + deposit_amount
        print("You have successfully Deposited the amount :", deposit_amount, " Rs.  | Your available Balance is :", self.__balance, " Rs.")
        print()

    def withdraw(self, withdraw_amount):    # Public function
        if self.__balance >= withdraw_amount :
            self.__balance = self.__balance - withdraw_amount
            print("You have successfully Withdrawn the amount :", withdraw_amount, " Rs.  | Your remaining Balance is :", self.__balance, " Rs.")
        else :
            return "Oops! You have not enough amount to withdraw. Try again !!!"
    
    def get_balance(self):                  # Public function
        print("Your Account Balance is :", self.__balance, " Rs.")
        print()


# Creating object of the class name 'bank_account' :
puru = bank_account(1000)


# Calling methods :
puru.get_balance()
puru.deposit(5000)
puru.withdraw(1500)


# # QUESTION 4️  : Why self is used in OOPs?

# In[68]:


Explanation_4 = '''In object-oriented programming (OOP), self is a special parameter that is used to refer to the current instance of a class. 
It is used to access the attributes and methods of an object within the class, as well as to create new attributes and methods for that object.

In Python, when a method is called on an instance of a class, the instance is automatically passed to the method as the first argument. 
This is why all instance methods in Python take self as their first parameter.

In summary, self is used in OOP to refer to the current instance of a class and access its attributes and methods. 
It allows for multiple instances of a class to have their own values for the same attributes and methods, and enables the creation of more flexible and powerful object-oriented programs. '''

print(Explanation_4)


# # QUESTION 5️ : What is inheritance? Give an example for each type of inheritance.

# In[69]:


Explanation_5 = '''Inheritance is a fundamental concept in object-oriented programming (OOPs) that allows for the creation of new classes based on existing classes.
Inheritance allows the new class to inherit all the attributes and methods of the existing class, and then add its own unique attributes and methods.

> There are five types of inheritance :

1. Single Inheritance: In this type of inheritance, a class inherits properties and methods from a single parent class.

2. Multiple Inheritance: In this type of inheritance, a class inherits properties and methods from multiple parent classes.

3. Multilevel Inheritance: In this type of inheritance, a class inherits properties and methods from a parent class, which in turn inherits properties and methods from its parent class.

4. Hierarchical Inheritance: In this type of inheritance, multiple classes inherit properties and methods from a single parent class.

5. Hybrid Inheritance: This type of inheritance combines multiple types of inheritance, such as multiple and multilevel inheritance, to create a more complex class hierarchy.

Please find below the examples of each type of Inheritance : 
'''

print(Explanation_5)

# Single Inheritance -->
class ParentClass :
    def test_meth(self) :
        return "1. This is an example of Single Inheritance. \n(Please check cell comment '# Single Inheritance' for the code)"
    
class ChildClass(ParentClass):
    pass

obj_child_class = ChildClass()
print(obj_child_class.test_meth())
    

# Multiple Inheritance -->
class class1 :
    def test_class1(self):
        print()
        return "2. This is an example of Multiple Inheritance \n(Please check cell comment '# Multiple Inheritance' for the code) \n--> This is class 1"

class class2 :
    def test_class2(self):
        return "--> This is class 2"

class class3(class1, class2):
    pass

obj_class3 = class3()
print(obj_class3.test_class1())
print(obj_class3.test_class2())


# Multilevel Inheritance -->
class class1 :
    def test_class1(self):
        print()
        return "3. This is an example of Multilevel Inheritance \n(Please check cell comment '# Multilevel Inheritance' for the code) \n--> This is a method from class 1"
    
class class2(class1) :
    def test_class2(self):
        return "--> This is a method from class 2"

class class3(class2) :
    pass

obj_class3 = class3()
print(obj_class3.test_class1())
print(obj_class3.test_class2())


# Hierarchical Inheritance -->
class class1 :
    def test_class1(self):
        print()
        return "4. This is an example of Hierarchical Inheritance \n(Please check cell comment '# Hierarchical Inheritance' for the code)"
    
class class2(class1) :
    def test_class2(self):
        return "--> This is a method from class 2"

class class3(class1) :
    def test_class3(self):
        return "--> This is a method from class 3"

obj_class2 = class2()
print(obj_class2.test_class1())
print(obj_class2.test_class2())

obj_class3 = class3()
print(obj_class3.test_class1())
print(obj_class3.test_class3())


# Hybrid Inheritance -->
class class1 :
    def test_class1(self):
        print()
        return "5. This is an example of Hybrid Inheritance \n(Please check cell comment '# Hybrid Inheritance' for the code)"
    
class class2:
    def test_class2(self):
        return "--> This is a method from class 2"

class class3(class1, class2) :
    def test_class3(self):
        return "--> This is a method from class 3"

class class4(class3):
    def test_class4(self):
        return "--> This is a method from class 4"
    
obj_class4 = class4()
print(obj_class4.test_class1())
print(obj_class4.test_class2())
print(obj_class4.test_class3())
print(obj_class4.test_class4())

