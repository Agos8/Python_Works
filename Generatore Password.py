
import random

def genera():
    print("""----- GENERA LA TUA PASSWORD -----""")
    simboli="""0123456789abcdefghilmnopqrstuvzABCDEFGHILMNOPQRSTUVZ,._!?"""
    lenght = int(input("""Scegli la lunghezza della Password """))
    password = ""
    for x in range(lenght):
        password += random.choice(simboli)
    print("\n Ecco la tua Password: ", password)

exit = "si"
while exit == "si":
    genera()
    exit = input("""\n VUOI UTILIZZARE DI NUOVO IL GENERATORE?
    Premi si per continuare
    Premi altro per uscire... """)
   
