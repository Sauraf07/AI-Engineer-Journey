'''
Variables
Input/Output
'''
Name = 'Saurav'
age = 20
print(Name)
print(age)

# This is called snake case:
my_name = 'Saurav'
my_age = 20

# In Python, comments start with a pound symbol (#), and the language ignores everything after the # symbol on that line:
# This is a comment

# Multi-line comments can be created by using consecutive single-line comments:
# This is a multi-line comment
# that spans multiple lines


print("Hello World")
print('My favorite colors are', 'blue', 'green', 'red')



'''Here are the most common data types you'll use in Python:

Integer: A whole number without decimals, for example, 10 or -5.'''
my_integer_var = 10
print('Integer:', my_integer_var) # Integer: 10
'''Float: A number with decimals, for example, 3.14 or -0.001.'''
my_float_var = 3.14
print('Float:', my_float_var) # Float: 3.144
'''String: A sequence of characters enclosed in quotes, for example, "Hello" or 'Python'.'''
my_string_var = "Hello, Python!"
print('String:', my_string_var) # String: Hello, Python!
'''Boolean: A value that can be either True or False.'''
my_boolean_var = True
print('Boolean:', my_boolean_var) # Boolean: True
# ============================================================
# Set: An unordered collection of unique elements, like {0.5, 4, 'apple'}.
my_set_var = {7, 'hello', 8.5}
print('Set:', my_set_var) # Set: {7, 'hello', 8.5}
# Dictionary: A collection of key-value pairs enclosed in curly braces, like {'name': 'John Doe', 'age': 28}.
my_dictionary_var = {'name': 'Alice', 'age': 25}
print('Dictionary:', my_dictionary_var) # Dictionary: {'name': 'Alice', 'age': 25}
# Tuple: An immutable ordered collection, enclosed in parentheses, like ('apple', 4.5, 7).
my_tuple_var = (7, 'hello', 8.5)
print('Tuple:', my_tuple_var) # Tuple: (7, 'hello', 8.5)
# Range: A sequence of numbers, often used in loops, for example, range(5).
my_range_var = range(5)
print('Range:', my_range_var) # Range: range(0, 5)
# List: An ordered collection of elements that supports different data types.
my_list = [22, 'Hello world', 3.14, True]
print(my_list) # [22, 'Hello world', 3.14, True]
# None: A special value that represents the absence of a value.
my_none_var = None
print('None:', my_none_var) # None: None
# In future lessons, you will learn more about how to work with all of these data types.



my_integer_var = 10
print(type(my_integer_var))  # <class 'int'>

my_float_var = 4.50
print(type(my_float_var))  # <class 'float'>

my_string_var = 'hello'
print(type(my_string_var))  # <class 'str'>

my_boolean_var = True
print(type(my_boolean_var))  # <class 'bool'>

my_set_var = {7, 'hello', 8.5}
print(type(my_set_var))  # <class 'set'>

my_dictionary_var = {'name': 'Alice', 'age': 25}
print(type(my_dictionary_var))  # <class 'dict'>

my_tuple_var = (7, 'hello', 8.5)
print(type(my_tuple_var))  # <class 'tuple'>

my_range_var = range(5)
print(type(my_range_var))  # <class 'range'>

my_list = [22, 'Hello world', 3.14, True]
print(type(my_list)) # <class 'list'>

my_none_var = None
print(type(my_none_var))  # <class 'NoneType'>