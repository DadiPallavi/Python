class student():
    school_name = "XYZ School"
    def  set_details(self):
        self.name = "Vamsi"
        self.marks = 85
    def display(self):
        print("name ",self.name)
        print("Marks ",self.marks)
        print("School ",student.school_name)
o=student()
o.set_details()
o.display()

