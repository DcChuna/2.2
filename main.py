class Student:
    def __init__(self):
        self.name = "Oleg"
        self.surname = "Bobyl"
        self.age = 20
        self.gradebook = [22, 12, 11, 11, 22]
        self.sum_gradebook = sum(self.gradebook) / len(self.gradebook)

class Diploma:
    def __init__(self):
        self.nothing = "воно потрібно для того щоби бути"
    def diploma(self):
        if self.sum_gradebook > 5 and 10> self.sum_gradebook:
            print("Im stronger,Im smarter, Im better, Im better")
        if self.sum_gradebook < 5:
            print("Im loser.")
        if self.sum_gradebook > 10 :
            print("I am not a king . I am a not god. I am ... worse")


    def method(self):
        print("about Aspirant")

class Aspirant(Student, Diploma):
    def pr(self):
        self.method()
        print(f"{self.name} {self.surname}")
        print(f"age = {self.age}")
        print(f"marks = {self.gradebook}")
        print(f"marks = {self.sum_gradebook}")
        self.diploma()

Aspirant1 = Aspirant()
Aspirant1.pr()