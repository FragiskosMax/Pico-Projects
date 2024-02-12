import machine
import utime
led = machine.Pin("LED", machine.Pin.OUT)

while True:
    led.off()
    utime.sleep(0.5)
    led.on()
    utime.sleep(0.5)
