def grade(name, hw_score, assess_score, final_exam):
    hw_percent = hw_score * 4
    assess_percent = assess_score * 2
    total_bf_divide = hw_percent + assess_percent + final_exam
    total = total_bf_divide/3
    if total >= 70:
        grade = 'A' 
    elif total >= 60:
        grade = 'B' 
    elif total >= 50:
        grade = 'C'   
    elif total >= 40:
        grade = 'D'
    else: 
        grade = 'Fail'
    return name, total, grade    

grade1 = grade('Alex', 20, 44, 90)
print(grade1)    