class Manufacturer :
    def __init__(self, identity,location):
        self.identity=identity
        self.location=location
class device :
    def __init__(self, name, price, identity,location):
        self.name = name
        self.price = price
        self.manufacturer=Manufacturer(identity,location)

    def describe(self):
      print(f"Name: {self.name} - Price: {self.price} Identity: {self.manufacturer.identity} - Location: {self.manufacturer.location}")

device1 = device(name="mouse", price=2.5, identity=9725, location="Vietnam") 
device2 = device(name="monitor", price=12.5, identity=11, location="Germany")

device1.describe()
device2 .describe()
