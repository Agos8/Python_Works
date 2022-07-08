class Persona():
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome

    def stampa(self):
        print(self.nome, self.cognome)

class Studente(Persona):
    def __init__(self, nome, cognome, istituto):
        super().__init__(nome, cognome)
        self.istituto = istituto

    def stampa_stud(self):
        print(self.nome, self.cognome, self.istituto)

class Insegnante(Persona):
    def __init__(self, nome, cognome, materia):
        super().__init__(nome, cognome)
        self.materia = materia

    def stampa_ins(self):
        print(self.nome, self.cognome, self.materia)

lista_stud = []
lista_ins = []

i = 0
while i != 3:
    x = input(" Chi sei? ")
    if x == "studente":
         nome_stud = input(" Studente dimmi il tuo nome ")
         cognome_stud = input(" Studente dimmi il tuo cognome ")
         istituto_stud = input(" Studente dimmi il tuo istituto ")
         Stud = Studente(nome_stud, cognome_stud, istituto_stud)
         Stud.stampa_stud()
         lista_stud.append(nome_stud)
         lista_stud.append(cognome_stud)
         lista_stud.append(istituto_stud)
    elif x == "insegnante":
         nome_ins = input(" Insegnante dimmi il tuo nome ")
         cognome_ins = input(" Insegnante dimmi il tuo cognome ")
         materia_ins = input(" Insegnante dimmi la materia che insegni ")
         Ins = Insegnante(nome_ins, cognome_ins, materia_ins)
         Ins.stampa_ins()
         lista_ins.append(nome_ins)
         lista_ins.append(cognome_ins)
         lista_ins.append(materia_ins)
    else: print(" Error 404")
    i += 1

Vista = input("\n Vuoi vedere tutti i dati delle LISTE??? ")
if Vista == "si":
    print("\n")
    print(lista_stud)
    print("\n")
    print(lista_ins)
    print("\n")
else:
    print(" Va bene! buona giornata ")
