from sense_hat import SenseHat
import time
s = SenseHat()
s.low_light = True
green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255) 
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105, 180)
def s_alpha():
    P = pink
    O = nothing
    logo = [
    O, P, P, P, P, P, P, O,
    O, P, O, O, O, O, O, O,
    O, P, O, O, O, O, O, O,
    O, P, O, O, O, O, O, O,
    O, P, P, P, P, P, P, O,
    O, O, O, O, O, O, P, O,
    O, O, O, O, O, O, P, O,
    O, P, P, P, P, P, P, O,
    ]
    return logo
def r():
    P = pink
    O = nothing
    logo = [
    O, P, P, P, P, P, O, O,
    O, P, O, O, O, P, O, O,
    O, P, O, O, O, P, O, O,
    O, P, O, O, O, P, O, O,
    O, P, P, P, P, P, O, O,
    O, P, O, P, O, O, O, O,
    O, P, O, O, P, O, O, O,
    O, P, O, O, O, P, O, O,
    ]
    return logo
def m():
    P = pink
    O = nothing
    logo = [
    P, O, O, O, O, O, P, O,
    P, P, O, O, O, P, P, O,
    P, O, P, O, P, O, P, O,
    P, O, O, P, O, O, P, O,
    P, O, O, O, P, O, P, O,
    P, O, O, O, O, O, P, O,
    P, O, O, O, O, O, P, O,
    P, O, O, O, O, O, P, O,
    ]
    return logo
def i():
    P = pink
    O = nothing
    logo = [
    P, P, P, P, P, P, P, P,
    P, P, P, P, P, P, P, P,
    O, O, O, P, P, O, O, O,
    O, O, O, P, P, O, O, O,
    O, O, O, P, P, O, O, O,
    O, O, O, P, P, O, O, O,
    P, P, P, P, P, P, P, P,
    P, P, P, P, P, P, P, P,
    ]
    return logo
def t():
    P = pink
    O = nothing
    logo = [
    P, P, P, P, P, P, P, P,
    P, P, P, P, P, P, P, P,
    O, O, O, P, P, O, O, O,
    O, O, O, P, P, O, O, O,
    O, O, O, P, P, O, O, O,
    O, O, O, P, P, O, O, O,
    O, O, O, P, P, O, O, O,
    O, O, O, P, P, O, O, O,
    ]
    return logo
def space():
    P = pink
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo
images = [s_alpha, r, m, space, i, s_alpha, t]
count = 0
while True:
    s.set_pixels(images[count % len(images)]())
    time.sleep(.75)
    count += 1
#2.
from sense_hat import SenseHat
import time
s = SenseHat()
s.low_light = True
green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105, 180)

def space():
    P = pink
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo
def diode():
    P = pink
    O = nothing
    logo = [
    O, O, O, P, P, O, O, O,
    P, P, P, P, P, P, P, P,
    O, O, O, P, P, O, O, O,
    O, O, P, O, O, P, O, O,
    O, P, O, O, O, O, P, O,
    P, P, P, P, P, P, P, P,
    O, O, O, P, P, O, O, O,
    O, O, O, P, P, O, O, O,
    ]
    return logo
def giveway():
    P = pink
    O = nothing
    logo = [
    P, P, P, O, O, O, O, O,
    P, P, P, P, O, O, O, O,
    P, P, O, P, P, O, O, O,
    P, P, O, O, P, P, O, O,
    P, P, O, O, P, P, P, O,
    P, P, O, P, P, P, O, O,
    P, P, P, P, O, O, O, O,
    P, P, P, O, O, O, O, O,
    ]
    return logo
images = [diode, space, giveway, space]
count = 0
while True:
    s.set_pixels(images[count % len(images)]())
    time.sleep(.75)
    count += 1