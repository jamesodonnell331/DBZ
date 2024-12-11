#My Dragon Ball Z Video Game (Codecademy project from object oriented programming portion of CS course)
#Character and Opponent classes
class Character:
  def __init__(self, name, race, power, max_health, special_attack):
    self.name = name
    self.race = race
    self.power = power
    self.max_health = max_health
    self.special_attack = special_attack

  def __repr__(self):
    return f"{self.name} the {self.race} is a hero and is destined to be victorious. Power: {self.power}. Max Health: {self.max_health}. Special Attack: {self.special_attack}."

  def attack(self, opponent):
    opponent.max_health -= self.power
    print(f"{self.name} attacks {opponent.name} and reduces their health by {self.power} points.")

  def use_special_attack(self, opponent):
    opponent.max_health -= (self.power * 1.5)
    print(f"{self.name} uses {self.special_attack} on {opponent.name} and reduces their health by {self.power * 1.5} points.")
  
  def healing(self):
    increase = self.max_health * 0.25
    self.max_health += increase
    print(f"{self.name} heals and increases their max health by {increase} points.")

class Opponent:
  def __init__(self, name, race, power, max_health, special_attack):
    self.name = name
    self.race = race
    self.power = power
    self.max_health = max_health
    self.special_attack = special_attack

  def __repr__(self):
    return f"{self.name} the {self.race} is a formidable force and should not be messed with. Power: {self.power}. Max Health: {self.max_health}. Special Attack: {self.special_attack}."
  
  def attack(self, character):
    character.max_health -= self.power
    print(f"{self.name} attacks {character.name} and reduces their health by {self.power} points.")
  
  def use_special_attack(self, amount):
    character.max_health -= (self.power * 1.5)
    print(f"{self.name} uses {self.special_attack} on {character.name} and reduces their max health by {self.power * 1.5} points.")

  def healing(self):
    increase = self.max_health * 0.25
    self.max_health += increase
    print(f"{self.name} heals and increases their max health by {increase} points.")

#Creating character and opponent objects
character_one = Character("Goku", "Saiyan", 50, 100, "Kamehameha")
character_two = Character("Gohan", "Saiyan", 60, 90, "Ki Blast")

opponent_one = Opponent("Frieza", "Alien", 45, 120, "Death Beam")
opponent_two = Opponent("Vegeta", "Saiyan", 50, 100, "Final Shine Attack")

#Getting input for character selection and opponent selection
character_selection = input("Which character would you like to choose as your fighter: Goku or Gohan?")
if character_selection == "Goku":
  selected_character = character_one
elif character_selection == "Gohan":
  selected_character = character_two
else:
  print("Invalid selection. Defaulting to Goku.")
  selected_character = character_one
print(selected_character)
  
opponent_selection = input("Who will you choose as your opponent: Frieza or Vegeta?")
if opponent_selection == "Frieza":
  selected_opponent = opponent_one
elif opponent_selection == "Vegeta":
  selected_opponent = opponent_two
else:
  print("Invalid selection. Defaulting to Vegeta.")
  selected_opponent = opponent_two
print(selected_opponent)

print("Lets FIGHT!")

#Calling attack method
selected_character.attack(selected_opponent)
print(f"{selected_opponent.name}'s remaining max health: {selected_opponent.max_health}")

selected_opponent.attack(selected_character)
print(f"{selected_character.name}'s remaining max health: {selected_character.max_health}")

#Calling healing method
selected_opponent.healing()
print(f"{selected_opponent.name}'s remaining max health: {selected_opponent.max_health}")

#Calling use_special_attack method
selected_character.use_special_attack(selected_opponent)
print(f"{selected_opponent.name}'s remaining max health: {selected_opponent.max_health}")

#Game over condition
if selected_character.max_health or selected_opponent.max_health < 1:
  print("Game Over")

#Second Round Fight
print("Lets FIGHT!")

