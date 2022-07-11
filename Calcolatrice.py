def addizione(x, y):
    a = x + y
    return a
def sottrazione(x, y):
    b = x - y
    return b
def moltiplicazione(x, y):
    c = x * y
    return c
def divisione(x, y):
    d = x / y
    return d


print("---------------- CALCOLATRICE ---------------")
operazione = int(input(""" Scegli il numero dell'operazione da svolgere:
1. ADDIZIONE 
2. SOTTRAZIONE
3. MOLTIPLICAZIONE
4. DIVISIONE
"""))

x = int(input("Dammi il valore X: "))
y = int(input("Dammi il valore Y: "))

if operazione == 1:
     print("Il risultato dell'Addizione è: ", addizione(x, y))
elif operazione == 2:
     print("Il risultato della Sottrazione è: ", sottrazione(x, y))
elif operazione == 3:
     print("Il risultato della Moltiplicazione è: ", moltiplicazione(x, y))
else: print("Il risultato della Divisione è: ", divisione(x, y))