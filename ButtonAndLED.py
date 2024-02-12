import machine # We import a library to control Pico
import utime # We import another library to control time
led_external = machine.Pin(15, machine.Pin.OUT) # We set the external led
button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN) # We set the button
while True:
 if button.value() == 1: # While button is pressed
 led_external.value(1) # Light up the led
 utime.sleep(2) # Wait 2 sec
 led_external.value(0) # Shut down the led
