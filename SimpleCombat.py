import random
random.seed()

# **************  Create a character and a monster**************
c_name = "Jiggly Jim"
c_health = 25
c_strength = 4
c_dexterity = 10

m_name = "slime ball"
m_health = 20
m_strength = 6
m_dexterity = 8

# Do combat with the monster
while c_health > 0 and m_health > 0:
    print(c_name, "'s health: ", c_health, sep='')
    print(m_name, "'s health: ", m_health, "\n", sep='')

    # Roll a die
    dieRoll = random.randint(1, 20)

    # If the roll is higher than the monster's dexterity, score a hit
    if dieRoll > m_dexterity:
        m_health -= c_strength

    # Roll a die
    dieRoll = random.randint(1, 20)

    # If the roll is higher than the character's dexterity, score a hit
    if dieRoll > m_dexterity:
        c_health -= m_strength

# End the battle
print(c_name, "'s health: ", c_health)
print(m_name, "'s health: ", m_health, "\n")

if c_health > 0:
    print(c_name, " is victorious over the ", m_name, "!", sep='')
else:
    print(c_name, " has been slain by the ", m_name, "!", sep='')