# BEHOLD, MY SHITTY CODE.
# Fuck comments. Ya have to do without comments because (;-;) (ToT)
# At this rate I'm gonna have a heart attack due to shock and stress

class Binusmaya:
    def __init__(self):
        self.lecturers = [{"name": "Jude", 
                      "subject": "Algorithm and Programming", 
                      "lecturerID": "123"},
                      {"name": "IDK", 
                      "subject": "Nonexistent", 
                      "lecturerID": "24"},
                      {"name": "Whom", 
                      "subject": "qwe", 
                      "lecturerID": "341"}]
        self.classes = ["L1AC", "L1BC", "L1CC"]
        self.schedules = []

    def add_lecturer(self, name, subject, ID):
        __lecturer_data = {}
        __lecturer_data["name"] = name
        __lecturer_data["subject"] = subject
        __lecturer_data["lecturerID"] = ID 
        self.lecturers.append(__lecturer_data)

    def remove_lecturer(self, ID_to_be_deleted):
        i = 0
        index_to_be_deleted = -1
        for a_lecturer in self.lecturers:
            if a_lecturer["lecturerID"] == ID_to_be_deleted:
                index_to_be_deleted = i
                break
            i += 1

        del self.lecturers[index_to_be_deleted]
                
    def add_class_code(self, class_code):
        self.classes.append(class_code)

    def remove_class_code(self, class_code):
        try:
            self.classes.remove(class_code)
        except:
            print("Class code not found")
    
    def add_schedule(self, class_name, time, subject):
        # search lecturer name by subject
        lecturer_name = ""
        for a_lecturer in self.lecturers:
            if a_lecturer["subject"] == subject:
                lecturer_name = a_lecturer["name"]

        # append tuple to list
        __schedule_tuple = (time, class_name, subject, lecturer_name)
        self.schedules.append(__schedule_tuple)


# MAIN
my_binusmaya_site = Binusmaya()

print(my_binusmaya_site.lecturers)
my_binusmaya_site.add_lecturer("Budi", "Nganggur", "999")
print(my_binusmaya_site.lecturers)

my_binusmaya_site.remove_lecturer("24")
print(my_binusmaya_site.lecturers)

print(my_binusmaya_site.classes)
my_binusmaya_site.add_class_code("L1BB")
print(my_binusmaya_site.classes)
my_binusmaya_site.remove_class_code("L1AC")
print(my_binusmaya_site.classes)

print(my_binusmaya_site.schedules)
my_binusmaya_site.add_schedule("L1BB", "09:30", "Nganggur")
print(my_binusmaya_site.schedules)