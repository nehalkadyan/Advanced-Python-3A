# itertools is a built in python module that lets you perform operations
# on iterators using it's functions
import itertools
# count
# counter = itertools.count(4)

# for count in counter:
#     if count > 15:
#         break
#     print(count)
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(f"counter : {counter}")


# list = [1,2,3,4,5,6]
# # next()

# for num in list:
#     print(num)

# count goes till infinity if you don't put any check or break statement
# you can also make it jump some elements by providing second argument
# argument 1 = where to start from
# argument 2 = how many elements to jump

# iterator
my_counter = itertools.count(5, 3)

print(type(my_counter))

for count in my_counter:
    if count > 15:
        break
    print(count)

# print(next(my_counter))
# print(next(my_counter))
# print(next(my_counter))
# print(next(my_counter))



