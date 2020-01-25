#######################################
# Practice: Custom Colors and Sounds  #
#######################################


# Define 5 of your favorite vehicles
# Move all common properties in your vehicles to a new Vehicle class.

class vehicle:
    def __init__(self, main_color, maximum_occupancy):
        self.main_color = main_color
        self.maximum_occapancy = maximum_occupancy

    def drive(self):
        print("The vehicle goes past. Put put put put.")

    def turn(self, direction):
        print(f"It's making a {direction} turn.")

    def stop(self):
        print("It's stopping now")


class bus(vehicle):
    def __init__(self, main_color, maximum_occupancy, mph_max):
        super().__init__(main_color, maximum_occupancy)
        self.mph_max = mph_max

    def drive(self):
        print(f"\nThe {self.main_color} bus goes past. Vrrrooooom.")

    def stop(self):
        print("This vehicle stops at all railroad crossings")


class electric_car(vehicle):
    def __init__(self, main_color, maximum_occupancy, number_of_battery_cells, mph_max):
        super().__init__(main_color, maximum_occupancy)
        self.number_of_battery_cells = number_of_battery_cells
        self.mph_max = mph_max

    def drive(self):
        print(f"\nThe {self.main_color} electric car goes past quietly...")


class truck(vehicle):
    def __init__(self, main_color, maximum_occupancy, engine_size, mph_max):
        super().__init__(main_color, maximum_occupancy)
        self.engine_size = engine_size
        self.mph_max = mph_max

    def drive(self):
        print(f"\nThe {self.main_color} truck goes past loudly...")

class boat(vehicle):
    def __init__(self, main_color, maximum_occupancy, engine_size, knots):
        super().__init__(main_color, maximum_occupancy)
        self.engine_size = engine_size
        self.knots = knots

    def drive(self):
        print(f"\nThe {self.main_color} boat goes past. Zoooooommm!")


class train(vehicle):
    def __init__(self, main_color, maximum_occupancy, number_of_cars, mph_max):
        super().__init__(main_color, maximum_occupancy)
        self.number_of_cars = number_of_cars
        self.mph_max = mph_max

    def drive(self):
        print(f"\nThe {self.main_color} train goes past. Chugga chugga chugga choo choo!")

    def stop(self):
        print("I need a lot of space to stop")


# Create an instance of each vehicle.
# Define a different value for each vehicle's properties.
bus = bus("yellow", 30, "75 mph")
electric_car = electric_car("red", 4, 12, "120 mph")
truck = truck("silver", 2, "400 cubic inches", "100 mph")
boat = boat("white", 6, "200 cubic inches", "90 knots")
train = train("black", 200, 10, "60 mph")


# Create a drive() method in the Vehicle class.
# Override the drive() method in all the other vehicle classes. Include the vehicle's color in the message (i.e. "The blue Ram drives past. RRrrrrrummbbble!").
# Create a turn(self, direction) method, and a stop(self) method on Vehicle. Define a basic implementation of each.

bus.drive()
bus.turn("left")
bus.stop()

electric_car.drive()
electric_car.turn("right")
electric_car.stop()

truck.drive()
truck.turn("left")
truck.stop()

boat.drive()
boat.turn("right")
boat.stop()

train.drive()
train.turn("left")
train.stop()


# Override all three of those methods on some of the vehicles. For example, the stop() method for a plane would be to output the message "The white Cessna rolls to a stop after rolling a mile down the runway."
# Make your vehicle instances perform all three behaviors.