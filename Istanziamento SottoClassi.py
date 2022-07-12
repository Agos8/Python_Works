class Fabbrica:
    def __init__(self, nome):
        self.nome = nome

    def Istanzia(self):
        h = Operaio()
        p = CapoTurno()
        t = CapoReparto()

        print("---------------- ", self.nome, " ---------------")
        cosa = int(input(""" Scegli il numero dell'operazione da svolgere:
        1. Visualizza OPERAIO 
        2. Visualizza CAPO-TURNO 
        3. Visualizza CAPO-REPARTO
      
        """))
        
        quante = int(input("Quante volte vuoi vederlo? "))
        i = 0
        while i < quante:
            if cosa == 1:
                 h.__init__()
            elif cosa == 2:
                 p.__init__()
            else: 
                 t.__init__()
            i += 1
             

class Operaio(Fabbrica):
    def __init__(self):
        print("Ciao sono un OPERAIO")

class CapoTurno(Fabbrica):
    def __init__(self):
        print("Ciao sono il CAPO-TURNO")
    
class CapoReparto(Fabbrica):
    def __init__(self):
        print("Ciao sono il CAPO-REPARTO")
    
#main
x = Fabbrica("BENVENUTI IN FERRERO")
x.Istanzia()