import machine
import utime

red = machine.Pin(15, machine.Pin.OUT)
amber = machine.Pin(14, machine.Pin.OUT)
green = machine.Pin(13, machine.Pin.OUT)

red.value(0)
amber.value(0)
green.value(0)

while True:
    green.value(1)
    utime.sleep(5)
    green.value(0)
    amber.value(1)
    utime.sleep(1)
    amber.value(0)
    red.value(1)
    utime.sleep(5)
    red.value(0)