try:
    print("Init int core [turtle]")
    from turtlel import *
except ModuleNotFoundError:
    print("Init int core [turtle] FAILED")
print("Init int core [turtle] FINISH")

try:
    print("Init int core [turtle_text]")
    from turtle_text import *
except ModuleNotFoundError:
    print("Init int core [turtle_text] FAILED")
print("Init int core [turtle_text] FINISH")