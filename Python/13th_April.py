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
    
    def accelerate(self):
        if self.speed > 100:
            print('Limit reached.')
        else:
            self.speed += 10
    
    def stop(self):
        if self.break1 == 0:
            print("Can't decrease the speed.")
        else:
            break1 -= 10
    
c1 = Car('Cyber Truck','Red','Tesla',5000000,75,15)
c1.info()