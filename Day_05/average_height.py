student_heights = input("Input a list of student heights ").split()
m = 0
totalsum = 0
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    totalsum = totalsum + student_heights[n]
    m = m + 1
print(round(totalsum/m))
