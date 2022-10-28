class Student:
    def __init__(self):
        self.name = "Oleg"
        self.surname = "Bobyl"
        self.age = 20
        self.gradebook = [22, 12, 11, 11, 22]
        self.sum_gradebook = sum(self.gradebook) / len(self.gradebook)

