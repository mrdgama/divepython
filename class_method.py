class Vehicle(object):
    
#	def __init__(self, name):
#		self.name = name

    @classmethod
    def is_motorcycle(cls):
        return cls.wheels == 2
