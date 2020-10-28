class Student:

    
    def __init__(self, name, age, class_ = "student"):
        self.name = name
        self.age = age
        self.class_ = class_

    def method(self, test1, test2, test3):
        score = int(test1 + test2 + test3)/3
        return score

John = Student("John", "21")
Jane = Student("Jane", "22") 
Alex = Student("Alex", "23")

print(John.method(90, 80, 70))
print(Jane.method(30, 80, 100))
print(Alex.method(60, 10, 75))