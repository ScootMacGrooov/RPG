from random import randint


class Dice:
    def die(num):
        die = randint(1, num)
        return die


class Character:
    def __init__(self, name, hp, thaco, ac, inventory, exp):
        self.name = name
        self.hp = hp
        self.thaco = thaco
        self.ac = ac
        self.inventory = inventory
        self.exp = exp


class Fighter(Character):
    def __init__(self):
        super().__init__(name=input("Wie ist dein Name, junger Abenteurer?"), thaco=20, ac=10,
                         hp=10, inventory={}, exp=10)

    prof = "Krieger"
    maxhp = 10
    level = 1
    hd = 10
    level2 = 20


class Cleric(Character):
    def __init__(self):
        super().__init__(name=input("Wie ist dein Name, junger Abenteurer?"), thaco=20, ac=10,
                         hp=8, inventory={}, exp=8)

    prof = "Kleriker"
    maxhp = 8
    level = 1
    hd = 8
    level2 = 15


class Mage(Character):
    def __init__(self):
        super().__init__(name=input("Wie ist dein Name, junger Abenteurer?"), thaco=20, ac=10,
                         hp=4, inventory={}, exp=4)

    prof = "Magier"
    mana = 10
    maxmana = 1
    maxhp = 4
    level = 1
    hd = 4
    level2 = 10


class Thief(Character):
    def __init__(self):
        super().__init__(name=input("Wie ist dein Name, junger Abenteurer?"), thaco=20, ac=10,
                         hp=6, inventory={}, exp=6)

    prof = "Dieb"
    stamina = 20
    maxstamina = 1
    maxhp = 6
    level = 1
    hd = 6
    level2 = 12


class Goblin(Character):
    def __init__(self):
        super().__init__(name="Kobold",
                         hp=(randint(3, 7)), thaco=20,
                         ac=6, inventory={},
                         exp=7)


class Ork(Character):
    def __init__(self):
        super().__init__(name="Ork",
                         hp=(randint(5, 9)), thaco=18,
                         ac=6, inventory={},
                         exp=12)


class Troll(Character):
    def __init__(self):
        super().__init__(name="Troll",
                         hp=(randint(10, 14)), thaco=18,
                         ac=6, inventory={},
                         exp=16)


def profession():
    print("Was ist deine Klasse?", '\n',
          "f für Krieger", '\n',
          "c für Kleriker", '\n',
          "m für Magier", '\n',
          "t für Dieb")
    pclass = input(">>>")
    if pclass == "f":
        Prof = Fighter()
    elif pclass == "c":
        Prof = Cleric()
    elif pclass == "m":
        Prof = Mage()
    elif pclass == "t":
        Prof = Thief()
    else:
        Prof = Fighter()
        # profession()
    return Prof


def ranmob():
    if Dice.die(5) <= 30:
        mob = Goblin()
        return mob
    if Dice.die(5) == 30:
        mob = Ork()
        return mob
    if Dice.die(5) <= 15:
        mob = Troll()
        return mob


def playerAttack():
    roll = Dice.die(20)
    if roll >= hero.thaco - mob.ac:
        print("Treffer")
        if hero.prof == "Krieger":
            rollD = Dice.die(10)

        if hero.prof == "Kleriker":
            rollD = Dice.die(6)

        if hero.prof == "Magier":
            rollD = Dice.die(4)
        if hero.prof == "Dieb":
            rollD = Dice.die(2)

        print("für", rollD, "Schaden")
        mob.hp -= rollD
        print(mob.name, "hat", mob.hp, "hp übrig")
    else:
        print("Daneben!")


def monsterAttack():
    roll = Dice.die(20)
    if roll >= mob.thaco - hero.ac:
        print("Monster Schaden")
        if mob.name == "Kobold":
            rollD = Dice.die(4)
        elif mob.name == "Ork":
            rollD = Dice.die(6)
        elif mob.name == "Troll":
            rollD = Dice.die(8)
        print("für", rollD, "Schaden")
        hero.hp -= rollD
        print(hero.name, "hat", hero.hp, "hp übrig")
    else:
        print(mob.name, "trifft daneben!")


def levelUp():
    while hero.exp >= hero.level2:
        levelGain = False
        hero.level += 1
        levelGain = True
        hero.level2 = hero.level2 * 2
        if levelGain == True:
            hero.maxhp += Dice.die(hero.hd)
            hero.hp = hero.maxhp
            if hero.prof == "Magier":
                hero.maxmana += 1
                hero.mana = hero.maxmana

            print("Levelaufstieg", "\n", 'hp:', hero.hp, "\n", 'Level:', hero.level)
            levelGain = False
    while hero.level >= 3:
        hero.level -= 3
        hero.thaco -= 1
        print("thaco:", hero.thaco)


