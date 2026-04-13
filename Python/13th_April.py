class Car():
    
    def __init__(self,name,color,brand,price,speed,break1):
        self.name = name
        self.color = color
        self.brand = brand
        self.price = price
        self.speed = speed
        self.break1 = break1
    
    def info(self):
        print('Car Name :',self.name)
        print('Car Color :',self.color)
        print('Car brand :',self.brand)
        print('Car price :',self.price)
        print('Car speed :',self.speed)
        print('Car stopped at',self.break1)
        print('_'*22)
    
    def start(self):
        print(f'{self.name} started')
        print('_'*22)
    
    def accelerate(self):
        if self.speed > 100:
            print('Limit reached.')
            self.speed -= 30
            print(f'Limit reached so car speed reduced to {self.speed}')
        else:
            self.speed += 10
            print(self.speed)
        print('_'*22)
    
    def stop(self):
        if self.break1 < 0:
            print("Can't decrease the speed.")
            self.break1 += 10
            print(f'Car started at speed {self.speed}')
        else:
            self.break1 -= 10
            print(self.break1)
        print('_'*22)
        
# First object
c1 = Car('Cyber Truck','Red','Tesla',5000000,75,15)
c1.info()
c1.accelerate()
c1.stop()
c1.start()

# Second Object
c2 = Car('BMW X7','Blue','BMW',25000000,125,0)
c2.start()
c2.accelerate()
c2.stop()

# Third Object
c3 = Car('R8','Red','AUDI',10000000,140,6)
c3.start()
c3.accelerate()
c3.stop()