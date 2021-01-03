# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 18:16:27 2021

@author: Luka
"""

def unosKnjige(redniBroj):
    knjiga = {}
    knjiga['redniBroj'] = redniBroj
    knjiga['naslov'] = input("Unesite naslov knjige: ")
    knjiga['autor'] = input("Unesite autora knjige: ")
    knjiga['izdavac'] = input("Unesite izdavaca: ")
    knjiga['godina'] = input("Unesite godinu izdanja: ")
    return knjiga


def dodajKnjigu(knjige, knjiga):
    knjige.append(knjiga)
    return knjige

def stampajKnjigu(k):
    print("{0:<5}{1:40}{2:20}{3:20}{4:4}".format(k['redniBroj'], k['naslov'], k['autor'], k['izdavac'], k['godina']))
    
def stampajKnjige(knjige):
    print("{0:<5}{1:40}{2:20}{3:20}{4:4}".format('id', 'naslov', 'autor', 'izdavac', 'godina'))
    print("-"*90)
    for x in knjige:
        stampajKnjigu(x)
    
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
    print("{0:<5}{1:40}{2:20}{3:20}{4:4}".format('id', 'naslov', 'autor', 'izdavac', 'godina'))
    print("-"*90)
    for x in knjige:
        stampajKnjigu(x)
        
    # print("-"*90)
    # for k in knjige:
    #     stampajKnjigu(k)
        
    fajl = open("knjige.txt", 'a')
    for k in knjige:
        fajl.write(str(k['redniBroj']) + '|' + k['naslov'] + '|' + k['autor'] + '|' + k['izdavac'] + '|' + str(k['godina']) + '\n')
        
    fajl.close()