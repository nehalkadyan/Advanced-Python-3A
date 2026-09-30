# operations
# read
# write
# append
# binary operations

# open(file-path, mode)
#modes -> r, w, a, b
# r - read
# w - write
# a - append
# b - binary

# reading from a text file
# file = open("sample.txt", "r")

# content = file.read()
# print(content)

# reading certain portion of the file

# file = open("sample.txt", "r")
# # number of letters you want to get from the text file
# content = file.read(10)

# print(content)

# open(filepath) -> also means read mode
# open(filepath, "r") -> also means read mode
# file = open("sample.txt")

# content = file.read()
# print(content)

# to read only the first line from the text file

# file = open("sample.txt", "r")

# content = file.readline()
# print(content)

# to read all the files from the text

# file2 = open("sample.txt", "r")

# content2 = file2.read()
# print(content2)

# to get all the lines from the text file in a list

# file = open("sample.txt", "r")
# content = file.readlines()

# print(content)

# write mode - w

# open the file
# file = open("sample.txt", "w")

# # writing new content to the file
# file.write("This is my new content in sample file!!!!!!!!!")
# file.write("\nAdding more content")
# file.write("\nAdding extra content.")

# # close the file
# file.close()

# file = open("sample.txt", "w")
# file.write("hi")


# append mode

# open the file

# file = open("sample.txt", "a")

# file.write("\nLine 3")

# # close the file
# file.close()

# binary mode - b

# Images - jpg, jped, png
# Audio - mp3,
# .csv
# Videos - mp4

# work with image file (jpg format)

# relative path
# file = open("mobile.jpg", "rb")

# # read the content from the image file
# data = file.read()

# print(data)

# file.close()

# write this data in a new file to create copy of this image

# If the file does not exist, then write mode will create the file for you
# file = open("students.txt", "w")
# file.write("Hello")


# Task : Copy the file content from mobile.jpg
# and put it's content in a new file to create a replica of the
# image

# open the mobile.jpg in read mode and get it's data

sourceImg = open("mobile.jpg", "rb")

# get the byte data from sourceImg
data = sourceImg.read()

# Create a new file and write "data" into it
#  wb - write binary mode
destinationImg = open("replicaImage.jpg", "wb")

# write new data to this replicaImage.jpg
destinationImg.write(data)

# close both files
sourceImg.close()
destinationImg.close()




