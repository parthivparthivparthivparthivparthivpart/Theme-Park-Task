class Base:
    def __init__(self, name, capacity):
        self._name = name
        self._capacity = capacity
    
    def get_details(self):
        print(f'Attraction: {self._name}, Capacity: {self._capacity}')
    
    def start(self):
        print(f'The attraction, {self._name} is starting')

class ThrillRide(Base):
    def __init__(self, name, capacity, min_height):
        super().__init__(name, capacity)
        self._minheight = min_height

    def start(self):
        print(f'Thrill Ride {self._name} is now starting. Hold on tight!')
    
    def is_eligible(self, Visitor):
        if Visitor._height > int(self._minheight):
            print('Get on the ride.')
            Visitor.allowed_height == True
        else: 
            print(f'You are too short for {self._name} {Visitor._name}, get taller than {self._minheight}😭🙏🙏🙏')

class FamilyRide(Base):
    def __init__(self, name, capacity, min_age):
        super().__init__(name, capacity)
        self._minage = min_age
    def start(self):
        print(f'Family Ride {self._name} is now starting. Enjoy the fun!')
    def is_eligible(self, Visitor):
        if Visitor._age < int(self._minage):
            print('You are too young for this ride')
        else:
            print(f'You can get on {self._name}')
            Visitor.allowedage = True

class Staff:
    def __init__(self, name, role):
        self._name = name
        self._role = role
    
    def work(self):
        print(f'Staff {self._name} is performing their role: {self._role}')

class Visitor:
    def __init__(self, name, age, height):
        self._name = name
        self._age = age
        self.allowedage = False
        self._height = height
        self.allowed_height = False
    def ride(self, ThrillRide, FamilyRide):
        if self.allowed_height == True:
            print(f'{self._name} rode {ThrillRide._name}')
        else:
            print(f'{self._name} was too short to ride {ThrillRide._name}')
        
        if self.allowedage == True:
            print(f'{self._name} rode {FamilyRide._name}')
        else:
            print(f'{self._name} is too young to ride {FamilyRide._name}')

a = ThrillRide('Dragon Coaster', '20', '140')
b = FamilyRide('Merry-Go-Round', '30', '4')
a.start()
b.start()
c = Visitor('Parthiv', 17, 120)
b.is_eligible(c)
a.is_eligible(c)
c.ride(a, b)