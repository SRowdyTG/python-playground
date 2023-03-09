class Player():
    def __init__(self, name, level, hp, mp, ad, ap, crit, race, stealth):
        self.name = name
        self.level = level
        self.hp = hp + (level * 1.5)
        self.mp = mp
        self.ad = ad
        self.ap = ap
        self.crit = crit
        self.race = race
        self.stealth = stealth

    def attack(self, ad, crit, stealth, rage):
        physdamage = (ad * stealth) * crit + (2* rage)
        return physdamage

    def castfireball(self, mp, ap, stealth, age):
        x = 3 + ap
        magdamage = ap + (age/10) + stealth
        self.mp = mp - x
        return magdamage
      
    def sneakattack(self, ad, crit, stealth):
        physdamage = (ad * (3*stealth)) * crit
        return physdamage

class Human(Player):
    def __init__(self, name, level, hp, mp, ad, ap, crit, race, stealth, profession, age, energy, rage):
        Player.__init__(self, name, level, hp, mp, ad, ap, crit, race, stealth)
        self.mp = self.mp + 5
        self.ad = self.ad + 5
        self.race = "Human"
        self.profession = profession
        self.age = age
        self.energy = energy
        self. rage = rage
        
class Elf(Player):

    def __init__(self, name, level, hp, mp, ad, ap, crit, race, stealth, profession, age, energy, rage):

        Player.__init__(self, name, level, hp, mp, ad, ap, crit, race, stealth)

        self.mp = mp + 15
        self.race = "Elf"
        self.profession = profession
        self.age = age
        self.energy = energy
        self. rage = rage

class Halfling(Player):
    def __init__(self, name, level, hp, mp, ad, ap, crit, race, stealth, profession, age, energy, rage):
        Player.__init__(self, name, level, hp, mp, ad, ap, crit, race, stealth)
        self.hp = hp - 5
        self.crit = crit + 10
        self.race = "Halfling"
        self.stealth = stealth + 15
        self.profession = profession
        self.age = age
        self.energy = energy
        self. rage = rage
        
class Orc(Player):
    def __init__(self, level, name, hp, mp, ad, ap, crit, race, stealth, profession, age, energy, rage):
        Player.__init__(self, name, level, hp, mp, ad, ap, crit, race, stealth)
        self.hp = hp + 10
        self.ad = ad + 15
        self.race = "Orc"
        self.profession = profession
        self.age = age
        self.energy = energy
        self.rage = rage
        
class Dragonborn(Player):
    def __init__(self, name, level, hp, mp, ad, ap, crit, race, stealth, profession, age, energy, rage):
        Player.__init__(self, name, level, hp, mp, ad, ap, crit, race, stealth)
        self.ap = ap + 10
        self.race = "Dragonborn"
        self.profession = profession
        self.age = age
        self.energy = energy
        self.rage = rage
        
import time
import random
import sys

def checkSave():
    pass

def overwriteSave(player):
    n = (input('Name your savefile: '))
    nombre_fichero = 'savefile' + str(n) + '.txt'
    playerData = "Name:{}\nLevel:{}\nHP:{}\nMP: {}\nAD: {}\nAP: {}\nCRIT: {}\nRace: {}\nStealth: {}\nProfession: {}\nAge: {}\nEnergy: {}\nRage: {}\n".format(player.name, player.level, player.hp, player.mp, player.ad, player.ap, player.crit, player.race , player.stealth, player.profession, player.age, player.energy, player.rage)
    f = open(nombre_fichero, 'w')
    f.write(playerData)
    f.close()

def loadSave():

    pass

def characterCreation():
    nameinput = ""
    player1 = None
    while not nameinput.isalnum():
        if not nameinput.isalnum():
            nameinput = input("What will your character's name be?")
    while True:
        pers = 0
        pers = int(input("Choose a character class.\n[1]Human\n[2]Elf\n[3]Halfling\n[4]Orc\n[5]Dragonborn"))
        if pers == 1:
            ageGen = random.randint(20, 60)
            tempprof = ""
            print("You've chosen 'Human' as your character class!")
            player1 = Human(nameinput, 1, 10, 10, 5, 5, 2, "Human", 2, tempprof, ageGen, 0, 0) 
            break
        elif pers == 2:
            ageGen = random.randint(210, 1110)
            tempprof = ""
            print("You've chosen 'Elf' as your character class!")
            player1 = Elf(nameinput, 1, 10, 10, 5, 5, 2, "Elf", 2, tempprof, ageGen, 0, 0) 
            break
        elif pers == 3:
            ageGen = random.randint(20, 60)
            tempprof = ""
            print("You've chosen 'Halfling' as your character class!")
            player1 = Halfling(nameinput, 1, 10, 10, 5, 5, 2, "Halfling", 2, tempprof, ageGen, 0, 0)
            break
        elif pers == 4:
            ageGen = random.randint(20, 60)
            tempprof = ""
            print("You've chosen 'Orc' as your character class!")
            player1 = Orc(nameinput, 1, 10, 10, 5, 5, 2, "Orc", 2, tempprof, ageGen, 0, 0)
            break
        elif pers == 5:
            ageGen = random.randint(20, 60)
            tempprof = ""
            print("You've chosen 'Dragonborn' as your character class!")
            player1 = Dragonborn(nameinput, 1, 10, 10, 5, 5, 2, "Dragonborn", 2, tempprof, ageGen, 10, 0)
            break
        else:
            print("Choose a valid character class.")
    if player1 != None:
        overwriteSave(player1)
    else:
        print("You have not created a character at this time.")
    overwriteSave()

def startMenu():
    case = True
    print("Welcome to the game!\n")
    while case:
        choice = 0
        choice = int(input("[1]Start an adventure\n[2]Exit the game\n"))
        if choice == 1:
            characterCreation()
        elif choice == 2:
            print("Closing the game...")
            time.sleep(3)
            sys.exit()
            #case = False
        else:
            print("Choose a valid input.")

def main():
    startMenu()
main()

