class Student:
    def __init__(self, fname,lname, age, courses ,pocket ,location):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.courses = courses
        self.pocket = pocket
        self.location = location

    def display_info(self):
        print("Name:", self.get_fullname())    
        print("Age:", self.age)
        print("Courses:", ", ".join(self.courses))
        print('pocket :',self.pocket)
        print("location :",self.location)
        print("-" * 20)

    def get_fullname(self):

        return f"{self.fname} {self.lname}"

student1 = Student("Alice",'Inwonderland', 20, ["Math", "English"],100,'540 M6')
student2 = Student("Bob",'Biechawton', 22, ["Physics", "History"],500 , '654 M5')

student1.display_info()
student2.display_info()