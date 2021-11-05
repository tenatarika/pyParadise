
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 18:46:30 2021

@author: furcas
"""

from random import randrange





class Hero():
    def __init__(self, team):

        self._id = randrange(0, 99999999)
        self.team = team
        self._lvl = 0
        self.army = list()
        
        
    def lvl_up(self):
        self._lvl = self._lvl + 1 
        
class GreateHero(Hero):
    def lvl_up(self):
        return super().lvl_up()*2
        

class Solder():
    def __init__(self, team):
        self._id = randrange(0, 99999999)
        self.team = team
        
        
    def going_for(self):
        print(self._id)
        
        
class Game():
    
    hero1 = Hero(1)
    hero2 = Hero(2)
    for i in range(randrange(0, 10)):
        solder = Solder(1)
        hero1.army.append(solder) 
        hero1.army[i].going_for()
    for i in range(randrange(0, 10)):    
        hero2.army.append(solder)
        hero2.army[i].going_for()
    if len(hero1.army) > len(hero2.army):
        hero1.lvl_up()
        
    else:
        hero2.lvl_up()
        
    print(hero1._lvl, hero2._lvl)