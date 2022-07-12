import yaml
class Ospedale:
    def PagaOre(self):
        print("Elenco DOTTORI: ")
        print(yaml.dump(dict_doctor, sort_keys=False, default_flow_style=False),"\n")

        print("Elenco SPECIALIZZANDI: ")
        print(yaml.dump(dict_doctor, sort_keys=False, default_flow_style=False))

        cond = input("Vuoi Pagare i dipendenti?")
        if cond == "si":
            dict_doctor.clear()
            dict_special.clear()
            print("OK non hai debiti")
        else: 
            print("NON SFRUTTARE I DIPENDENTI!")

class Dottore(Ospedale):
    def SegnaOre(self):
        while True:
            nome=input("Nome del DOTTORE? ")
            ore= int(input("Ore del DOTTORE? "))
            dict_doctor.update({nome: ore})
            contr = input("Vuoi inserire un altro dottore?")
            if contr != "si":
                break

class Specializzando(Ospedale):
    def SegnaOre(self):
        while True:
            nome=input("Nome dello SPECIALIZZANDO? ")
            ore= int(input("Ore dello SPECIALIZZANDO? "))
            dict_doctor.update({nome: ore})
            contr = input("Vuoi inserire un altro specializzando?")
            if contr != "si":
                break
#main
dict_doctor = {}
dict_special = {}

a = Ospedale()
b = Dottore()
c = Specializzando()

b.SegnaOre()
c.SegnaOre()
a.PagaOre()
