# function to find sqaure of a number

# def findSqaure(num):
#     # square of that number
#     return num * num

# # lambda version of this function

# square = lambda num: num * num

# print(square(4))
# print(findSqaure(5))

# # function to add three numbers
# # anynymous functions are those functions that do not have a name
# sum = lambda num1, num2, num3: num1 + num2 + num3

# print(sum(10, 10, 10))


# Functions can be used in the following ways:
# 1) Function can be stored in a variable
# 2 ) Function can be passed as parameters to other functions
# 3) Functions can be returned from other functions also
# 4 functions can be stored in a list, dictionary, etc

# example:
# def greet():
#     return "Welcome"

# # store it in variable
# my_greet = greet

# print(type(my_greet))
# print(my_greet())

# def greet():
#     return "Welcome"
# #  second function
# def greetWithName(func, name):
#     return func() + " " + name

# print(greetWithName(greet, "John Doe"))


# def outer_greet():
#     def inner_greet():
#         return "Hello and Welcome!"
#     return inner_greet

# result = outer_greet()
# print(result())

# def add(num1, num2):
#     return num1 + num2

# def subtract(num1, num2):
#     return num1 - num2

# operations = {
#     "sum" : add,
#     "difference" : subtract
# }

# print(operations["sum"](10, 10))
# print(operations["difference"](100, 90))

# storing both functions in a list
# operations = [add, subtract]
# # index.      0      1
# print(operations[0](2, 2))
# print(operations[1](100, 10))


# Higher Order Function
def process(func, userText):
    return func(userText)

# function to be passed ar an argument - helper function
def to_upper(text):
    return text.upper()

print(process(to_upper, "john doe"))