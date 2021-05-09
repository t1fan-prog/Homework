class Person:
    name = None
    age = None
    gender = None

    def __init__(self, l_name, l_age, l_gender):
        self.name = l_name
        self.age = l_age
        self.gender = l_gender


class Teacher(Person):
    salary = None
    classroom_teacher = False

    def __init__(self, l_name, l_age, l_gender, l_salary, l_classroom_teacher):
        super().__init__(l_name, l_age, l_gender)
        self.salary = l_salary
        self.classroom_teacher = l_classroom_teacher


class Student(Person):
    average_grade = None
    quantity_of_classmates = None

    def __init__(self, l_name, l_age, l_gender, l_average_grade, l_quantity_of_classmates):
        super().__init__(l_name, l_age, l_gender)
        self.average_grade = l_average_grade
        self.quantity_of_classmates = l_quantity_of_classmates
