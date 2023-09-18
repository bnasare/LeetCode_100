class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_grades(self):
        return ', '.join(map(str, self.grades))

    def add_grades(self, new_grades):
        for grade in new_grades:
            self.grades.append(grade)

    def get_average_grade(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0

student_details = Student('Asare', 15, [39, 75, 57, 68])
student_details.add_grades([85, 90, 95])

print('Student name:', student_details.get_name())
print('Student age:', student_details.get_age())
print('Student grades:', student_details.get_grades())
print('Average grade:', student_details.get_average_grade())
