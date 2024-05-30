class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and 
            course in self.courses_in_progress and grade in range(1, 11)):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'  

    def average(self):  
        if self.grades:       
            grade_list = list(map(lambda x: sum(x)/len(x), self.grades.values()))        
            return sum(grade_list)/len(grade_list)
        else:
            return 'Ошибка'      
        
    def __str__(self): 
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self.average()}\n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' 
                f'Завершенные курсы: {", ".join(self.finished_courses)}')
    
    def __eq__(self, other):
        if self.average() != 'Ошибка' and other.average() != 'Ошибка': 
            return self.average() == other.average()
        else:
            return 'Ошибка' 
    
    def __lt__(self, other):
        if self.average() != 'Ошибка' and other.average() != 'Ошибка':
            return self.average() < other.average()
        else:
            return 'Ошибка'
    
    def __gt__(self, other):
        if self.average() != 'Ошибка' and other.average() != 'Ошибка':
            return self.average() > other.average() 
        else:
            return 'Ошибка' 

    def __le__(self, other):
        if self.average() != 'Ошибка' and other.average() != 'Ошибка':
            return self.average() <= other.average()
        else:
            return 'Ошибка' 
    
    def __ge__(self, other):
        if self.average() != 'Ошибка' and other.average() != 'Ошибка':
            return self.average() >= other.average()
        else:
            return 'Ошибка' 
        
class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)            
        self.grades = {} 

    def average(self):  
        if self.grades:       
            grade_list = list(map(lambda x: sum(x)/len(x), self.grades.values()))        
            return sum(grade_list)/len(grade_list)
        else:
            return 'Ошибка'

    def __str__(self):              
            return (f'Имя: {self.name}\n'
                    f'Фамилия: {self.surname}\n'
                    f'Средняя оценка за лекции: {self.average()}')
    
    def __eq__(self, other):
        if self.average() != 'Ошибка' and other.average() != 'Ошибка': 
            return self.average() == other.average()
        else:
            return 'Ошибка' 
    
    def __lt__(self, other):
        if self.average() != 'Ошибка' and other.average() != 'Ошибка':
            return self.average() < other.average()
        else:
            return 'Ошибка'
    
    def __gt__(self, other):
        if self.average() != 'Ошибка' and other.average() != 'Ошибка':
            return self.average() > other.average() 
        else:
            return 'Ошибка' 

    def __le__(self, other):
        if self.average() != 'Ошибка' and other.average() != 'Ошибка':
            return self.average() <= other.average()
        else:
            return 'Ошибка' 
    
    def __ge__(self, other):
        if self.average() != 'Ошибка' and other.average() != 'Ошибка':
            return self.average() >= other.average()
        else:
            return 'Ошибка' 

class Reviewer(Mentor):
    
    def __init__(self, name, surname):
        super().__init__(name, surname)  
               
    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student) and course in self.courses_attached and 
            course in student.courses_in_progress and grade in range(1, 11)):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def __str__(self):        
        return f'Имя: {self.name}\nФамилия: {self.surname}'

def average_student_rating(name_list, course):
    average = []
    for student in name_list:
        if isinstance(student, Student) and course in student.courses_in_progress:
            average.append(student.grades.get(course))            
        else:            
            return 'Ошибка' 
    grade_list = list(map(lambda x: sum(x)/len(x), average))    
    return sum(grade_list)/len(grade_list)     

def average_lecturers_rating(name_list, course):
    average = []
    for lecturer in name_list:
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            average.append(lecturer.grades.get(course))            
        else:            
            return 'Ошибка' 
    grade_list = list(map(lambda x: sum(x)/len(x), average))    
    return sum(grade_list)/len(grade_list) 
 
best_student = Student('Han', 'Solo', 'man')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Java']
best_student.courses_in_progress += ['Pascal']

best_student.finished_courses += ['C++']
best_student.finished_courses += ['PHP']

best_student_1 = Student('Boba', 'Fett', 'man')
best_student_1.courses_in_progress += ['Python']
best_student_1.courses_in_progress += ['ADA']
best_student_1.courses_in_progress += ['Java']

best_student_1.finished_courses += ['C++']
best_student_1.finished_courses += ['PHP']
 
cool_reviewer = Reviewer('Luke', 'Skywalker')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Java']

cool_reviewer_1 = Reviewer('Leia', 'Organa')
cool_reviewer_1.courses_attached += ['Python']
cool_reviewer_1.courses_attached += ['ADA']

cool_lecturer = Lecturer('R2', 'D2')
cool_lecturer.courses_attached += ['Python']
cool_lecturer.courses_attached += ['Java']

cool_lecturer_1 = Lecturer('C3', 'PO')
cool_lecturer_1.courses_attached += ['Pascal']
cool_lecturer_1.courses_attached += ['Java']

best_student.rate_hw(cool_lecturer, 'Python', 8)
best_student.rate_hw(cool_lecturer, 'Java', 9)
best_student.rate_hw(cool_lecturer, 'ADA', 5)

best_student.rate_hw(cool_lecturer_1, 'Pascal', 5)
best_student.rate_hw(cool_lecturer_1, 'Java', 10)

best_student_1.rate_hw(cool_lecturer, 'Python', 4)

best_student_1.rate_hw(cool_lecturer_1, 'Java', 5)
 
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Java', 9)
cool_reviewer.rate_hw(best_student, 'Java', 8)
cool_reviewer.rate_hw(best_student, 'Pascal', 8)

cool_reviewer.rate_hw(best_student_1, 'Python', 5)
cool_reviewer.rate_hw(best_student_1, 'Python', 5)
cool_reviewer.rate_hw(best_student_1, 'Java', 5)
cool_reviewer.rate_hw(best_student_1, 'Java', 5)
cool_reviewer.rate_hw(best_student_1, 'Pascal', 5)

cool_reviewer_1.rate_hw(best_student, 'Python', 8)
cool_reviewer_1.rate_hw(best_student, 'Python', 8)
cool_reviewer_1.rate_hw(best_student, 'Java', 8)
cool_reviewer_1.rate_hw(best_student, 'Java', 8)
cool_reviewer_1.rate_hw(best_student, 'Pascal', 8)

cool_reviewer_1.rate_hw(best_student_1, 'Python', 8)
cool_reviewer_1.rate_hw(best_student_1, 'Python', 8)
cool_reviewer_1.rate_hw(best_student_1, 'Java', 8)
cool_reviewer_1.rate_hw(best_student_1, 'Java', 8)
cool_reviewer_1.rate_hw(best_student_1, 'Pascal', 8)

print('1. ', average_student_rating([best_student, best_student_1], 'Python'))
print('2. ', average_lecturers_rating([cool_lecturer, cool_lecturer_1], 'Java')) 
print('3. ', best_student)
print('4. ', cool_lecturer)
print('5. ', cool_reviewer)
print('6. ', best_student_1)
print('7. ', cool_lecturer_1)
print('8. ', cool_reviewer_1)
print('9. ', cool_lecturer == cool_lecturer_1)
print('10. ', cool_lecturer > cool_lecturer_1)
print('11. ', cool_lecturer < cool_lecturer_1)
print('12. ', best_student == best_student_1)
print('13. ', best_student > best_student_1)
print('14. ', best_student < best_student_1)