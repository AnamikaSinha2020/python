
class Employee:
    num_of_emp=0
    raise_amt=1.04

    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.email = first+'.'+last + '@email.com'
        self.pay=pay

        Employee.num_of_emp +=1

    def fullnamme(self):
        return '{} { }'.format(self.first,self.last)

    def apply_raise(self):
        self.pay= int(self.pay * self.raise_amt)

emp1=Employee('Anamika','Sinha',50000)
emp2=Employee('Nisha','Verma',55000)

# print(Employee.raise_amt)
# print(emp1.raise_amt)
# print(emp2.raise_amt)

emp_str_1='Anamika-sinha-60000'
emp_str_2= 'Shital-verma-50000'

first,last,pay = emp_str_1.split('-')
new_emp_1=Employee(first,last,pay)
print(new_emp_1.email)
print(new_emp_1.pay)


