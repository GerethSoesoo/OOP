import random

class Sõdalane:
    def __init__(self, nimi, tervis):
        self.nimi = nimi
        self.tervis = tervis

    def ründa(self, vastane):
        print(f"{self.nimi} ründab {vastane.nimi}!")
        vastane.tervis -= 20
        print(f"{vastane.nimi} tervis: {vastane.tervis}\n")

# Küsi kasutajalt sõdurite nimed
sõdalane1_nimi = input("Sisesta esimese sõdalase nimi: ")
sõdalane2_nimi = input("Sisesta teise sõdalase nimi: ")

# Loome sõdalased kasutaja sisestatud nimedega
sõdalane1 = Sõdalane(sõdalane1_nimi, 100)
sõdalane2 = Sõdalane(sõdalane2_nimi, 100)

while sõdalane1.tervis > 0 and sõdalane2.tervis > 0:
    ründaja = random.choice([sõdalane1, sõdalane2])
    vastane = sõdalane1 if ründaja == sõdalane2 else sõdalane2
    ründaja.ründa(vastane)

if sõdalane1.tervis <= 0:
    print(f"{sõdalane2.nimi} võitis lahingu!")
else:
    print(f"{sõdalane1.nimi} võitis lahingu!")
