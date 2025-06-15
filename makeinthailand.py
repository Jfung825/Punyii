class Student:
    student_count = 0

    def __init__(self, fname,lname, age, courses ,sarary):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.courses = courses
        self.pocket = 0
        self.sarary = sarary
        Student.student_count +=1

    def display_info(self):
        print("Name:", self.get_fullname())    
        print("Age:", self.age)
        print("Courses:", ", ".join(self.courses))
        print('pocket :',self.pocket)
        print("sarary :",self.sarary)
        print("-" * 20)

    def get_fullname(self):

        return f"{self.fname} {self.lname}"

student1 = Student("Alice",'Inwonderland', 20, ["Math", "English"],540)
student2 = Student("Bob",'Biechawton', 22, ["Physics", "History"],654)

student1.display_info()
student2.display_info()

print(Student.student_count)