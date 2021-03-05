#Programa para medir el tiempo de reaccion ante un estimulo (LED encendido)
import machine
import utime
import urandom

led_ext = machine.Pin(15, machine.Pin.OUT)
boton = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_DOWN)

def atencion_boton(pin):
    boton.irq(handler=None)
    tiempo_reaccion = utime.ticks_diff(utime.ticks_ms(), comienzo)
    print ('Su tiempo de reacción fué de '+ str(tiempo_reaccion) + ' milisegundos!')
    led_ext.value(0)
    
while True:
    led_ext.value(0)
    utime.sleep(urandom.uniform(5, 10))
    led_ext.value(1)
    comienzo = utime.ticks_ms()
    boton.irq(trigger=machine.Pin.IRQ_RISING, handler=atencion_boton)
    utime.sleep(2)
