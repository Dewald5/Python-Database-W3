# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random
import sqlite3 as sql

outp = '' 
def rand():
    i = random(0,40)
    return i 

def remover():
    out = outp.replace('[(', '')
    out = out.replace(')]', '')
    print(out+'\n')    

Stonks = sql.connect('Stonks.db')

c = Stonks.cursor()
 #Ran all of this code to create the Database and to give its tables values

c.execute("""CREATE TABLE IF NOT EXISTS Chips(
  Simba integer,
  Lays integer,
  Pringles integer,
  Doritos integer,
  Ghostpops integer)""")
 
c.execute("""CREATE TABLE IF NOT EXISTS Cooldrinks(
  Coke integer,
  CokeL integer,
  Fant integer,
  FantaG integer,
  Sprite integer,
  CremeSoda integer        
  )""")
 
c.execute("""CREATE TABLE IF NOT EXISTS Chocolate(
  Cadbury integer,
  Tex integer,
  PS integer,
  Lunchbar integer,
  Barone integer          
  )""")
 
c.execute("""CREATE TABLE IF NOT EXISTS Pies(
  Pepper steak integer,
  Chicken integer,
  Mushroom integer,
  Beef integer,
  Sausage integer          
  )""")
 
c.execute("""CREATE TABLE IF NOT EXISTS Fruit(
  Pear integer,
  Apple integer,
  Orange integer
  Grape integer,
  Banana integer,
  Kiwi integer          
  )""")
 
c.execute("""CREATE TABLE IF NOT EXISTS Cupcakes(
  Vanilla integer,
  Chocolate integer,
  Caramel integer,
  Coffee integer,
  Bran integer          
  )""")
 
c.execute("""CREATE TABLE IF NOT EXISTS Veggies(
  Spinach integer,
  cabbage integer,
  Carrot integer,
  Beet integer,
  Potato integer,
  Pumpkin integer          
  )""")
 
Stonks.commit()
def values(): 
 c.execute("INSERT INTO Chips VALUES ('12','22','6','4','30')")
 c.execute("INSERT INTO Cooldrinks VALUES ('1','16','5','21','31','20')")
 c.execute("INSERT INTO Chocolate VALUES ('34','45','13','20','50')")
 c.execute("INSERT INTO Pies VALUES ('3','5','2','8','7')")
 c.execute("INSERT INTO Fruit VALUES ('9','14','7','6','11')")
 c.execute("INSERT INTO Cupcakes VALUES ('5','4','8','14','2')")
 c.execute("INSERT INTO Veggies VALUES ('9','4','7','10','13','6')")
 Stonks.commit()

with Stonks:
  c.execute("SELECT * FROM Chips")
  outp = str(c.fetchall())
  print("Chip Stock Levels: ")
  remover()
  
  c.execute("SELECT * FROM Cooldrinks")
  outp = str(c.fetchall())
  print("Cooldrinks Stock Levels:")
  remover()
  
  c.execute("SELECT * FROM Chocolate")
  outp = str(c.fetchall())
  print("Chocolate Stock Levels:")
  remover()
  
  c.execute("SELECT * FROM Pies")
  outp = str(c.fetchall())
  print("Pies Stock Levels:")
  remover()
  
  c.execute("SELECT * FROM Fruit")
  outp = str(c.fetchall())
  print("Fruit Stock Levels:")
  remover()
  
  c.execute("SELECT * FROM Cupcakes")
  outp = str(c.fetchall())
  print("Cupcakes Stock Levels:")
  remover()
  
  c.execute("SELECT * FROM Veggies")
  outp = str(c.fetchall())
  print("Veggies Stock Levels:")
  remover()