class Isik:
    def __init__(self, eesnimi, perekonnanimi, kvalifikatsioon=1):
        self.eesnimi = eesnimi
        self.perekonnanimi = perekonnanimi
        self.kvalifikatsioon = kvalifikatsioon

    def teave(self):
        return f"Eesnimi: {self.eesnimi}, Perekonnanimi: {self.perekonnanimi}, Kvalifikatsioon: {self.kvalifikatsioon}"

    def __del__(self):
        print(f"Hüvasti, härra {self.eesnimi} {self.perekonnanimi}!")


# Kolm Isiku klassi objekti loomine
isik1 = Isik("Steven", "Bogdanov", 3)
isik2 = Isik("Kristjan", "Kangur", 1)
isik3 = Isik("Gereth", "Soesoo", 2)

# Kuvatakse kogu töötajate teave
print(isik1.teave())
print(isik2.teave())
print(isik3.teave())

# Nõrgima lüli vallandamine
norgim = min(isik1.kvalifikatsioon, isik2.kvalifikatsioon, isik3.kvalifikatsioon)
if norgim == isik1.kvalifikatsioon:
    del isik1
elif norgim == isik2.kvalifikatsioon:
    del isik2
else:
    del isik3

# input funktsioon, et programm ei lõpetaks ennast kohe
input("Vajuta Enter, et programmist väljuda...")