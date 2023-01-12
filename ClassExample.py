# Cat as a Class

class Cat:
    fur ='Long hair, short hair'

    def __init__(self, breed, eye_colour, clawed_or_declawed, age):
        self.breed = breed
        self.eye_colour = eye_colour
        self.clawed_or_declawed = clawed_or_declawed
        self.age = age

    def play(self):
        print("The cat wants to play.")

Purrugly = Cat('Tabby','Green','Clawed',2)
print(Purrugly.breed)
print(Purrugly.eye_colour)
print(Purrugly.clawed_or_declawed)
print(Purrugly.age)
Purrugly.play()