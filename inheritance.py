class animal:
    def speaks(self):
        print("animal speaks")
class cat(animal):
    def meows(self):
        print("cat meows")
paka=cat()
paka.meows()
paka.speaks()