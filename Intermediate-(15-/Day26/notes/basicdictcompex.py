#Aim: To make a dictionary with names as keys and random integer as value (test score)
import random

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

student_scores = {student:random.randint(0, 100) for student in names}
print(student_scores)
print()

passed_students = {student:score for (student, score) in student_scores.items() if score >= 60}
print(passed_students)