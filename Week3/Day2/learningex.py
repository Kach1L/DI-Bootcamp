# Ex 1: Basic Classes
class Employee:
    def __init__(self,first_name,last_name,age,job,salary,address):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.job = job
        self.salary = salary
        self.__address = address
        print(f'{self.first_name} {self.last_name} {self.age} years old {self.job}, who has a salary of ${self.salary}.')
        
        
    def get_fullname(self):
        return f"{self.first_name} {self.last_name}"
    
    def happy_birthday(self):
        self.age += 1
    
    def get_promotion(self, promotion_amount):
        self.salary += promotion_amount

    def __str__(self):
        return (f"name:{self.get_fullname} age:{self.age} job:{self.job} salary:{self.salary}")
    
    def create_best_employee(self,newemployee):
        if newemployee.salary>30000:
            self.newemployee = newemployee
            return newemployee
    
    @property
    def address(self):
        return self.address
    
    @address.setter
    def address(self,newaddress):
        try:
            if self.age > 30:
                self.address = newaddress
            else:
                raise TypeError('Too young Employee')
        except Exception as err:
            print(err)
            
    # What I learnt from Week3 Day3(Dunder Methods)
    def __gt__(self,other_employee):
        if self.salary>other_employee.salary:
            return self
        else:
            return other_employee 

    def __add__(self,other_employee):
        return self.salary + other_employee.salary




# Ex 2: Inheritance
class Developer(Employee):
    def __init__(self, first_name, last_name, age, job='developer', salary=15000):
        super().__init__(first_name, last_name, age, job, salary)
        self.coding_skills = []
        
    def add_skills(self, *skills):
        self.coding_skills.extend(skills)
        
    def coding(self):
        all_skills = ",".join(self.coding_skills)
        print((f'The developer named {self.get_fullname()}'))

    
        