import math

class cal():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def liitmine(self):
        return self.a + self.b

    def lahutamine(self):
        return self.a - self.b

    def korrutamine(self):
        return self.a * self.b

    def jagamine(self):
        return self.a / self.b

    def jaak(self):
        return self.a % self.b

    def astendamine(self):
        return self.a ** self.b

    def ruutjuur(self):
        return math.sqrt(self.a)

while True:

    a = int(input("Sisesta esimene number: "))
    b = int(input("Sisesta teine number: "))

    kalk = cal(a, b)

    def menu():
        x = ('1. Valin numbrid uuesti\n2. Liitmine \n3. Lahutamine\n4. Korrutamine\n5. Jagamine\n6. Jäägi leidmine\n7. Ruutjuure leidmine (leiab esimese arvu ruutjuure).\n8. Exit')
        print(x)

    while True:
        menu()
        valik = int(input('Sisesta üks valikutest: '))

        if valik == 1:
            a = int(input("Sisesta esimene number: "))
            b = int(input("Sisesta teine number: "))            
        elif valik == 2:
            print("Vastus: ", kalk.liitmine())            
        elif valik == 3:
            print("Vastus: ", kalk.lahutamine())            
        elif valik == 4:
            print("Vastus: ", kalk.korrutamine())           
        elif valik == 5:
            print("Vastus: ", kalk.jagamine())            
        elif valik == 6:
            print("Vastus: ", kalk.jaak())
        elif valik == 7:
            print("Vastus: ", kalk.ruutjuur())
        elif valik == 8:
            break
        else:
            print('Sisesta uuesti üks valikutest')

    break
