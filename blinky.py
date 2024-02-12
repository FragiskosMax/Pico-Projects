import machine # We import a library to cntrol our Pico
import utime # We import another library to control the time
led = machine.Pin("LED", machine.Pin.OUT) # We set Pico's led

while True: # Forever (You can change it if you want)
    led.off() # Close the led
    utime.sleep(0.5) # Wait 0.5 sec
    led.on() # Open the led
    utime.sleep(0.5) # Wait 0.5 sec
