import datetime
import switchcase
import ctypes

v1 = directory
v2 = directory
v3 = directory
v4 = directory
v5 = directory
v6 = directory
v7 = directory

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
