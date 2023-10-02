###################
Author = "Spyro24"
name ="Blue VXE"
Version = "0.0.1"
vname = "BLUEX"

print(name)
print("Version:", Version)
print("Release:", vname)
try:
    print("Init core [pygame]")
    import pygame as pg
    print("Init core [pygame] FINISH")
except ModuleNotFoundError:
    print("Init core [pygame] FAILED")
    
#if __name__ == "__main__" :
    