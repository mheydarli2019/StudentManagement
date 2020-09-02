studentList = []

class Student:
    def __init__(self, kod, ad, soyad, email, number):
        self.kod = kod
        self.ad = ad
        self.soyad = soyad
        self.email = email
        self.number = number

    def showStudents(self):
        print(f"Kod: {self.kod} , Ad: {self.ad}, Soyad: {self.soyad} , Email: {self.email}, Number: {self.number}")




def addNewStudent():
    userInput1 = int(input("Add new student's ID: "))
    userInput2 = input("Add new student's name: ")
    userInput3 = input("Add new student's surname: ")
    userInput4 = input("Add new student's email address: ")
    userInput5 = int(input("Add new student's phone number: "))

    newStudent = Student(userInput1, userInput2, userInput3, userInput4, userInput5)

    studentList.append(newStudent)



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


x = 15
while x > 0:
    print("1. Add new Student")
    print("2. Delete by code")
    print("3. Edit by code")
    print("4. Show by name")
    print("5. Show all students")

    userInput = int(input("Choose the number: "))

    if userInput == 1:
        for x in range(2):
            addNewStudent()
    elif userInput == 2:
        deleteByStudentCode()
    elif userInput == 3:
        editByStudentCode()
    elif userInput == 4:
        showStudentInfoByName()
    elif userInput == 5:
        showAllStudents()
    else:
        print("Error Typo")


