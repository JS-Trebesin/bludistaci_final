import csv, sys

cesta = "D:\\Documents\\py\\sandbox\\bludistaci\\data.csv"


def main():
    bludistaci = {}

    nacist_data(bludistaci)

    print("Vítej uživateli")
    print("Zvol možnost: ")
    print("Pro vypsání všech Bludišťáků zvol 1")
    print("Pro vypsání jednoho studenta zvol 2")
    print("Pro přidání Bludišťáka zvol 3")
    print("Pro odebrání Bludišťáka zvol 4")
    print("Pro vypsání nejlepšího studenta zvol 5")
    print("Pro přidání studenta zvol 6")
    print("Pro ukončení zvol 7")

    while True:
        try:
            zvolena_moznost = int(input())
            break
        except ValueError:
            print("Nezadal/a jsi číslo. Zadej číslo.")

    match zvolena_moznost:
        case 1:
            vypis_vse(bludistaci)
        case 2:
            vypis_bludistaky_pro(bludistaci)
        case 3:
            pridej_bludistaka(bludistaci)
        case 4:
            odeber_bludistaka(bludistaci)
        case 5:
            nejvyssi_skore(bludistaci)
        case 6:
            pridej_studenta(bludistaci)
        case 7:
            print("Bye!")
            sys.exit()
        case _:
            print("Zvol číslo mezi 1 - 6")

    uloz_data(bludistaci)


def vypis_bludistaky_pro(bludistaci):
    jmeno = input("Koho chceš zkontrolovat? ").capitalize()
    print(jmeno, bludistaci[jmeno])


def vypis_vse(bludistaci):
    for i in bludistaci:
        print(i, bludistaci[i])


def pridej_bludistaka(bludistaci):
    pridat = input("Komu chceš bludišťáka přidat? ").capitalize()
    bludistaci[pridat] += 1
    print(pridat, bludistaci[pridat])


def odeber_bludistaka(bludistaci):
    odebrat = input("Komu chceš bludišťáka odebrat? ").capitalize()
    bludistaci[odebrat] -= 1
    print(odebrat, bludistaci[odebrat])


def pridej_studenta(bludistaci):
    student = input("Přidej studenta/ku: ").capitalize()
    bludistaci[student] = 1
    print(student, bludistaci[student])


def nejvyssi_skore(bludistaci):
    nejvic = max(bludistaci, key=bludistaci.get)
    print("Nejvíce bludišťáku má: ")
    print(nejvic, bludistaci[nejvic])


def nacist_data(bludistaci):
    with open(cesta, "r", newline="") as f:
        reader = csv.reader(f, delimiter=",")
        for x in reader:
            bludistaci[x[0]] = int(x[1])


def uloz_data(bludistaci):
    with open(cesta, "w", newline="") as f:
        writer = csv.writer(f, delimiter=",")
        for x in bludistaci:
            writer.writerow([x, bludistaci[x]])


if __name__ == "__main__":
    main()
