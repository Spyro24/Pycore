try:
    print("Init module [absolute_solver]")
    sure = input("are you sure (this can demage you PC)[y/n]")
    if sure == "y":
        print("[absolute_solver] is loading...")
        from solver import *
    else:
        print("init was canceled by USER")
except:
    print("Init module [absolute_solver] FAILED")
print("Init module [absolute_solver] FINISH")
        