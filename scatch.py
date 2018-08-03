import random


class Player:
    water = ["waterball", "wave of piranhas", "trident throw", "shark attack"]
    fire = ["fireball", "ring of fire", "lava rain", "demon attack"]
    earth = ["rock attack", "army of trees", "landslide", "quicksand"]
    wind = ["thunderstorm", "tornado", "hurricane", "the Force"]
    tribes = [water, fire, earth, wind]

    def __init__(self, name, tribe):
        self.name = name
        min_val = 1
        max_val = 4
        self.tribe = list(tribe)

        max_val = 10
        self.ability1 = random.randint(min_val, max_val)
        self.ability2 = random.randint(min_val, max_val)
        self.ability3 = random.randint(min_val, max_val)
        self.ability4 = random.randint(min_val, max_val)


name = input("Hi, I'm Jared of the water tribe, and what's your name?")
print("Hello, and which tribe do you belong to?")
tribe = input("Press [W] for Water, [F] for Fire, [E] for Earth, or [W] for Wind")
if tribe == "W":
    tribe = "water"
if tribe == "F":
    tribe = "fire"
if tribe == "E":
    tribe = "earth"
if tribe == "W":
    tribe = "wind"
player = Player(name, tribe)




