
class Binusmaya:
    def __init__(self, Lecturers, Classes, Schedules):
        self.Lecturers= Lecturers
        self.Classes= Classes 
        self.Schedules = Schedules
    
    def add_lect(self, name:str, subject:str, id=str):
        if self.check_for_lect(subject):
            print('Error, matching data already exists')
        else:
            new_lect = {'Name' : name, 'ID' : id, 'Subject' : subject }
            self.Lecturers.append(new_lect)
            print('Lecturer added successfully')
    
    def check_for_lect(self, subject: str) -> bool:
        for lect in self.Lecturers:
            if lect['Subject'] == subject:
                return True
        return False 
    
    def remove_lect(self, id:str):
        for lect in self.Lecturers:
            if lect['ID'] == id:
                self.Lecturers.remove(lect) 
                print('lecturer removed successfully')
                return
        else:
            print('no lecturer with matching ID')
    
    def add_class(self, classes: str ):
        if self.check_for_class(classes):
            print('Error, class already exists')
        else:
            new_class= (classes)
            self.Classes.append(new_class)
            print('class added successfully')
            return 
    
    def check_for_class(self, classes: str) -> bool:
        for i in self.Classes:
            if i == classes:
                return True
        return False 
    
    def remove_class(self, classes: str):
        for i in self.Classes:
            if i == classes:
                self.Classes.remove(i)
                print('class removed successfully')
                return
        else:
            print('no such class exists')
    
    def add_schedule(self, clas : str, time : str, subject : str):
        lect_subject = ''
        lect_name = ''
        for lect in self.Lecturers:
            if lect['Subject'] == subject:
                lect_subject = lect['Subject']
                lect_name = lect['Name']
        if lect_subject and lect_name:
            new_sched = (time, clas, lect_subject, lect_name)
            self.Schedules.append(new_sched)
            print('schedule added successfully')
        else:
            print('No subjects match')


data= Binusmaya([{'Name':'Jude', 'ID':'1234567','Subject':"Algoprog"},{'Name':'Zhandos', 'ID':'7654332', 'Subject':'Scientific Computing'}],
['L1AC','L1BC','L1CC'],
[] )




#addimg lecturers 
data.add_lect('Bobbie','6543217','math')
data.add_lect('Bobbie','6543217','AlgoProg')
print(data.Lecturers)

#removing lecturers 
data.remove_lect('1234567')
print(data.Lecturers)

#adding classes
data.add_class('L1DC')
data.add_class('L1AC')
data.add_class('L1FC')
print(data.Classes)

#removing classes 
data.remove_class('L1AC')
print(data.Classes)

#adding schedules 
data.add_schedule('L1AC','14:00','Scientific Computing')
data.add_schedule('L1BC','13:00','Art Class')
print(data.Schedules)







