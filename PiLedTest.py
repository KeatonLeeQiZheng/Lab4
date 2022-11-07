import time
from time import sleep

from hal import hal_input_switch as switch
from hal import hal_led as led

switch.init()
led.init()
timer: int=0

while(1):
    if (switch.read_slide_switch()==1):

        led.set_output(0, 1)
        time.sleep(0.2)

        led.set_output(0, 0)
        time.sleep(0.2)

    else:
        while(switch.read_slide_switch()==0):
            if(timer < 25):
                led.set_output(0, 1)
                time.sleep(0.1)

                led.set_output(0, 0)
                time.sleep(0.1)
                timer = timer+1
            else:
                led.set_output(0, 0)

        timer =0