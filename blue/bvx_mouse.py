import pygame as p
from pygame.locals import *
from time import sleep
p.init()
#screen = p.display.set_mode((120*4, 72*4))
clock = p.time.Clock()
print("Blue Voxel Editor - Mouse modul - V.0.0.2")

def get_mouse():
    p.event.get()
    return p.mouse.get_pos()

def set_mouse(x, y):
    #p.event.get()
    p.mouse.set_pos([x, y])
    
def mouse_wheel():
    Scrolled = 0
    for event in p.event.get():
        if event.type == MOUSEWHEEL:
            Scrolled = event.y
    return Scrolled

def get_moved():
    X, Y = p.display.get_window_size()
    set_mouse(X/2, Y/2)
    p.event.get()
    move = p.mouse.get_rel()
        
    return move
    



        

