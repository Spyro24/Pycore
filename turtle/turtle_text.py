from turtle import *

#Maked Letters: S, A

def set_pos(pos1,pos2):
    up()
    goto(pos1,pos2)
    down()

def S(size):
    down()
    fd(2*size)
    left(90)
    fd(2*size)
    left(90)
    fd(2*size)
    right(90)
    fd(2*size)
    right(90)
    fd(2*size)
    
def A(size):
    down
    left(90)
    fd(4*size)
    right(90)
    fd(2*size)
    right(90)
    fd(4*size)
    back(2*size)
    right(90)
    fd(2*size)
    back(2*size)
    right(90)
    fd(2*size)
    right(90)
    
def D(size):
    left(90); fd(4*size)
    right(90);fd(1*size)
    right(45);fd(1.5*size)
    right(45);fd(2*size)
    right(45);fd(1.35*size)
    right(45);fd(1.07*size)
    up();right(90);fd(4*size);right(90);fd(2*size);down()
    
    
    
def spa_ce(size):
    up()
    fd(0.5*size)
    right(90)
    fd(4*size)
    down()
    left(90)
  
def tur_write(word, size):
    word = str(word)
    size = int(size)
    for letter in word:
        if letter == "A":
            A(size)
        if letter == "D":
            D(size)
        if letter =="S":
            S(size)
        spa_ce(size)
  


tur_write("Hello, World",10)
