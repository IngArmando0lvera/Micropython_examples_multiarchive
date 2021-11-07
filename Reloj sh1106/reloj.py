#este proyecto emula un reloj sincronizado por ETC propio de un PC


#librerias
from machine import Pin, I2C, Timer
import utime
from utime import sleep_ms
from sh1106 import SH1106_I2C

timer0 = Timer()

i2c=I2C(0,scl=Pin(17),sda=Pin(16))#inicializamos bus I2C
display=SH1106_I2C(128,64,i2c)

def mes_str(mes=1):
#decision de nombre del mes
    if   mes == 0:  mes="ene"
    elif mes == 1:mes="feb"
    elif mes == 2:mes="mar"
    elif mes == 3:mes="abr"
    elif mes == 4:mes="may"
    elif mes == 5:mes="jun"
    elif mes == 6:mes="jul"
    elif mes == 7:mes="ags"
    elif mes == 8:mes="sep"
    elif mes == 9:mes="oct"
    elif mes == 10:mes="nov"
    elif mes == 11:mes="dic"
    return mes

def tiempo():
    t=["", "", "", "", "", "", ""]
    t[0],t[1],t[2],t[3],t[4],t[5],data,data2=utime.localtime()
    
    

    return t

def pantalla_oled():
    t = tiempo()
    fecha = str(t[2]) + " / " + str(mes_str(t[1])) + " / " + str(t[0])
    hora =  str(t[3]) + " : " + str(t[4]) + " : " + str(t[5])
    display.fill(0)
    display.text("RELOJ DE WINDOWS",0,0)
    display.text(fecha,8,32)
    display.text(hora,15,16)
    display.text("A R M A N D O",13,48)
    display.invert(1)
    display.show()
    sleep_ms(2)
    display.invert(0)
    display.show()

    


def main(timer):
    tiempo()
    pantalla_oled()

#ejecucion


#interrupcion constante, para actualizar reloj
timer0.init(freq=1, mode = Timer.PERIODIC, callback=main)

