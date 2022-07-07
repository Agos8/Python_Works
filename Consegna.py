
# ES.1   CREARE UN SISTEMA CHE PRENDA IN INPUT UN DATO E LO STAMPI DOPO AVER CONTROLLATO CHE NON ABBIA VALORE FALSE
Dato = input("Inserisci il dato")
if(Dato != False):
   print("OTTIMO! ecco il tuo dato: "+Dato)
else:
   print("Il tuo dato è False!")


   
# ES.2   CREARE UNA SERIE DI INPUT INSERIRLI IN UNA LISTA E STAMPARLI CONTROLLANDO CHE NON ABBIANO VALORE FALSE

Dato1 = (input("Dammi il primo input "))
Dato2 = (input("Dammi il secondo input "))
Dato3 = (input("Dammi il terzo input "))

Lista = [Dato1, Dato2, Dato3]

if(Dato1 != False and Dato2 != False and Dato3 != False):
   print(Lista)
else:
   print("è presente un valore False! ")

# ES.3   CREARE UN SISTEMA DI DOMANDE E INPUT CHE INSERISCANO E CONTROLLINO I DATI SE NON SONO CORRETTI NON VERRANNO INSERIRTI NELLA LISTA
Nome = input("Come ti chiami? ")
Età = input("Quanti anni hai? ")
Citta = input("Da dove vieni? ")
if(Nome == "Agostino" and Età == "26" and Citta == "Milano"):
    Lista = [Nome, Età, Citta]
    print("Complimenti sei la persona giusta! ")
    print(Lista)
else:
   print("Error 404")
