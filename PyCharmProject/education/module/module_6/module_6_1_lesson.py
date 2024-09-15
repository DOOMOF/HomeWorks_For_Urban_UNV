class Human:
    head = True

    def __init__(self):
        self.about()
class Student(Human):
    head = False

    def about(self):
        print('я студент')

    def say_hell(self):
        print('Здравствуйте')

class Teacher(Human):

    def say_hell(self):
        print('Здравствуйте')

#human = Human()
student = Student()
print(student.head)