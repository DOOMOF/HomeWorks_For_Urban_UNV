grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

def cal_grades(x):
    avr_grades = []

    for i in range(len(x)):

        avr_grades.append((sum(x[i]) / len(x[i])))
    return avr_grades


print(dict(zip(sorted(students), cal_grades(grades))))
