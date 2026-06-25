class Student:
    def __init__(self, name : str, roll_num : int, marks : float):
        self.name = name
        self.roll_num = roll_num
        self.marks = marks
    
    def calculate_grade(self):
        if 85 < self.marks < 100:
            return "Grade is :- A+"
        elif 75 < self.marks < 85:
            return "Grade is :- A"
        elif 65 < self.marks < 75:
            return "Grade is :- B"
        elif 55 < self.marks < 65:
            return "Grade is :- C"
        elif 45 < self.marks < 55:
            return "Grade is :- D"
        else :
            return "fail"
    
    def display_details(self):
        print ("Detail of student ",self.name," , ",self.roll_num," , ",self.marks)

S1 = Student("Anish",12,23.42)
grade = S1.calculate_grade()
print(grade)
S1.display_details()