# A generator is a special type of Python function that uses yield to
# produce values one at a time. Each time yield is reached,
# the function pauses its execution and remembers its state. 
# When the next value is requested, it resumes from where it paused.
# This allows values to be processed one at a time instead of creating
# and storing all values in memory at once.

# example 1
# get users from database

# import time

# def get_users_from_db():
#     # mock users list
#     users = ["user 1", "user 2", "user 3", "user 4", "user 5"]

#     for user in users:
#         time.sleep(2)
#         print(f"fetching user : {user}")
        
# get_users_from_db

# using generator function

import time
# generator function / producer function
def get_users_from_database():
    # mock list
    users = ["user 1", "user 2", "user 3", "user 4", "user 5"]

    for user in users:
        time.sleep(2)
        yield user


# consumer function
def sendMail():
    # generator object
    user_generator = get_users_from_database()

    # iterating over the generator

    for user in user_generator:
        print(f"sending mail to user : {user}")
        time.sleep(2)
        print(f"Mail sent to user : {user}")

sendMail()









