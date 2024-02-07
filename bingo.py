# Impordi random moodul
import random

# Määra klass nimega Board
class Board:
    def __init__(self):
        # Algata eksemplarimuutujad
        self.position = {}  # Sõnastik numbrite asukohtade salvestamiseks laual
        self.playBoard = [  # 2D-list mängulaua esitamiseks
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
        ]
        self.bingo = {  # Sõnastik bingo oleku jälgimiseks
            "row" : [0,0,0,0,0],  # Loend märgitud numbrite arvu salvestamiseks igas reas
            "col" : [0,0,0,0,0],  # Loend märgitud numbrite arvu salvestamiseks igas veerus
            "diagonal" : [0,0]  # Loend märgitud numbrite arvu salvestamiseks igas diagonaalis
        }

        # Kutsu välja meetod createBoard mängulaua algatamiseks
        self.createBoard()

    # Meetod mängulaua loomiseks
    def createBoard(self):
        choices = [i for i in range(1,26)]  # Numbrite loend, millest valida
        for i in range(5):
            for j in range(5):
                choice = random.choice(choices)  # Vali juhuslikult number valikute loendist
                self.playBoard[i][j] = choice  # Määra valitud number mängulauale
                choices.pop(choices.index(choice))  # Eemalda valitud number valikute loendist
                self.position[choice] = (i,j)  # Salvesta valitud numbri asukoht positsiooni sõnastikku
    
    # Meetod mängulaua uuendamiseks, kui number on välja kutsutud
    def updateBoard(self, val):
        x,y = self.position[val]  # Hangi väljakutsutud numbri asukoht
        self.playBoard[x][y] = 'X'  # Märgi asukoht 'X'-ga, et näidata, et see on välja kutsutud
        self.updateBingo(x,y)  # Uuenda bingo olekut märgitud asukoha põhjal
    
    # Meetod bingo oleku uuendamiseks
    def updateBingo(self, x, y):
        self.bingo["row"][x] += 1  # Suurenda märgitud numbrite arvu vastavas reas
        self.bingo["col"][y] += 1  # Suurenda märgitud numbrite arvu vastavas veerus
        if x==y==2:
            self.bingo["diagonal"][0] += 1  # Suurenda märgitud numbrite arvu põhidiagonaalis
            self.bingo["diagonal"][1] += 1  # Suurenda märgitud numbrite arvu vastasdiagonaalis
        elif x==y:
            self.bingo["diagonal"][0] += 1  # Suurenda märgitud numbrite arvu põhidiagonaalis
        elif x+y == 4:
            self.bingo["diagonal"][1] += 1  # Suurenda märgitud numbrite arvu vastasdiagonaalis
    
    # Meetod kontrollimaks, kas on bingo
    def checkBingo(self):
        return 5 in self.bingo["row"] or 5 in self.bingo["col"] or 5 in self.bingo["diagonal"]

# Määra klass nimega Player, mis pärineb klassist Board
class Player(Board):
    def __init__(self, name):
        # Kutsu välja ülemklassi konstruktor
        super().__init__()
        # Algata eksemplarimuutujad
        self.name = name
        self.board = Board()  # Loo mängulaud mängijale
    
    # Meetod mängija laua uuendamiseks, kui number on välja kutsutud
    def updatePlayerBoard(self, val):
        self.board.updateBoard(val)
    
    # Meetod kontrollimaks, kas mängijal on bingo
    def checkBingo(self):
        return self.board.checkBingo()

# Määra klass nimega Game
class Game:
    # Meetod kahe mängija laudade kuvamiseks
    def displayBoard(self, player1, player2):
        board1 = player1.board.playBoard  # Hangi mängija 1 mängulaud
        board2 = player2.board.playBoard  # Hangi mängija 2 mängulaud
        size = 20  # Kuvatava laua suurus
        p1len = len(player1.name)  # Mängija 1 nime pikkus
        print(player1.name+" "*(size-p1len+1)+player2.name)  # Prindi mängijate nimed
        for i in range(5):
            for j in board1[i]:
                if j=='X':
                    print(f" {j}",end=" ")  # Prindi 'X' märgitud numbrite jaoks
                elif j>9:
                    print(j,end=" ")  # Prindi numbrid, mis on suuremad kui 9
                else:
                    print(f"0{j}",end=" ")  # Prindi numbrid, mis on väiksemad kui 10, eesliitega null
            print("      ",end="")
            for j in board2[i]:
                if j=='X':
                    print(f" {j}",end=" ")  # Prindi 'X' märgitud numbrite jaoks
                elif j>9:
                    print(j,end=" ")  # Prindi numbrid, mis on suuremad kui 9
                else:
                    print(f"0{j}",end=" ")  # Prindi numbrid, mis on väiksemad kui 10, eesliitega null
            print()
        print()

# Loo Game klassi eksemplar
game = Game()
# Loo kaks Player klassi eksemplari
player1 = Player(name="player1")
player2 = Player(name="player2")

# Kuva mängijate algseid laudu
game.displayBoard(player1, player2)

# Alusta mängutsüklit
while True:
    val = int(input(f"{player1.name}'s käik : "))  # Hangi number, mida mängija 1 välja kutsub
    player1.updatePlayerBoard(val)  # Uuenda mängija 1 lauda
    player2.updatePlayerBoard(val)  # Uuenda mängija 2 lauda
    game.displayBoard(player1,player2)  # Kuva uuendatud lauad

    # Kontrolli, kas on bingo
    if player1.checkBingo() and player2.checkBingo():
        print("VIKK")
        break
    if player1.checkBingo():
        print(f"{player1.name} VÕITIS")
        break
    if player2.checkBingo():
        print(f"{player2.name} VÕITIS")
        break
    

    val = int(input(f"{player1.name}'s käik : "))  # Hangi number, mida mängija 2 välja kutsub
    player1.updatePlayerBoard(val)  # Uuenda mängija 1 lauda
    player2.updatePlayerBoard(val)  # Uuenda mängija 2 lauda
    game.displayBoard(player1,player2)  # Kuva uuendatud lauad

    # Kontrolli, kas on bingo
    if player1.checkBingo() and player2.checkBingo():
        print("VIKK")
        break
    if player1.checkBingo():
        print(f"{player1.name} VÕITIS")
        break
    if player2.checkBingo():
        print(f"{player2.name} VÕITIS")
        break