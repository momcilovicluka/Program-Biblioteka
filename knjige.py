# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 18:16:27 2021

@author: Luka
"""

def loadKnjige():
    for line in open('knjige.txt', 'r').readlines():
        if len(line) > 1:
            knjiga = str2knjiga(line)
            knjige.append(knjiga)

def str2knjiga(line):
    if line[-1] =='\n':
        line = line[:-1]
    redniBroj, naslov, autor, izdavac, godina, brKnjiga = line.split('|')
    knjiga = {'redniBroj' : redniBroj,
              'naslov' : naslov,
              'autor' : autor,
              'izdavac' : izdavac,
              'godina' : godina,
              'brKnjiga' : brKnjiga}
    return knjiga

def unosKnjige(redniBroj):
    knjiga = {}
    knjiga['redniBroj'] = redniBroj
    knjiga['naslov'] = input("Unesite naslov knjige: ")
    knjiga['autor'] = input("Unesite autora knjige: ")
    knjiga['izdavac'] = input("Unesite izdavaca: ")
    knjiga['godina'] = input("Unesite godinu izdanja: ")
    knjiga['brKnjiga'] = input("Unesite broj knjiga u biblioteci: ")
    return knjiga


def dodajKnjigu(knjige, knjiga):
    knjige.append(knjiga)
    return knjige

def stampajKnjigu(k):
    print("{0:<5}{1:40}{2:20}{3:20}{4:8}{5:4}".format(k['redniBroj'], k['naslov'], k['autor'], k['izdavac'], k['godina'], k['brKnjiga']))
    
def stampajKnjige(knjige):
    print("{0:<5}{1:40}{2:20}{3:20}{4:6}{5:4}".format('id', 'naslov', 'autor', 'izdavac', 'godina', 'brKnjiga'))
    print("-"*90)
    for x in knjige:
        stampajKnjigu(x)
        
def pronadjiKnjigu(naslov):
    for x in knjige:
        if naslov == x['naslov']:
            return x 
    return 0

def izmeniBrojKnjiga(redniBroj, broj):
    for x in knjige:
        if redniBroj == x['redniBroj']:
            x['brKnjiga'] = str(int(x['brKnjiga']) + broj)
    return 0
        
def save2file():
    fajl = open("knjige.txt", 'w')
    for k in knjige:
        fajl.write(str(k['redniBroj']) + '|' + k['naslov'] + '|' + k['autor'] + '|' + k['izdavac'] + '|' + str(k['godina']) + "|" + str(k['brKnjiga'])+ '\n')

def main():
    fajl = open("knjige.txt", 'r')
    knjige = []
    for l in fajl:
        k = {}
        knjiga = l[:-1].split('|')
        k['redniBroj'] = knjiga[0]
        k['naslov'] = knjiga[1]
        k['autor'] = knjiga[2]
        k['izdavac'] = knjiga[3]
        k['godina'] = knjiga[4]
        k['brKnjiga'] = knjiga[5]
        knjige.append(k)
        
        # Ovako nije dobro!
        # naslovi = []
        # naslovi.append(k['naslov'])
        # autori = []
        # autori.append(k['autor'])
        
    fajl.close()
        
    stampajKnjige(knjige)
        
    redniBroj = int(knjige[-1]['redniBroj']) + 1
    print("\nUnosite knjige, Enter za kraj.")
    string = 'da'
    knjige = []
    while string != "":
        knjiga = unosKnjige(redniBroj)
        redniBroj += 1
        dodajKnjigu(knjige, knjiga)
        string = input("Da li ima jos knjiga? ")
    print("{0:<5}{1:40}{2:20}{3:20}{4:4}{5:4}".format('id', 'naslov', 'autor', 'izdavac', 'godina', 'brKnjiga'))
    print("-"*90)
    for x in knjige:
        stampajKnjigu(x)
        
    # print("-"*90)
    # for k in knjige:
    #     stampajKnjigu(k)
        
    fajl = open("knjige.txt", 'a')
    for k in knjige:
        fajl.write(str(k['redniBroj']) + '|' + k['naslov'] + '|' + k['autor'] + '|' + k['izdavac'] + '|' + str(k['godina']) + "|" + str(k['brKnjiga'])+ '\n')
        
    fajl.close()
    
print(__name__)
knjige = []
loadKnjige()