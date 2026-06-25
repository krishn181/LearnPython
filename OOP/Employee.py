class Employee:
    count = 0
    def __init__(self, name:str, salary:int):
        self.name = name
        self.salary = salary
        Employee.count +=1 
    def display_emp(self):
        print("Emp details ",self.name,", and salary ",self.salary)
    
    def annual_salary(self):
        return self.salary
    def emp_count():
        return Employee.count

emp = Employee("Harish",1234)
emp1 = Employee("Harish",134)
emp.display_emp()
print("Annual salary of emp ",emp.annual_salary())
print(Employee.emp_count())
    
    