def commands():
    if hero.prof == "Krieger":
        print(" drücke f für Kampf", '\n',
              "drücke enter für nichts")
        command = input("~~~~~~~~~Drücke eine Taste zum Weiterfahren.~~~~~~~")
        if command == "f":
            playerAttack()
        if command == "":
            pass

    if hero.prof == "Kleriker":
        print(" drücke f für Kampf", '\n',
              "drücke h zum heilen", '\n',
              "drücke enter für nichts")
        command = input("~~~~~~~~~Drücke eine Taste zum Weiterfahren.~~~~~~~")
        if command == "f":
            playerAttack()
        elif command == "h":
            if hero.hp < hero.maxhp:
                hero.hp += Dice.die(8)
                if hero.hp > hero.maxhp:
                    hero.hp = hero.hp - (hero.hp - hero.maxhp)
                print("du hast nun:", hero.hp, "hp")
            else:
                print("Deine hp sind voll")
                commands()
        elif command == "":
            pass
    if hero.prof == "Magier":
        print(" drücke f für Kampf", '\n',
              "drücke s für Sprüche", '\n',
              "drücke m um mana zu generieren", '\n',
              "drücke enter für nichts")
        command = input("~~~~~~~~~Drücke eine Taste zum Weiterfahren.~~~~~~~")
        if command == "f":
            playerAttack()
        elif command == "s":
            print("Du hast", hero.mana, "Mana")
            if hero.mana >= 1 and hero.mana < 3:
                print("drücke s für Schläferungsspruch", '\n',
                      "drücke m für magisches Projektil")
                command = input(">>>")
                if command == "s":
                    print("Das Monster schläft, es ist nun einfach zu töten.")
                    mob.hp -= mob.hp
                    hero.mana -= 1
                if command == "m":
                    if hero.mana < hero.maxmana:
                        hero.mana += Dice.die(4)
                        if hero.mana > hero.maxmana:
                            hero.mana -= (hero.mana - hero.maxmana)
                    dam = Dice.die(4) * hero.mana
                    mob.hp -= dam
                    print("Kein Mana! und du teilst", dam, "Schaden aus!")
                    hero.mana -= hero.mana
            elif hero.mana >= 3:
                print("drücke s für Schläferungsspruch", '\n',
                      "drücke m für magisches Projektil", '\n',
                      "drücke f für Feuerball")
                command = input(">>>")
                if command == "s":
                    print("Das Monster schläft, es ist nun einfach zu töten.")
                    mob.hp -= mob.hp
                    hero.mana -= 1
                if command == "m":
                    dam = Dice.die(4) * hero.mana
                    mob.hp -= dam
                    print("Kein Mana! und du teilst", dam, "Schaden aus!")
                    hero.mana -= hero.mana
                if command == "f":
                    print("Du bist temporär geblendet von einem Lichtblitz")
                    dam = 0
                    dam += Dice.die(6)
                    dam += Dice.die(6)
                    dam += Dice.die(6)
                    mob.hp -= dam
                    print("Du hast", dam, "Schaden angerichtet")

                    hero.mana -= 3
            else:
                print("Dein Mana ist leer")
                commands()
        elif command == "m":
            if hero.mana < hero.maxmana:
                hero.mana += 1
                print("Du hast", hero.mana, "Mana")
            elif hero.mana >= hero.maxmana:
                print("Dein Mana ist voll.")
                print("Du hast", hero.mana, "Mana")
                commands()

        elif command == "":
            pass

    if hero.prof == "Dieb":
        print(" drücke f für Kampf", '\n',
              "drücke s für spezial Attacken", '\n',
              "drücke enter für nichts")
        command = input("~~~~~~~~~Drücke eine Taste zum Weiterfahren.~~~~~~~")
        if command == "f":
            playerAttack()
        elif command == "s":
            print("Du hast", hero.stamina, "Stamina")
            if hero.stamina >= 1 and hero.stamina < 3:
                print("drücke k für kritischer Schlag")
                command = input(">>>")
                if command == "s":
                    print("Das Monster wurde am Kopf getroffen!")
                    mob.hp -= dam * 1.5
                    hero.mana -= 5
                    print("Kein Stamina! und du teilst", dam, "Schaden aus!")
                    hero.stamina -= hero.stamina
            elif hero.mana >= 3:
                print("drücke k für kritischer Schlag")
                command = input(">>>")
                if command == "s":
                    print("Das Monster wurde am Kopf getroffen!")
                    mob.hp -= dam * 1.5
                    hero.mana -= 5

                if command == "f":
                    dam = 0
                    dam += Dice.die(6)
                    dam += Dice.die(6)
                    dam += Dice.die(6)
                    mob.hp -= dam
                    print("Du hast", dam, "Schaden angerichtet")

                    hero.stamina -= 3
            else:
                print("Deine Stamina ist leer. Du bist erschöpft")
                commands()

        elif command == "":
            pass


mob = ranmob()
hero = profession()
print("|name|hp thaco|ac|inventar|xp|", '\n',
      hero.name, hero.hp, hero.thaco, hero.ac, hero.inventory, hero.exp)
while True:

    if mob.hp <= 0:
        print('Der', mob.name, 'ist tot!')
        hero.exp += mob.exp
        print('Held xp', hero.exp)
        mob = ranmob()
    if hero.hp <= 0:
        mob.exp += hero.exp
        print("Monster xp:", mob.exp)
        print(hero.name, 'ist gestorben!')
        # name=input("What is your characters name?")
        hero = profession()
        print("|name|hp thaco|ac|inventar|xp|", '\n',
              hero.name, hero.hp, hero.thaco, hero.ac, hero.inventory, hero.exp)

    levelUp()

    print("Du siehst", mob.name + ",", mob.name, "hat", mob.hp, "hp.")
    if hero.hp > 0:
        commands()
    if mob.hp > 0:
        monsterAttack()