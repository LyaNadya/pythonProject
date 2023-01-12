class Vehicle:
    engine_capacity = "1,6 Turbo"

    def __init__(self,number_of_wheels,type_of_tank,seating_capacity,maximum_velocity):
        self.number_of_wheels = number_of_wheels
        self.type_of_tank = type_of_tank
        self.seating_capacity = seating_capacity
        self.maximum_velocity = maximum_velocity

    def drive(self):
        print("The vehicle is in driving mode now.")

vios = Vehicle('4','petrol',5,180)
print(vios.number_of_wheels)
print(vios.type_of_tank)
print(vios.seating_capacity)
print(vios.maximum_velocity)
vios.drive()

class Electric_Car(Vehicle):
    def __init__(self, number_of_wheels, seating_capacity, maximum_velocity):
        Vehicle.__init__(self,number_of_wheels, 'electric', seating_capacity, maximum_velocity)

blueSG = Electric_Car('4', 5, 150)
print(blueSG.number_of_wheels)
print(blueSG.type_of_tank)
print(blueSG.seating_capacity)
print(blueSG.maximum_velocity)
blueSG.drive()


class Computer:
    CPU = "12 Gigahertz"

    def __init__(self, storage_capacity, frames_per_second, audio_level):
        self.storage_capacity = storage_capacity
        self.frames_per_second = frames_per_second
        self.audio_level = audio_level

    def playGame(self):
        print("Welcome to Genshin Impact!")

ether = Computer('100GB','60 Frames',40)
print(ether.storage_capacity)
print(ether.frames_per_second)
print(ether.audio_level)
ether.playGame()

class laptop(Computer):
    def __init__(self, storage_capacity, frames_per_second, audio_level ):
        Computer.__init__(self, storage_capacity, frames_per_second, audio_level)
class desktop(Computer):
    def __init__(self, storage_capacity, frames_per_second, audio_level ):
        Computer.__init__(self, storage_capacity, frames_per_second, audio_level)

HyperX = laptop('60GB','90 Frames',54)
print(HyperX.storage_capacity)
print(HyperX.frames_per_second)
print(HyperX.audio_level)
HyperX.playGame()

Razer= desktop('210GB','30 Frames',90)
print(Razer.storage_capacity)
print(Razer.frames_per_second)
print(Razer.audio_level)
Razer.playGame()

