from bvx_mouse import *
import pygame as p
import time
p.init()

WIN = p.display.set_mode((16*27, 9*27))

def sprite(scren, img, x, y):
    scren.blit(img, (x, y))
    
def box_choser(x, y, size, num_options, to, scale, folder, *bigger): #x and y is a pos on the options grid
    bigger = bigger
    if size > 5:
        if bigger != True:
            print("[Blue_NumERR]\nYou have to set bigger to True.\n(Set scale lower as 6 to avoid this ERR.)") 
            exit(1) 
    
        
def bvx_hotbar(ui_size, places, screen, PATH_TO_BG, PATH_TO_CS):
    PL = int(places)
    scale = 16 * ui_size
    W_S, H_S = p.display.get_window_size()
    H_POS = H_S - scale
    seter = scale / 2
            
    INV_BG = p.image.load(PATH_TO_BG)
    INV_CUR = p.image.load(PATH_TO_CS)
    INV_BG_S = p.transform.scale(INV_BG, (scale, scale))
    pos_cs = 1
    pos_cs_max = places
    
    if PL <= 0:
        PL = 1
        
    W_CO = W_S / 2
    start_pos = W_CO - scale * PL / 2
    c_pos = start_pos - scale / 2
    iter_cs = c_pos
        
    for n in range(0, PL+1):
        H = H_S - scale
        sprite(screen, INV_BG_S, c_pos, H)
        c_pos = c_pos + scale
        
    scroled = mouse_wheel()
    pos_cs = pos_cs + scroled
    
    if pos_cs == 0:
        pos_cs = pos_cs_max
    if pos_cs == pos_cs_max + 1:
        pos_cs = 1
        
    for pos in range(0, pos_cs + 1):
        iter_cs = iter_cs + scale
    
    
    
test_box = box_choser(0,0,6,0,0,0,0,0)

"""while 1:
    bvx_hotbar(1, 9, WIN, "./TEXTURES/hotbar_back.png", "./TEXTURES/hotbar_back.png")
    p.display.flip()
    WIN.fill((0,0,0))
    print(mouse_wheel())"""
    


    