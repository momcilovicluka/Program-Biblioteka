# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 00:40:26 2021

@author: Luka
"""

def loadIzdate():
    for line in open('izdate.txt', 'r').readlines():
        if len(line) > 1:
            izdat = str2izdat(line)
            izdate.append(izdat)
            
def str2izdat(line):
    if line[-1] =='\n':
        line = line[:-1]
    korIme, redniBroj, datumIzdanja, datumVracanja = line.split('|')
    izdat = {'korIme' : korIme,
             'redniBroj' : redniBroj,
             'datumIzdanja' : datumIzdanja,
             'datumVracanja' : datumVracanja}
    return izdat
            
def dodajIzdat(izdate, izdat):
    izdate.append(izdat)
    return izdate

def save2file():
    fajl = open("izdate.txt", 'w')
    for i in izdate:
        fajl.write(i['korIme'] + '|' + (i['redniBroj'] + '|' + i['datumIzdanja'] + '|' + k['datumVracanja'] + '\n')

def stampajKnjigu(k):
    print("{0:<5}{1:40}{2:20}{3:20}{4:8}{5:4}".format(k['redniBroj'], k['naslov'], k['autor'], k['izdavac'], k['godina'], k['brKnjiga']))
    
def stampajKnjige(knjige):
    print("{0:<5}{1:40}{2:20}{3:20}{4:6}{5:4}".format('id', 'naslov', 'autor', 'izdavac', 'godina', 'brKnjiga'))
    print("-"*90)
    for x in knjige:
        stampajKnjigu(x)
        
print(__name__)
izdate = []
loadIzdate()