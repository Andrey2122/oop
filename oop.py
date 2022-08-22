class Student:
    student_list = []

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def avg_grade_students(student_list, course):
        s = 0
        counter = 0
        for student in student_list:
            if course in student.courses_in_progress:
                s += student.count_avg_grade()
                counter += 1
        return s

    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def count_avg_grade(self):
        if len(self.grades.values()) > 0:
            return sum(list(self.grades.values())[0]) / len(list(self.grades.values())[0])
        else:
            return 0

    def __str__(self):
        return f"Имя: {self.name}\n" \
               f"Фамилия: {self.surname}\n" \
               f"Средняя оценка за домашние задания: {self.count_avg_grade()}\n" \
               f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n" \
               f"Завершенные курсы: {', '.join(self.finished_courses)}\n"
               
    def __lt__ (self, other):
        if isinstance(other, Student):
            if self.count_avg_grade() < other.count_avg_grade():
                return True
            else:
                return False
        else:
            pass


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    lecturer_list = []

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.count_avg_grade()}\n"

    def __init__(self, name, surname):
        Lecturer.lecturer_list.append(self)
        self.grades = {}
        super().__init__(name, surname)

    def count_avg_grade(self):
        if len(self.grades.values()) > 0:
            return sum(list(self.grades.values())[0]) / len(list(self.grades.values())[0])
        else:
            return 0

    def avg_grade_lectors(lecturer_list, course):
        s = 0
        counter = 0
        for lecturer in lecturer_list:
            if course in lecturer.courses_attached:
                s += lecturer.count_avg_grade()
                counter += 1
        return s / counter

    def __lt__ (self, other):
        if isinstance(other, Lecturer):
            if self.count_avg_grade() < other.count_avg_grade():
                return True
            else:
                return False
        else:
            pass


class Reviewer(Mentor):
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\n"

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
        
some_student = Student('Ruoy', 'Eman', 'your_gender')
second_student = Student('Andrey', 'Stepanov', 'your_gender')
some_student.finished_courses += ['Python'] 
second_student.finished_courses += ['Git'] 
some_student.rate_lec('some_lecturer', 'Git', 8)
some_student.rate_lec('second_lecturer', 'Python', 9)
second_student.rate_lec('second_lecturer', 'Python', 10)
second_student.rate_lec('some_lecturer', 'Git', 8)

some_lecturer = Lecturer(f'Some', 'Buddy')
second_lecturer = Lecturer(f'Ivan', 'Petrov')
some_lecturer.courses_attached += ['Python']
second_lecturer.courses_attached += ['Git']

some_reviewer = Reviewer('Some', 'Buddy')
second_reviewer = Reviewer('Aleksander', 'Ivanov')
second_reviewer.courses_attached += ['Python']
some_reviewer.courses_attached += ['Git']
second_reviewer.rate_hw('some_student', 'Python', 6)
some_reviewer.rate_hw('some_student', 'Git', 10)



print(some_reviewer, '\n')
print(second_reviewer, '\n')
print(some_lecturer, '\n')
print(second_lecturer, '\n')
print(some_student, '\n')
print(second_student, '\n')
