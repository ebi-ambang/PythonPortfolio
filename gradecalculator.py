# Calculator that will show a student's grade in 5 subjects
#A <= 90
#B >= 80
#C >= 70
#D >= 60
#E == Failed!

from re import S
from turtle import st


math_grade = int(input("Mathmatics grade:\n"))

if math_grade >= 90:
    print("You're grade is: A")
    
elif math_grade >= 80:
    print("You're grade is: B")

elif math_grade >= 70:
    print("You're grade is: C")

elif math_grade >= 60:
    print("You're grade is: D")

else:
    print("You're grade is: E and you have failed!")


chemistry_grade = int(input("Chemistry grade:\n"))

if chemistry_grade >= 90:
    print("You're grade is: A")
    
elif chemistry_grade >= 80:
    print("You're grade is: B")

elif chemistry_grade >= 70:
    print("You're grade is: C")

elif chemistry_grade >= 60:
    print("You're grade is: D")

else:
    print("You're grade is: E and you have failed!")
    


biology_grade = int(input("Biology grade:\n"))

if biology_grade >= 90:
    print("You're grade is: A")
    
elif biology_grade >= 80:
    print("You're grade is: B")

elif biology_grade >= 70:
    print("You're grade is: C")

elif biology_grade >= 60:
    print("You're grade is: D")

else:
    print("You're grade is: E and you have failed!")


physics_grade = int(input("Physics grade:\n"))

if physics_grade >= 90:
    print("You're grade is: A")
    
elif physics_grade >= 80:
    print("You're grade is: B")

elif physics_grade >= 70:
    print("You're grade is: C")

elif physics_grade >= 60:
    print("You're grade is: D")

else:
    print("You're grade is: E and you have failed!")  
    
    
literature_grade = int(input("Literature grade:\n"))

if literature_grade >= 90:
    print("You're grade is: A")
    
elif literature_grade >= 80:
    print("You're grade is: B")

elif literature_grade >= 70:
    print("You're grade is: C")

elif literature_grade >= 60:
    print("You're grade is: D")

else:
    print("You're grade is: E and you have failed!")