import classes
from database import studentList

def addNewStudent():
    userInput1 = int(input("Add new student's ID: "))
    if userInput1 < 1000 and userInput1 > 99:
        userInput2 = input("Add new student's name: ")
        userInput3 = input("Add new student's surname: ")
        userInput4 = input("Add new student's email address: ")
        if userInput4.__contains__("@"):
            userInput5 = input("Add new student's phone number: ")
            if str(userInput5[0:4])==str("+994"):
                newStudent = classes.Student(userInput1, userInput2, userInput3, userInput4, userInput5)
                studentList.append(newStudent)
            else:
                print("Unavailable number added, please try again")
        else:
            print("Unavailable email adress added, please try again")
    else:
        print("Student ID number should be between 100 and 1000, please try again")

def deleteByStudentCode():
    userInput = int(input("Add Student's ID which you want to delete: "))
    for studInfo in studentList:
        if studInfo.kod == userInput:
            studentList.remove(studInfo)

def editByStudentCode():
    userInput = int(input("Add Student's ID which you want to edit: "))
    for studInfo in studentList:
        if studInfo.kod == userInput:
            studInfo.kod = int(input("Yeni Kod:"))
            studInfo.ad = int(input("New Name:"))
            studInfo.soyad = int(input("New Surname:"))
            studInfo.email = int(input("New Email:"))
            studInfo.number = int(input("New Phone Number:"))

def showStudentInfoByName():
    userInput = input("Add Student's name you want to search:")

    for stud in studentList:
        if stud.ad == userInput:
            stud.showStudents()
            break
        else:
            print("There is not such a student")

def showAllStudents():
    for students in studentList:
        students.showStudents()

def start():
    x = 1
    while x > 0:
        print("1. Add new Student")
        print("2. Delete by code")
        print("3. Edit by code")
        print("4. Show by name")
        print("5. Show all students")

        userInput = int(input("Choose the number: "))

        if userInput == 1:
            addNewStudent()
        elif userInput == 2:
            deleteByStudentCode()
        elif userInput == 3:
            editByStudentCode()
        elif userInput == 4:
            showStudentInfoByName()
        elif userInput == 5:
            if len(studentList) == 0:
                print("There is no any registered student. Please press 1 and enter for adding new student.")
            showAllStudents()
        else:
            print("Error Typo")
