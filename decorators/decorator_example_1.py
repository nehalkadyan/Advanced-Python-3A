# import time module
import time

# decorator function
def calculateExecutionTime(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"execution time : {end - start} seconds")

    return wrapper

# function to upload marks
@calculateExecutionTime
def uploadMarks():
    print("Uploading Marks...")
    print("Marks uploaded!")

uploadMarks()

@calculateExecutionTime
def markAttendance():
    print("Marking Attendance...")
    print("Attendance Marked!")

markAttendance()

@calculateExecutionTime
def getAllUsers():
    print("Fetching users from database ....")
    print("Users fetched!")

getAllUsers()