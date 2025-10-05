# multiple student grade calculator
#----------------------------------

# Ask how many students you want to grade
num_students = int(input("Enter the number of students: "))

# create an empty dictionary to store names and grades
grades = {}

# Loop through each student
for i in range(num_students):
	     # Get the student's name
    name = input(f"Enter the name of student {i + 1}: ")
    
    # Get the student's grade
    grade = float(input(f"Enter the grade for {name}: "))
    
    # Store the name and grade in the dictionary
    grades[name] = grade

    # Determine letter grade
    if grade >= 70:
        letter_grade = 'A'
    elif grade >= 60:
        letter_grade = 'B'
    elif grade >= 50:
        letter_grade = 'C'
    elif grade >= 45:
        letter_grade = 'D'
    else:
        letter_grade = 'F'

    # Store the name and letter grade in the dictionary
    grades[name] = letter_grade

# print results neatly
print("\n--- Final Grades ---") 
for name, letter_grade in grades.items():
    print(f"{name}: {letter_grade}")  

