from hooman import Hooman
from math import sin, pi
import time

hapi = Hooman(900, 500)

hapi.set_background(hapi.color['white'])

sliders = [hapi.slider(20+x*30, 50, 20, 400, {'direction': 'vertical', 'curve': 1}) for x in range(29)]
speed = hapi.slider(10, 10, 800, 30, {'value_range': (0, 0.5)})
period = hapi.slider(10, 460, 800, 30, {'value_range': (0, 1)})

"""y= A sin(Bx)"""

offset = 0
dx = pi/15
curr_time = time.time()

while hapi.is_running:
    hapi.clock.tick(30)

    speed.update()
    period.update()

    if time.time() - curr_time > speed.value():
        angle = offset + dx
        offset += dx
        curr_time = time.time()
        for slid in sliders:
            slid.set_value(hapi.constrain(sin(angle), -1, 1, 0, 1))
            angle += dx * period.value() # y = A sin(Bx)   <---this line changes B

    for slid in sliders:
        slid.update()

    hapi.flip_display()
    hapi.event_loop()


