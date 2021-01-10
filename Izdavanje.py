# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 00:40:26 2021

@author: Luka
"""

import datetime as dt

def loadIzdate():
    for line in open('izdate.txt', 'r').readlines():
        if len(line) > 1:
            izdat = str2izdat(line)
            izdate.append(izdat)
            
def loadNajizdavanije():
    # for line in open('najizdavanije.txt', 'r').readlines():
    #     # print()
    #     if len(line) > 1:
    #         najizdavanija = str2najizdavanije(line)
    #         najizdavanije.append(najizdavanija)
    with open('najizdavanije.txt', 'r') as fajl:
        lista = fajl.read().splitlines()
        for r in lista:
            najizdavanija = str2najizdavanije(r)
            najizdavanije.append(najizdavanija)
            
            
def str2najizdavanije(line):
    if line[-1] =='\n':
        line = line[:-1]
    naslov, autor, brIzdavanja = line.split('|')
    najizdavanija = {'naslov' : naslov,
                     'autor' : autor,
                     'brIzdavanja' : int(brIzdavanja)}
    return najizdavanija
        
def str2izdat(line):
    if line[-1] =='\n':
        line = line[:-1]
    korIme, redniBroj, naslov, autor, datumIzdavanja, datumVracanja = line.split('|')
    izdat = {'korIme' : korIme,
             'redniBroj' : redniBroj,
             'naslov' : naslov,
             'autor' : autor,
             'datumIzdavanja' : datumIzdavanja,
             'datumVracanja' : datumVracanja}
    return izdat
            


def save2file():
    fajl = open("izdate.txt", 'w')
    for i in izdate:
        fajl.write(i['korIme'] + '|' + i['redniBroj'] + '|' + i['naslov'] + "|" + i['autor'] + "|"+ i['datumIzdavanja'] + '|' + i['datumVracanja'] + '\n')
        
def save2fileNajizdavanija():
    fajl = open("najizdavanije.txt", 'w')
    for n in najizdavanije:
        fajl.write(n['naslov'] + '|' +n['autor'] + '|' + str(n['brIzdavanja']) + '\n')

def dodajIzdat(izdate, izdat):
    izdate.append(izdat)
    return izdate

def dodajNajizdavanija(najizdavanije, najizdavanija):
    najizdavanije.append(najizdavanija)
    return najizdavanija

def formatHeader():
        print("korIme     |id   |naslov                                  |autor               |datumIzdavanja  |rokZaVracanje")
        print("-----------+-----+----------------------------------------+--------------------+----------------+-------------")

def stampajIzdat(i):
    print("{0:<11}|{1:5}|{2:40}|{3:20}|{4:16}|{5:16}".format(i['korIme'], i['redniBroj'], i['naslov'], i['autor'], i['datumIzdavanja'], i['datumVracanja']))
    
def stampajIzdate(izdate):
    #print("{0:<5}{1:40}{2:20}{3:20}{4:8}{5:4}".format('id', 'naslov', 'autor', 'izdavac', 'godina', 'brKnjiga'))
    #print("-"*101)
    formatHeader()
    for i in izdate:
        stampajIzdat(i)
        
def pronadjiIzdat(korIme):
    for i in izdate:
        if korIme == i['korIme']:
            return i
    return 0

def pronadjiIzdatNaslov(korIme):
    for i in izdate:
        if korIme == i['korIme']:
            danasnji = dt.datetime.today()
            danasnji.strftime("%d.%m.%Y.")
            datumIzdavanja = dt.datetime.strptime(i['datumIzdavanja'], "%d.%m.%Y.")
            razlika = (danasnji - datumIzdavanja).days
            if razlika > 30:
                print("Kasnite sa vracanjem knjige: " + i['naslov'] + ', autora: ' + i['autor'])
                
def pronadjiNajizdavanija(naslov, autor):
    for n in najizdavanije:
        if naslov == n['naslov'] and autor == n['autor']:
            return n
    return 0

def izmeniNajizdavanija(naslov, autor):
    for x in najizdavanije:
        if naslov == x['naslov'] and autor == x['autor']:
            x['brIzdavanja'] = str(int(x['brIzdavanja']) + 1)
    return 0

# def stampajKnjigu(k):
#     print("{0:<5}{1:40}{2:20}{3:20}{4:8}{5:4}".format(k['redniBroj'], k['naslov'], k['autor'], k['izdavac'], k['godina'], k['brKnjiga']))
    
# def stampajKnjige(knjige):
#     print("{0:<5}{1:40}{2:20}{3:20}{4:6}{5:4}".format('id', 'naslov', 'autor', 'izdavac', 'godina', 'brKnjiga'))
#     print("-"*90)
#     for x in knjige:
#         stampajKnjigu(x)

def sortirajIzdate(key):
    izdate.sort(key = lambda x: x[key])
    
def sortirajNajizdavanije(skey):
    return sorted(najizdavanije, key = lambda x: x[skey], reverse = True)

print(__name__)
izdate = []
loadIzdate()
najizdavanije = []
loadNajizdavanije()