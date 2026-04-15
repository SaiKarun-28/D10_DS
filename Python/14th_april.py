# INHERITANCE

class parent():
    
    def __init__(self,name,age,work):
        self.name = name
        self.age = age
        self.work1 = work
    
    def info(self):
        print('Name :',self.name)
        print('Age :',self.age)
    
    def work(self):
        print(f'{self.name} is waorking as {self.work1}')
    

p1 = parent('Ravi',32,'Software_developer')
p1.info()
p1.work()
print('='*25)

# child class

class child(parent):
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def work(self): # method overriding
        print('Not working')
    
    def hub(self):  # specialized method
        print('Working')
        
c1 = child('varma',12)
c1.info()            # inherited method
c1.work()            
c1.hub()

