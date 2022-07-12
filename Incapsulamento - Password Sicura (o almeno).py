# PASSWORD SICURA (o almeno)
class Login:

    def __init__(self):
        self.__password = ""

    def Inserisci(self):
        self.__password = input("Inserisci la tua password")

    def Reimposta(self):
        self.__password = input("Reimposta la tua password")
        return self.__password
    
    def Stampa(self):
        print(self.__password)

# Istanza di classe
x = Login()

# Inserisci password
x.Inserisci()
print("Ecco la password inserita")
x.__password = "ciao"  #non permette la modifica
x.Stampa()

# Modifica password
re = input("Vuoi reimpostare la tua passwor??? ")
if re == "si":
    x.Reimposta()

# Stampa
x.__password = "ciao"   #non permette la modifica
x.Stampa()


