import csv
import operator

def leggi_csv(sez):
    biblioteca = []
    with open("biblioteca.csv", "r", encoding='utf-8') as infile:
        sezioni = int(infile.readline().strip())
        for riga in infile:
            campi = riga.strip().split(",")
            if len(campi) < 5:
                continue
            libro = {
                "titolo": campi[0],
                "autore": campi[1],
                "anno": int(campi[2]),
                "pagine": int(campi[3]),
                "sezione": int(campi[4])
            }
            biblioteca.append(libro)

    print(biblioteca)
    return biblioteca


def aggiungi_libro(biblioteca):
    libro = {
                "titolo": input("inserisci il titolo del libro: "),
                "autore": input("inserisci il nome dell'autore: "),
                "anno": int((input("inserisci l'anno di pubblicazione: "))),
                "pagine": int(input("inserisci il numero di pagine: ")),
                "sezione": int(input("inserisci la sezione in cui vuoi mettere il libro: "))
            }
    biblioteca.append(libro)

def cerca_libro(biblioteca):
    nome_cerc=input("inserisci il titolo del libro che vuoi cercare nella biblioteca: ")
    for line in biblioteca:
        print(line)
        if line["titolo"]==nome_cerc:
            print(line)
        else:
            print("il titolo che hai cercato non esiste")
            break

def elenco_libri_sezione_per_titolo(biblioteca):
    sezione_cerc=int(input("inserisci la sezione della quale vuoi i libri ordinati alfabeticamente: "))
    ordi=[]
    for line in biblioteca:
        if line["sezione"]==sezione_cerc:
            ordi.append(line)
        ordi.sort(key=operator.itemgetter("titolo"))
        for line in ordi:
            print(line)



def main():
    sez = 0
    biblioteca = leggi_csv(sez)
    print("1. Carica biblioteca da file \n2. Aggiungi un nuovo libro  \n3. Cerca un libro per titolo   \n4. Ordina titoli di una sezione  \n5. Esci  \nScegli un'opzione >>")
    numero=int(input(""))
    while numero!=5:
        if numero==1:
            leggi_csv(sez)
        elif numero==2:
            aggiungi_libro(biblioteca)
        elif numero==3:
            cerca_libro(biblioteca)
        elif numero==4:
            elenco_libri_sezione_per_titolo(biblioteca)
        print("1. Carica biblioteca da file \n2. Aggiungi un nuovo libro  \n3. Cerca un libro per titolo   \n4. Ordina titoli di una sezione  \n5. Esci  \nScegli un'opzione >>")
        numero=int(input(""))

main()