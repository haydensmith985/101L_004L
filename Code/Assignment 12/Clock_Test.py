from Clock_Class import *
import time

uhours = int(input('Number of hours: '))
uminutes = int(input('Number of minutes: '))
useconds = int(input('Number of seconds: '))

clock = Clock(uhours, uminutes, useconds)

while True:
    print(clock)
    clock.tick()
    time.sleep(1)

