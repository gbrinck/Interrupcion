#cronometro
import utime

comienzo = utime.ticks_ms()
utime.sleep(.5)
fin = utime.ticks_ms()
#print (comienzo)
print (fin-comienzo)
dif = utime.ticks_diff(fin, comienzo)
print (dif)