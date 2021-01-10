# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 19:02:53 2021

@author: Luka
"""

import Knjige
import Clanovi
import Bibliotekari
import Izdavanje
import datetime as dt
import matplotlib.pyplot as plt

JE_BIBLIOTEKAR = False
USERNAME = ""

def main():
    print()
    print("Program Biblioteka")
    print("==================")
    print()
    if not login():
        print("\nNiste uneli postojece ime i lozinku!")
        return
    
    komanda = '0'
    if(JE_BIBLIOTEKAR):
        print("Ulogovani ste kao bibliotekar")
        while komanda != 'X':
            komanda = menu()
            if komanda == '1':
                stampajKnjige()
            elif komanda == '2':
                stampajClanove()
            elif komanda == '3':
                pronalazenjeKnjige()
            elif komanda == '4':
                pronalazenjeClana()
            elif komanda == '5':
                izmenaKnjige()
            elif komanda == '6':
                izmenaClana()
            elif komanda == '7':
                Knjige.main()
            elif komanda == '8':
                dodavanjeClana()
            elif komanda == '9':
                izdavanje()
            elif komanda == '10':
                vracanje()
            elif komanda == '11':
                izdateKnjige()
            elif komanda == '12':
                grafikon()
                
    else:
        Izdavanje.pronadjiIzdatNaslov(USERNAME)
        print("Ulogovani ste kao clan biblioteke")
        while komanda != 'X':
            komanda = menuClan()
            if komanda == '1':
                stampajKnjige()
            elif komanda == '2':
                pronalazenjeKnjige()
            elif komanda == '3':
                izdavanje()
            elif komanda == '4':
                vracanje()
    
    print("Dovidjenja.")

def menu():
    printMenu()
    command = input(">> ")
    while command.upper() not in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', 'X'):
        print("\nUneli ste pogresnu komandu.\n")
        printMenu()
        command = input(">> ")
    return command.upper()

def menuClan():
    printMenuClan()
    command = input(">> ")
    while command.upper() not in ('1', '2', '3', '4', 'X'):
        print("\nUneli ste pogresnu komandu.\n")
        printMenuClan()
        command = input(">> ")
    return command.upper()
    


def printMenu():
    print("\nIzaberite opciju:")
    print(" 1  - prikaz knjiga")
    print(" 2  - prikaz clanova")
    print(" 3  - pronalazenje knjige")
    print(" 4  - pronalazenje clana")
    print(" 5  - izmena podataka o knjizi")
    print(" 6  - izmena podataka o clanu")
    print(" 7  - dodavanje knjige")
    print(" 8  - dodavanje clana")
    print(" 9  - izdavanje knjige")
    print(" 10 - vracanje knjige")
    print(" 11 - izdate knjige")
    print(" 12 - grafikon")
    print(" x  - izlaz iz programa\n")
    
def printMenuClan():
    print("\nIzaberite opciju:")
    print(" 1 - prikaz knjiga")
    print(" 2 - pronalazenje knjige")
    print(" 3 - izdavanje knjige")
    print(" 4 - vracanje knjige")
    print(" x - izlaz iz programa\n")

def login():
    username = input("Unesite korisnicko ime: ")
    password = input("Unesite lozinku: ")
    global USERNAME
    USERNAME = username
    if Bibliotekari.login(username, password):
        global JE_BIBLIOTEKAR
        JE_BIBLIOTEKAR = True
        return 1
    elif Clanovi.login(username, password):
        return 2
    return 0

def stampajKnjige():
    print("[Stampanje knjiga] \n")
    print("Da li zelite da knjige budu sortirane?")
    print(" 1 - naslov")
    print(" 2 - autor")
    print(" 3 - izdavac")
    print(" 4 - godinaIzdanja")
    print(" 5 - default\n\n>>")
    command = input(">> ")
    while command not in ('1', '2', '3', '4', '5'):
        print("\nUneli ste pogresnu komandu.\n")
        command = input(">> ")
    if command == '1':
        Knjige.sortirajKnjige('naslov')
    elif command == '2':
        Knjige.sortirajKnjige('autor')
    elif command == '3':
        Knjige.sortirajKnjige('izdavac')
    elif command == '4':
        Knjige.sortirajKnjige('godina')
        
    Knjige.stampajKnjige(Knjige.knjige)
    
def stampajClanove():
    print("[Stampanje clanova] \n")
    print("Da li zelite da clanovi budu sortirani?")
    print(" 1 - ime")
    print(" 2 - prezime")
    print(" 3 - korisnicko ime")
    print(" 4 - bez sortiranja\n\n>>")
    command = input(">> ")
    while command not in ('1', '2', '3', '4'):
        print("\nUneli ste pogresnu komandu.\n")
        command = input(">> ")
    if command == '1':
        Clanovi.sortirajClanove('ime')
    elif command == '2':
        Clanovi.sortirajClanove('prezime')
    elif command == '3':
        Clanovi.sortirajClanove('korIme')
    Clanovi.formatHeader()
    Clanovi.stampajClanove(Clanovi.clanovi)

def pronalazenjeKnjige():
    print("[Pronalazenje knjige] \n")
    naslov = input("Unesite naslov knjige >> ")
    knjige = Knjige.pronadjiKnjigu(naslov.lower())
    if not knjige:
        print("Knjiga nije pronadjena")
    else:
        #print("{0:<5}{1:40}{2:20}{3:20}{4:8}{5:4}".format('id', 'naslov', 'autor', 'izdavac', 'godina', 'broj knjiga'))
        Knjige.stampajKnjige(knjige)

def pronalazenjeClana():
    print("[Pronalazenje clana] \n")
    ImeIPrezime = input("Unesite ime i prezime clana >> ")
    try:
        ime, prezime = ImeIPrezime.split(" ")
    except:
        print("Niste ispravno uneli ime i prezime")
        return
    if not Clanovi.clanPostojiImePrezime(ime, prezime):
        print("Clan ne postoji")
        return
    clanovi = Clanovi.pronadjiClana(ime, prezime)
    Clanovi.formatHeader()
    Clanovi.stampajClanove(clanovi)
    
def izmenaKnjige():
    print("[Izmena knjige] \n")
    stampajKnjige()
    redniBroj = input("Unesite redni broj knjige koju zelite da izmenite >>")
    if not Knjige.knjigaPostoji(redniBroj):
        print("Ne postoji knjiga sa tim rednim brojem")
        return
    #print("{0:<5}{1:40}{2:20}{3:20}{4:8}{5:4}".format('id', 'naslov', 'autor', 'izdavac', 'godina', 'broj knjiga'))
    Knjige.formatHeader()
    Knjige.stampajKnjigu(Knjige.pronadjiKnjiguRedniBroj(redniBroj))
    Knjige.izmeniKnjigu(redniBroj)
    Knjige.save2file()
    
def izmenaClana():
    print("[Izmena clana] \n")
    stampajClanove()
    korIme = input("Unesite korisnicko ime clana kojeg zelite da izmenite >>")
    if not Clanovi.clanPostoji(korIme):
        print("Ne postoji clan sa tim korisnickim imenom")
        return
    
    odgovor = input("Da li zelite da izbrisete clana (da/ne) >>")
    if odgovor == "da":
        for c in range(len(Clanovi.clanovi)):
            if Clanovi.clanovi[c]['korIme'] == korIme:
                del Clanovi.clanovi[c]
                print("Clan je izbrisan")
                break
    else:
        Clanovi.izmeniClana(korIme)
    Clanovi.save2file()
    Clanovi.clanovi.clear()
    Clanovi.loadClanovi()

def izdavanje():
    print("[Izdavanje knjige] \n")
    izdavanje = ""
    if JE_BIBLIOTEKAR:
        global USERNAME
        USERNAME = input("Unesite korisnicko ime clana: ")
        if not Clanovi.clanPostoji(USERNAME):
            print("Clan ne postoji")
            return
    izdavanje += USERNAME + "|"
    naslov = input("Unesite naslov knjige >> ")
    knjiga = Knjige.pronadjiKnjigu(naslov)
    if(knjiga == 0):
        print("Knjiga nije pronadjena")
        return
    else:
        #print("{0:<5}{1:40}{2:20}{3:20}{4:8}{5:4}".format('id', 'naslov', 'autor', 'izdavac', 'godina', 'broj knjiga'))
        Knjige.formatHeader()
        Knjige.stampajKnjigu(knjiga)
        if int(knjiga['brKnjiga']) >=1:
            if input("Potvrdite iznajmljivanje knjige (da/ne) >>") == "ne":
                print("Knjiga nije iznajmljenja")
                return 0
            izdavanje += knjiga['redniBroj'] + "|" + knjiga['naslov'] + "|" + knjiga['autor'] + "|"
            if Izdavanje.pronadjiNajizdavanija(knjiga['naslov'], knjiga['autor']) == 0:
                najIzdavanije = knjiga['naslov'] + "|" + knjiga['autor'] + "|" + "1"
                fajl = open("najizdavanije.txt", 'a')
                fajl.write(najIzdavanije + '\n')
                fajl.close()
            else:
                Izdavanje.izmeniNajizdavanija(knjiga['naslov'], knjiga['autor'])
                Izdavanje.save2fileNajizdavanija()
            datum = dt.date.today()
            izdavanje += str(datum.strftime("%d.%m.%Y.")) + "|"
            datum += dt.timedelta(days = 30)
            izdavanje += str(datum.strftime("%d.%m.%Y."))
            fajl = open("izdate.txt", 'a')
            fajl.write(izdavanje + '\n')
            fajl.close()
            Izdavanje.izdate.clear()
            Izdavanje.loadIzdate()
            Knjige.izmeniBrojKnjiga(knjiga['redniBroj'], -1)
            Knjige.save2file()
            
        else:
            print("\nTrenutno nema slobodnih primeraka te knjige u biblioteci")

def vracanje():
    print("[Vracanje knjige] \n")
    if JE_BIBLIOTEKAR:
        global USERNAME
        USERNAME = input("Unesite korisnicko ime clana: ")
        if not Clanovi.clanPostoji(USERNAME):
            print("Clan ne postoji")
            return
    naslov = input("Unesite naslov knjige >> ")
    knjiga = Knjige.pronadjiKnjigu(naslov)
    if(knjiga == 0):
        print("Knjiga nije pronadjena")
        return
    else:
        for i in range(len(Izdavanje.izdate)):
            if Izdavanje.izdate[i]['korIme'] == USERNAME and Izdavanje.izdate[i]['naslov'] == naslov:
                del Izdavanje.izdate[i]
                Izdavanje.save2file()
                Izdavanje.loadIzdate()
                print("Knjiga je vracena")
                return
        print("Korisnik nije iznajmio tu knjigu")
        
        
def grafikon():
    print("[Najprodavanije knjige] \n")
    x_podaci = []
    y_podaci = []
    Izdavanje.najizdavanije.clear()
    Izdavanje.loadNajizdavanije()
    Izdavanje.najizdavanije = Izdavanje.sortirajNajizdavanije('brIzdavanja')
    Izdavanje.save2fileNajizdavanija()
    for i in Izdavanje.najizdavanije[:5]:
        y_podaci.append(int(i['brIzdavanja']))
        x_podaci.append(i['naslov'] + '\n' + i['autor'])
    plt.bar(x_podaci, y_podaci)
    plt.xlabel('Knjige')
    plt.xticks(rotation = 90)
    plt.ylabel('Broj izdavanja')
    plt.show()
    

def dodavanjeClana():
    print("[Dodavanje clana] \n")
    ime = input("Unesite ime >>")
    prezime = input("Unesite prezime >>")
    korIme = input("Unesite korisnicko ime >> ")
    while Clanovi.clanPostoji(korIme) or Bibliotekari.bibliotekarPostoji(korIme):
        print("Korisnicko ime vec postoji")
        korIme = input("Unesite korisnicko ime >> ")
    lozinka = input("Unesite lozinku >> ")
    clan = {'ime' : ime, 'prezime' : prezime, 'korIme' : korIme, 'lozinka' : lozinka}
    Clanovi.formatHeader()
    Clanovi.stampajClana(clan)
    Clanovi.clanovi = Clanovi.dodajClana(Clanovi.clanovi, clan)
    Clanovi.save2file()

def izdateKnjige():
    print("[Izdate knjige] \n")
    Izdavanje.stampajIzdate(Izdavanje.izdate)

# def funkcija():
#     printMenu()
#     fajl = open("clanovi.txt", 'r')
#     clanovi = []
#     for l in fajl:
#         c = {}
#         clan = l[:-1].split('|')
#         c['Ime'] = clan[0]
#         c['Prezime'] = clan[1]
#         c['username'] = clan[2]
#         c['password'] = clan[3]
#         clanovi.append(c)
#     fajl.close()
    
#     fajl = open("bibliotekari.txt", 'r')
#     bibliotekari = []
#     for l in fajl:
#         b = {}
#         bibliotekar = l[:-1].split('|')
#         b['username'] = bibliotekar[0]
#         b['password'] = bibliotekar[1]
#         bibliotekari.append(b)
#     fajl.close()
    
#     Knjige.main()


if __name__ == '__main__':
    main()