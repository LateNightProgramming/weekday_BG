import datetime
import switchcase
import ctypes

v1 = "C:\\Users\\zacpo\\Desktop\\bg\\monday.png"
v2 = "C:\\Users\\zacpo\\Desktop\\bg\\tuesday.png"
v3 = "C:\\Users\\zacpo\\Desktop\\bg\\wednesday.png"
v4 = "C:\\Users\\zacpo\\Desktop\\bg\\thursday.png"
v5 = "C:\\Users\\zacpo\\Desktop\\bg\\friday.png"
v6 = "C:\\Users\\zacpo\\Desktop\\bg\\saturday.png"
v7 = "C:\\Users\\zacpo\\Desktop\\bg\\sunday.png"

for case in switchcase.switch(datetime.datetime.today().weekday()):
    if case(0):
        ctypes.windll.user32.SystemParametersInfoW(20, 0, v1, 3)
        break
    if case(1):
        ctypes.windll.user32.SystemParametersInfoW(20, 0, v2, 3)
        break
    if case(2):
        ctypes.windll.user32.SystemParametersInfoW(20, 0, v3, 3)
        break
    if case(3):
        ctypes.windll.user32.SystemParametersInfoW(20, 0, v4, 3)
        break
    if case(4):
        ctypes.windll.user32.SystemParametersInfoW(20, 0, v5, 3)
        break
    if case(5):
        ctypes.windll.user32.SystemParametersInfoW(20, 0, v6, 3)
        break
    if case(6):
        ctypes.windll.user32.SystemParametersInfoW(20, 0, v7, 3)
        break
