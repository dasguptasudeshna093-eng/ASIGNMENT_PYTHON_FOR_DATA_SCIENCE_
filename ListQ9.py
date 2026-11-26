scores = [[78, 82, 91], [65, 70, 68], [90, 88, 94],  [55, 61, 58]]
averages = []
passing_students = 0

for student in scores:
    total = 0
    for score in student:
        total += score

    average = total / len(student)
    averages.append(average)
    print("Total:", total, "Average:", round(average, 2))
    if average >= 60:
        passing_students += 1

highest_average = max(averages)
highest_index = averages.index(highest_average)

print("Averages: ", averages)
print("Passing students: ", passing_students)
print("Student with highest average: ", highest_index)
