"""
Test File 



"""
no_of_students = int(input("Enter the number of students"))

file = open("names.txt", "a")


for i in range(no_of_students):

    names = input("What is your name")

    file.write(names)
    file.write("\n")

    file.close()
