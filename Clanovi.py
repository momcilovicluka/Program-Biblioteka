# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 16:29:04 2021

@author: Luka
"""

def login(username, password):
    for c in clanovi:
        if c['korIme'] == username and c['lozinka'] == password:
            return True
    return False

def loadClanovi():
    for line in open('clanovi.txt', 'r').readlines():
        if len(line) > 1:
            clan = str2clan(line)
            clanovi.append(clan)
            
def str2clan(line):
    if line[-1] =='\n':
        line = line[:-1]
    ime, prezime, korIme, lozinka = line.split('|')
    clan = {'ime' : ime,
           'prezime' : prezime,
           'korIme' : korIme,
           'lozinka' : lozinka}
    return clan

def clan2str(clan):
    return '|'.join([clan['ime'], clan['prezime'], clan['korIme'], clan['lozinka']])

def formatHeader():
        print("Ime            |Prezime             |Korisnicko ime      |Lozinka        ")
        print("---------------+--------------------+--------------------+---------------")

def formatClan(clan):
    return u"{0:15}|{1:20}|{2:20}|{3:20}".format(clan['ime'], clan['prezime'], clan['korIme'], clan['lozinka']) + '\n'

def formatClanovi(clanList):
    result = ""
    for clan in clanList:
        result += formatClan(clan) + '\n'
    return result

def formatAllClanovi():
    result = ''
    for clan in clanovi:
        result += "{0:15}|{1:20}|{2:20}|{3:20}".format(clan['ime'], clan['prezime'], clan['korIme'], clan['lozinka']) + '\n'
    return result

def stampajClana(c):
    print("{0:15}|{1:20}|{2:20}|{3:20}".format(c['ime'], c['prezime'], c['korIme'], c['lozinka']))

def stampajClanove(clanovi):
    for x in clanovi:
        stampajClana(x)

def sortirajClanove(key):
    clanovi.sort(key = lambda x: x[key])

print(__name__)
clanovi = []
loadClanovi()