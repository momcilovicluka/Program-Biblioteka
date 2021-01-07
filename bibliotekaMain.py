# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 19:02:53 2021

@author: Luka
"""

import Knjige
import Clanovi
import Bibliotekari
import datetime as dt

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
        while komanda != 'X':
            komanda = menu()
            if komanda == '1':
                stampajKnjige()
            elif komanda == '2':
                stampajClanove()
            elif komanda == '3':
                pronalazenjeKnjige()
            elif komanda == '4':
                pass
            elif komanda == '5':
                pass
            elif komanda == '6':
                pass
            elif komanda == '7':
                Knjige.main()
            elif komanda == '8':
                pass
            elif komanda == '9':
                izdavanje()
            elif komanda == '10':
                pass
            elif komanda == '11':
                pass
                
    else:
        while komanda != 'X':
            komanda = menuClan()
            if komanda == '1':
                stampajKnjige()
            elif komanda == '2':
                pronalazenjeKnjige()
            elif komanda == '3':
                izdavanje()
            elif komanda == '4':
                pass
    
    print("Dovidjenja.")

def menu():
    printMenu()
    command = input(">> ")
    while command.upper() not in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', 'X'):
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
    print(" 11 - grafikoni")
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
    Knjige.stampajKnjige(Knjige.knjige)
    
def stampajClanove():
    Clanovi.formatHeader()
    Clanovi.stampajClanove(Clanovi.clanovi)

def pronalazenjeKnjige():
    print("[Pronalazenje knjige] \n")
    naslov = input("Unesite naslov knjige >> ")
    knjiga = Knjige.pronadjiKnjigu(naslov)
    if(knjiga == 0):
        print("Knjiga nije pronadjena")
    else:
        print("{0:<5}{1:40}{2:20}{3:20}{4:8}{5:4}".format('id', 'naslov', 'autor', 'izdavac', 'godina', 'broj knjiga'))
        Knjige.stampajKnjigu(knjiga)
    
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
        print("{0:<5}{1:40}{2:20}{3:20}{4:8}{5:4}".format('id', 'naslov', 'autor', 'izdavac', 'godina', 'broj knjiga'))
        Knjige.stampajKnjigu(knjiga)
        if int(knjiga['brKnjiga']) >=1:
            if input("Potvrdite iznajmljivanje knjige (da/ne) >>") == "ne":
                print("Knjiga nije iznajmljenja")
                return 0
            izdavanje += knjiga['redniBroj'] + "|"
            datum = dt.date.today()
            izdavanje += str(datum) + "|"
            datum += dt.timedelta(days = 30)
            izdavanje += str(datum)
            fajl = open("izdate.txt", 'a')
            fajl.write(izdavanje + '\n')
            fajl.close()
            Knjige.izmeniBrojKnjiga(knjiga['redniBroj'], -1)
            Knjige.save2file()
            
        else:
            print("Trenutno nema slobodnih primeraka te knjige u biblioteci")

def funkcija():
    printMenu()
    fajl = open("clanovi.txt", 'r')
    clanovi = []
    for l in fajl:
        c = {}
        clan = l[:-1].split('|')
        c['Ime'] = clan[0]
        c['Prezime'] = clan[1]
        c['username'] = clan[2]
        c['password'] = clan[3]
        clanovi.append(c)
    fajl.close()
    
    fajl = open("bibliotekari.txt", 'r')
    bibliotekari = []
    for l in fajl:
        b = {}
        bibliotekar = l[:-1].split('|')
        b['username'] = bibliotekar[0]
        b['password'] = bibliotekar[1]
        bibliotekari.append(b)
    fajl.close()
    
    Knjige.main()


if __name__ == '__main__':
    main()