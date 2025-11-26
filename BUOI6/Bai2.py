#2a
class student :
    def __init__(self,name,yob,grade):
        self.name=name
        self.yob=yob
        self.grade=grade
    def describe (self):
        print (f'Student - Name:{self.name} - YoB: {self.yob} - Grade: {self.grade}')
class doctor :
    def __init__(self,name,yob,specialist):
        self.name=name
        self.yob=yob
        self.specialist=specialist
    def describe (self):
        print (f' Doctor - Name: {self.name} - YoB: {self.yob} - Specialist: {self.specialist}')
class teacher:
    def __init__(self,name,yob,subject):
        self.name=name
        self.yob=yob
        self.subject=subject
    def describe (self):
        print (f'Teacher - Name: {self.name} - YoB: {self.yob}- Subject: {self.subject}')
student1 = student(name="studentA", yob=2010, grade="7") 
student1.describe()
teacher1 = teacher(name="teacherA", yob=1969, subject="Math") 
teacher1.describe()
doctor1 = doctor(name="doctorA", yob=1945, specialist="Endocrinologists") 
doctor1.describe()
#2b
class Ward:
    def __init__(self, name):
        self.name = name
        self.people = []        

    def addPerson(self, person):
        self.people.append(person)

    def describe(self):
        print(f"Ward: {self.name}")
        for p in self.people:
            p.describe()
    def countdoctor (self):
        count=0
        for people in self.people:
            if isinstance (people,doctor):
                count+=1
        return count
teacher2 = teacher(name="teacherB", yob=1995, subject="History") 
doctor2 = doctor(name="doctorB", yob=1975, specialist="Cardiologists") 
ward1 = Ward(name="Ward1")
ward1.addPerson(student1) 
ward1.addPerson(teacher1)
ward1.addPerson(teacher2)
ward1.addPerson(doctor1) 
ward1 .addPerson(doctor2)
ward1.describe()
print('Number of doctor in ward :',ward1.countdoctor())


