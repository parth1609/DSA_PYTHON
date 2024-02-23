class kompany :
    def __init__(self, rollno, nam, salary):
        self.rollno = rollno
        self.nam = nam
        self.salary = salary

    def show(self):
        print(f"th rollno {self.rollno} having nam {self.nam} having salary {self.salary}")
    
roll = int(input("roll no. "))
Name = input("nams is ")
sal = int(input("Salary is "))

k1 = kompany(roll, Name, sal)
k1.show()
