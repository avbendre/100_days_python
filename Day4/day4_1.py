#classes
class Employee:
    def __init__(self,first,last,pay) :
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+'.'+last+'@company.com'

    def full_name(self):
        return '{} {}'.format(self.first, self.last)
        

emp_1= Employee('Abhishek','Bendre',6000000)
emp_2= Employee('Test','User',650191)


print(emp_1.email)
print(emp_2.email)
#print('{} {}'.format(emp_1.first, emp_1.last))
print(emp_2.full_name())  #instance is passed to the method
print(Employee.full_name(emp_1)) #Running method using the class name itself, so attribute is passed