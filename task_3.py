with open("employees_salary.txt", "r", encoding="UTF-8") as text:
    employees_salaries = text.read().split("\n")
    emp_base = []
    sal_base = []

    for string in employees_salaries:
        words = string.split( )
        employee = words[0]
        salary = int(words[1])
        emp_base.append(employee)
        sal_base.append(salary)

    work = dict(zip(sal_base, emp_base))
    poor = []

    for i in work:
        if i < 20000:
            poor.append(work[i])
    print(f"Сотрудники, которые получают меньше 20 000: {', '.join(poor)}")

    average_sal = sum(sal_base) / len(sal_base)
    print(f"Средняя величина дохода сотрудников: {average_sal}")

