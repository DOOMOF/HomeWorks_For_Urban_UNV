grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}


def average_grades_calc(x):
    average_grades = []
    for i in range(len(x)):
        average_grades.append(sum(x[i]) / len(x[i]))
    return average_grades


print(dict(zip(sorted(students), average_grades_calc(grades))))