# Assignment 1.19

gradeList = [5.0, 4.7, 3.4, 3.0, 2.7, 2.4, 2.0, 1.7, 1.4, 0.0]

def grades_to_letter (p1: list) -> list:
    letterGradeList = [] # Variable to hold final return values
    for x in p1: # Loop through each GPA in the list
        # Use if statements to assign letter grades and append those to the grade list
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

print(grades_to_letter(gradeList)) # Call function in print statement using values defined above