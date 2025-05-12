


class Car:
    """simulator"""

    def __init__(self, make, model, year):
        """initial attributes"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return description"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print odometer message"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set up"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Increase"""
        self.odometer_reading += miles



class Battery:
    """simulator"""

    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        ranges = 0
        if self.battery_size == 40:
            ranges = 150
        elif self.battery_size == 65:
            ranges = 225
        print(f"This car can go about {ranges} miles on a full charge.")



class ElectricCar(Car):
    """Electric Car"""

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()



my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()