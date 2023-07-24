# Ex 1: Basic Classes
class Employee:
    def __init__(self,first_name,last_name,age,job,salary):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.job = job
        self.salary = salary
        print(f'{self.first_name} {self.last_name} {self.age} years old {self.job}, who has a salary of ${self.salary}.')
        
        
    def get_fullname(self):
        return f"{self.first_name} {self.last_name}"
    
    def happy_birthday(self):
        self.age += 1
    
    def get_promotion(self, promotion_amount):
        self.salary += promotion_amount

    def show_info(self):
        print(f"name:{self.get_fullname} age:{self.age} job:{self.job} salary:{self.salary}")




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
        