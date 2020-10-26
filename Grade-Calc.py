def grade_calculator(maths, chemistry, physics):
    total_percentage = float(maths + chemistry + physics)/3
    print(total_percentage)
    if total_percentage >= 70:
        return("Grade: A")
    elif total_percentage >= 60:
        return("Grade: B")
    elif total_percentage >= 50:
        return("Grade: C")
    elif total_percentage >= 40:
        return("Grade: D")    
    else:
        return("You fail!!!")     
        
maths_mark = int(input("What is your maths mark?"))
chemistry_mark = int(input("What is your chem mark?"))
physics_mark = int(input("What is your physics mark?"))

print(grade_calculator(maths_mark, chemistry_mark, physics_mark))