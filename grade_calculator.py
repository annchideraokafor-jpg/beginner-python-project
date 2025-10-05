# student grade_calculator 
# input section

math = int(input("Enter Math score: "))
english = int(input("Enter English score: "))
biology = int(input("Enter Biology score: "))
chemistry = int(input("Enter Chemistry score: "))
# calculation

total = math + english + biology + chemistry
average = total / 4
# Grade logic

if average >= 70:
    grade = "A"
elif average >= 60:
    grade = "B"
elif average >= 50:
    grade = "C"
elif average >= 40:
    grade = "D"
else:
    grade = "F"

# output
print("\n---RESULT---")
print("Total Score:", total)
print("Average Score:", average)
print("Grade:", grade)