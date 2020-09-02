class Student:
    def __init__(self, kod, ad, soyad, email, number):
        self.kod = kod
        self.ad = ad
        self.soyad = soyad
        self.email = email
        self.number = number

    def showStudents(self):
        print(f"Kod: {self.kod} , Ad: {self.ad}, Soyad: {self.soyad} , Email: {self.email}, Number: {self.number}")