# Assignment 1.19
# Write a Python function to convert GPAs to letter grades according to the table below. 
# Return a list of strings. Display result after function returns.

# function: def grades_to_letter (p1: list[float]) -> List[str]:

# Input: [4.0, 3.5, 3.8]
# Output: ['A+', 'A-', 'A']

# Input: [5.0, 4.7, 3.4, 3.0, 2.7, 2.4, 2.0, 1.7, 1.4, 0.0]
# Output: ['A+', 'A+', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'F']

# GPAs Grades
# 4.0: A+
# 3.7: A
# 3.4: A-
# 3.0: B+
# 2.7: B
# 2.4: B-
# 2.0: C+
# 1.7: C
# 1.4: C-
# below 1.4: F

gradeList = [5.0, 4.7, 3.4, 3.0, 2.7, 2.4, 2.0, 1.7, 1.4, 0.0]

def grades_to_letter (p1: list) -> list:
    letterGradeList = []
    for x in p1:
        if x >= 4.0:
            letterGradeList.append('A+')
        elif x >= 3.7 and x < 4.0:
            letterGradeList.append('A')
        elif x >= 3.4 and x < 3.7:
            letterGradeList.append('A-')
        elif x >= 3.0 and x < 3.4:
            letterGradeList.append('B+')
        elif x >= 2.7 and x < 3.0:
            letterGradeList.append('B')
        elif x >= 2.4 and x < 2.7:
            letterGradeList.append('B-')
        elif x >= 2.0 and x < 2.4:
            letterGradeList.append('C+')
        elif x >= 1.7 and x < 2.0:
            letterGradeList.append('C')
        elif x >= 1.4 and x < 1.7:
            letterGradeList.append('C-')
        else:
            letterGradeList.append('F')
    return letterGradeList

print(grades_to_letter(gradeList))

