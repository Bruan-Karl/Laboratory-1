studentName = input("Enter your name: ")
programName = input("Enter your program: ")
prelimsGrade = input("Enter your Prelims grade:")
midtermsGrade = input("Enter your Midterms grade: ")
finalsGrade = input("Enter your Finals grade: ")
semestral_grade = (float(prelimsGrade) + float(midtermsGrade) + float(finalsGrade))//3
semestral_grades = round(semestral_grade , 2)

print('Hi' , studentName,'! Your Sesmestral Grade is', semestral_grades)

happy = '\U0001f600'
LOL = '\U0001F606'
sad = '\U0001F62D'

if (semestral_grades > 70):
    print(happy)

elif(semestral_grades == 70):
    print(LOL)

else:
    print(sad)

