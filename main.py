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
    
    def is_eligible(self, height):
        if height > self._minheight:
            print('Get on the ride.')
        else: 
            print(f'You are too short for {self._name} buddy, get taller than {self._minheight}😭🙏🙏🙏')

class FamilyRide(Base):
    def __init__(self, name, capacity, min_age):
        super().__init__(name, capacity)
        self._minage = min_age
    def start(self):
        print(f'Family Ride {self._name} is now starting. Enjoy the fun!')