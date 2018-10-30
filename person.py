from car import Car

class Person:

    def __init__(self, name, occupation):
        self._name = name
        self._occupation = occupation

    @property
    def name(self):
        return self._name
    
    @property
    def occupation(self):
        return self._occupation

    @classmethod
    def has_oldest_car():
        