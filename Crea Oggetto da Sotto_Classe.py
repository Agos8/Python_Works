import random
class Animale:
    def __init__(self, zoo):
        self.zoo = zoo

    def Crea_Oggetto(self):
        ListaOggetti = []

        while True:
            print("\n","----------- ", self.zoo ," -----------")
            quale = int(input(""" Da quale SOTTO-CLASSE vuoi creare un OGGETTO? 
            1. FELINO
            2. CANIDE 
            3. UCCELLO
        
            """))

            simboli="""abcdefghilmnopqrstuvz"""
            oggetto = ""

            for x in range(4):
                oggetto += random.choice(simboli)   #genera una variabile casuale di 4 caratteri, in modo da istanziare più oggetti con nomi diversi
            
            ListaOggetti.append(oggetto)
            
            if    quale == 1:
                velocità = input("Dammi la Velocità del Felino ")
                oggetto = Felino(velocità)
            elif  quale == 2:
                zampe = input("Dammi le zampe ")
                oggetto = Canide(zampe)
                
            else: 
                ali = input("Dammi le ali ")
                oggetto = Uccello(ali)

            uscita = input("Vuoi creare un altro OGGETTO? ")
            if uscita != "si":
                break

        print("\n", "Ecco la lista degli oggetti creati: ")      
        print("\n".join(map(str, ListaOggetti)))

class Felino(Animale):
    def __init__(self, velocità):
        print("OGGETTO della Sotto-Classe \"Felino\" CREATO!", "\n")

class Canide(Animale):
    def __init__(self, zampe):
        print("OGGETTO della Sotto-Classe \"Canide\" CREATO!", "\n")
    
class Uccello(Animale):
    def __init__(self, ali):
        print("OGGETTO della Sotto-Classe \"Uccello\" CREATO!", "\n")


    
#main
x = Animale("BENVENUTI NELLO ZOO")
x.Crea_Oggetto()
