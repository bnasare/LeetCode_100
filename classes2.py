class Cars:
    def __init__(self, carName, carModel, carColor):
        self.carColor = carColor
        self.carName = carName
        self.carModel = carModel

    def get_carDetails(self):
        return  f"{self.carColor} {self.carName} {self.carModel}."
    def change_carDetails(self, carName, carModel, carColor):
        self.carColor = carColor
        self.carName = carName
        self.carModel = carModel

cars= Cars('Toyota','Vitz','blue')
cars.change_carDetails('Toyota','Vitz','yellow')

print('The car I have is a', cars.get_carDetails())