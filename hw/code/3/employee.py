__author__ = 'nkrishn'

class Employee:
    def __init__(self,Name = ' ',Age=0):
        self.name = Name
        self.age = Age

    def __repr__(self):
        return "Name = %s \nAge = %d" % (self.name,self.age)

    def __lt__(self, other):
        return self.age<other.age


emp01 = Employee('Nikhil Krishnan', 30)
print emp01.__repr__()

emp02 = Employee('Rahul Krishna', 25)
print emp02.__repr__()

print emp01<emp02


