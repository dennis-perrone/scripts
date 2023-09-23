#!/usr/bin/python3

salary_dict = {
    'Junior Engineer' : 80,
    'Senior Engineer' : 100,
    'Lead Engineer' : 140,
}

# for employee in salary_dict.items():


for employee, salary in salary_dict.items():
    print("="*len(str(employee)))
    print(f'Position: {employee}, Salary: ${salary},000')