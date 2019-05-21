def find_new_salary(current_salary,job_level):
    if job_level==3:
        new_salary=(15/100)*current_salary+current_salary
    elif job_level==4:
        new_salary=(7/100)*current_salary+current_salary
    elif job_level==5:
        new_salary=(5/100)*current_salary+current_salary
    else:
        new_salary="invalid"
    return new_salary
new_salary=find_new_salary(10000,3)
print(new_salary)
