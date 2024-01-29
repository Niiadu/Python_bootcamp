import random
# number = [1, 2, 3]
# new_number = [n + 1 for n in number]
# print(new_number)

# name = "Angela"
# new_list = [letter for letter in name]
# print(new_list)

# new_number = [n * 2 for n in range(1, 5)]
# print(new_number)

# names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
# new_name = [n.upper() for n in names if len(n) > 5]
# print(new_name)

name = ["Alex", "James", "Jennifer", "Juliana", "Majorie"]
students_scores = {student: random.randint(1, 100) for student in name}
# passed_students = {student:score for (student, score) in students_scores.items() if score >= 60}
# print(passed_students)
#
# import pandas
#
# frame = pandas.DataFrame(students_scores.items())
# for (index, row) in frame.ite