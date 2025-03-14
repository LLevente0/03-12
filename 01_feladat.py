"""1. Feladat
A mellékelt fájl néhány ismert programozási nyelv adatát tartalmazza.
Olvasd be a fájl tartalmát, és másold át azt egy fájlba úgy, hogy abba már csak a nyelv és az évszám kerüljön!
(Fájl letöltése: kattints a "Forrásfájl" feliratú gombra az egér jobb gombjával,
 és a felugró menüből válaszd a "Link mentése másként..." opciót!)"""


nyelv_ev = []

def kigyujtes():
    with open("Sourcew", "r", encoding="utf-8") as forrasfajl:
        for sor in forrasfajl:
            adatok = sor.strip().split(";")
            ev = adatok[0]
            programnyelv = adatok[1]
            nyelv_ev.append([ev, programnyelv])


    print(f"\nÉvek és nyelvek:\n {nyelv_ev}")


def fajliras():
    with open("Nyelv_ev.txt", "w", encoding="utf-8") as celfajl:
        print(f"\nÉvek és nyelvek:\n {nyelv_ev}", file=celfajl)



kigyujtes()
fajliras()



# nyelv = []
# evszam = []
#
# def kigyujtes():
#     with open("Sourcew", "r", encoding="utf-8") as forrasfajl:
#         for sor in forrasfajl:
#             adatok = sor.strip().split(";")
#             ev = adatok[0]
#             programnyelv = adatok[1]
#             nyelv.append(programnyelv)
#             evszam.append(ev)
#
#
#     print(f"Nyelvek:\n {nyelv}\n")
#     print(f"Évek:\n {evszam}")
#
# def fajliras():
#     with open("Nyelv_ev.txt", "w", encoding="utf-8") as celfajl:
#         print(f"Nyelvek:\n {nyelv}\n", file=celfajl)
#         print(f"\nÉvek:\n {evszam}", file=celfajl)
#
#
# kigyujtes()
# fajliras()