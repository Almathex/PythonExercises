def grade(name, hw_score, assess_score, final_exam):
    hw_percent = hw_score * 4
    assess_percent = assess_score * 2
    total_bf_divide = hw_percent + assess_percent + final_exam
    total = total_bf_divide/4
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
    return name, grade    

grade1 = grade('Alex', 23, 44, 80)
print(grade1)    