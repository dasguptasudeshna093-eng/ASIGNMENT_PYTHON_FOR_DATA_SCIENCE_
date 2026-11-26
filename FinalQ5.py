
def analyse_marks(marks):

    highest = max(marks)
    lowest = min(marks)
    average = sum(marks) / len(marks)

    passed = 0
    failed = 0

    for mark in marks:
        if mark >= 50:
            passed += 1
        else:
            failed += 1

    return highest, lowest, average, passed, failed

student_marks = [78, 45, 82, 39, 67, 50, 91]

result = analyse_marks(student_marks)

print("Highest mark:", result[0])
print("Lowest mark:", result[1])
print("Average mark:", result[2])
print("Number of passes:", result[3])
print("Number of fails:", result[4])
