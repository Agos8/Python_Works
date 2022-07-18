import json

def inserisci(lista):
    global x
    x = json.dumps(lista)
    print(x)


def carica(dato):
    y = json.loads(x)
    print(y[dato])


regioni = []
while True:
            print("\n","----------- HOME -----------")
            risp = int(input("""Cosa vuoi fare??? 
            1. INSERIRE 
            2. CARICARE
    
                """))
            if risp == 1:
                while True:
                    reg = input("Inserisci una regione:  ")
                    regioni.append(reg)   
                    continua = input("Vuoi inserire un'altra regione???  ")   
                    if continua != "si":   
                        inserisci(regioni)
                        break 
            else: 
                if len(regioni) == 0:
                    print("ERROR 404.. non sono presenti dati ")
                else:
                    print(regioni)
                    quale = int(input("Dimmi l'indice di posizione del dato che vuoi caricare???  "))
                    carica(quale)


