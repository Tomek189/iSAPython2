class Animal(object):
    def __init__(self, imie):
        self.name = imie

    def say(self):
        print("Zwierzak {} nie mówi".format(self.name))

    def capitalize_name(self):
        self.name = str(self.name).capitalize()

class Horse(Animal):
    def __init__(self, imie):
        super().__init__(imie)

    def say(self):
        print("{} rży!".format(self.name))

    def jump(self):
        print("Koń {} skacze!".format(self.name))


class Donkey(Animal):
    def __init__(self, imie):
        super().__init__(imie)

    def say(self):
        print("iiiiiiiiiiihahahhaaaaaa jestem osioł")

    def run(self):
        print("Jestem uparty, ja nie biegam!")


class Mule(Horse, Donkey):

    def say(self):
        print("Muł mówi coś takiego:", end="")
        # super().say()
        # Donkey.say(self)
        Animal.say(self)

mul = Mule("muł edek")
mul.capitalize_name()
mul.say()
mul.run()
mul.jump()



# zwierz = Animal("ciasteczkowy potwór")
# zwierz.capitalize_name()
# zwierz.say()
# print()
# kon = Horse("gniady")
# kon.capitalize_name()
# kon.say()
# kon.jump()
#
# # zwierz.jump()
# print()
# osiol = Donkey("Uparciuch")
# osiol.capitalize_name()
# osiol.say()
# osiol.run()

# kon.run()
