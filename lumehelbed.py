class Lumi:
    # Defineerime klassi Lumi
    def __init__(self, helveste_arv):
        # Konstruktor, mis võtab argumendiks helveste_arvu ja seatab selle objekti omaduseks
        self.helveste_arv = helveste_arv

    def __add__(self, n):
        # Ülekoormatud meetod __add__, mis võimaldab helveste_arvu suurendada
        self.helveste_arv += n
        return self

    def __sub__(self, n):
        # Ülekoormatud meetod __sub__, mis võimaldab helveste_arvu vähendada
        self.helveste_arv -= n
        return self

    def __mul__(self, n):
        # Ülekoormatud meetod __mul__, mis võimaldab helveste_arvu korrutada
        self.helveste_arv *= n
        return self

    def __truediv__(self, n):
        # Ülekoormatud meetod __truediv__, mis võimaldab helveste_arvu jagada
        # Arvutame täisarvulise jagamise, kasutades int(), ning salvestame tulemuse helveste_arvuks
        self.helveste_arv = int(self.helveste_arv / n)
        return self

    def makeSnow(self):
        # Meetod makeSnow, mis loob stringi lumehelveste kujutisega
        snowflake_row = '*' * self.helveste_arv
        snowfall = '\n'.join([snowflake_row] * self.helveste_arv)
        return snowfall

    def __repr__(self):
        # Ülekoormatud meetod __repr__, mis tagastab objekti esitusena stringi
        return f"Lumi({self.helveste_arv})"


# Testime klassi meetodeid
lumi = Lumi(3)  # Loome Lumi objekti, kus on 3 lumehelvest
print(lumi.makeSnow())  # Väljastab:
# ***
# ***
# ***
lumi += 2  # Suurendame helveste arvu 2 võrra
print(lumi.makeSnow())  # Väljastab:
# *****
# *****
# *****
lumi -= 1  # Vähendame helveste arvu 1 võrra
print(lumi.makeSnow())  # Väljastab:
# *****
# *****
# *****
# *
lumi *= 2  # Korrutame helveste arvu 2-ga
print(lumi.makeSnow())  # Väljastab:
# ********
# ********
# ********
# **
lumi /= 3  # Jagame helveste arvu 3-ga
print(lumi.makeSnow())  # Väljastab:
# ***
# ***
# ***
