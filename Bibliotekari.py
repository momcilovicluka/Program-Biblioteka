# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 16:29:04 2021

@author: Luka
"""

def login(username, password):
    for b in bibliotekari:
        if b['korIme'] == username and b['lozinka'] == password:
            return True
    return False

def loadBibl():
    for line in open('bibliotekari.txt', 'r').readlines():
        if len(line) > 1:
            bib = str2bib(line)
            bibliotekari.append(bib)
            
def str2bib(line):
    if line[-1] =='\n':
        line = line[:-1]
    korIme, lozinka = line.split('|')
    bib = {'korIme' : korIme,
           'lozinka' : lozinka}
    return bib

def bib2str(bib):
    return '|'.join([bib['ime'], bib['prezime'], bib['korIme'], bib['lozinka']])

print(__name__)
bibliotekari = []
loadBibl()