# Decorator is a fucntion that takes a function as an argument
# and returns a new function. It does not modify the original
# functionn that it takes but returns a modified result

def operartion(func):
    def wrapper():
        print("Start")
        # printHello()
        func()
        print("End")
    
    return wrapper

@operartion
def printHello():
    print("Hello World!")

printHello()

# result = operartion(printHello)

# print(result)
# result()

# greeting = decorator(printHello) 
# # greeting = wrapper()

# greeting()
# Output 
# Start
# Hello World
# End



# def calculateSum(num1, num2):
#     print(f"sum is : {num1 + num2 }")

# calculateSum(5, 10)



