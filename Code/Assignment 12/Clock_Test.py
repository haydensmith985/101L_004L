from Clock_Class import *
import time

uhours = int(input('Number of hours: ')) #asking user for input
uminutes = int(input('Number of minutes: '))
useconds = int(input('Number of seconds: '))

clock = Clock(uhours, uminutes, useconds) #creating a clock object

while True: #adjusting clock values for seconds passed
    print(clock)
    clock.tick()
    time.sleep(1)

