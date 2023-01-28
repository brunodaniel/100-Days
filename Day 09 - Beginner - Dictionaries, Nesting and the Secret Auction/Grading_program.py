students_scores = {"Harry": 81, "Ron": 78, "Hermione": 99, "Draco": 74, "Neville": 62,}
students_grades={}
for key in students_scores:
    if students_scores[key] > 90:
        students_grades[key] = "Outstanding"
    elif students_scores[key] > 80 and students_scores[key] < 91:
        students_grades[key] = "Exceeds Expectations"
    elif students_scores[key] > 70 and students_scores[key] <= 80:
        students_grades[key] = "Acceptable"
    else:
        students_grades[key] = "Fail"

print(students_grades)