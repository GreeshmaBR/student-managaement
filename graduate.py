class Student(Person):

    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course


    def display(self):
        print("----- Student Details -----")
        print("Name :", self.name)
        print("Age :", self.get_age())
        print("Course :", self.course)


class GraduateStudent(Student):

    def __init__(self, name, age, course, specialization):
        super().__init__(name, age, course)
        self.specialization = specialization

    
    def display(self):
        print("----- Graduate Student -----")
        print("Name :", self.name)
        print("Age :", self.get_age())
        print("Course :", self.course)
        print("Specialization :", self.specialization)