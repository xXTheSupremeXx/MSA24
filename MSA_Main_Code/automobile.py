#create an automobile class

class Automobile():

    #Define a constructor
    #The constructor is a function that executes when an object is created
    def __init__(self, make, model, vin, engine_size, owner, year):
        #assigne class properties values
        self.make = make
        self.model = model
        self.vin = vin
        self.engine_size = engine_size
        self.owner = owner
        self.yea = year
 