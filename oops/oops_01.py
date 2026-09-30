# how to create class (syntax)

class Student:
    # constructor
    def __init__(self, name, course, age, roll_number):
        self.name = name
        self.course = course
        self.age = age
        self.roll_number = roll_number

    # methods

    def displayDetails(self):
        print(f"Name : {self.name}")
        print(f"course : {self.course}")
        print(f"age : {self.age}")
        print(f"Roll number : {self.roll_number}")

student1 = Student("John Doe", "B.Tech", 20, "32653526536")

student1.displayDetails()

    


