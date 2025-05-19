# Hardware platform: Pico W & Pico
# Author : JC Santamaria 
# Date : 2023 - 5 - 14
# Goal : Neopixel ring x8 rotate rainbow like lights
# adapted from C version
# Learning Target : High level neopixel handling & for loop
# Ref : https://www.coderdojotc.org/micropython/basics/05-neopixel/


from machine import Pin
from neopixel import NeoPixel
from utime import sleep

# Informative block - start
p_ucontroler = "Pico W & Pico _"
p_keyOhw = "External neopixel ring x 8 on GPIO15"
p_project = "Neopixel strip x8 rainbow like liths - adapted from C"
p_version = "1.0"
print(f"Microcontroler: {p_ucontroler} - Key other HW : {p_keyOhw}")
print(f"Program: {p_project} - Version: {p_version}")
# Informative block - end

NUMBER_PIXELS = 8
LED_PIN = 15

tira = NeoPixel(Pin(LED_PIN), NUMBER_PIXELS)

# STARTR FUNCTIONS -----------
def iris(pos):
    """Mapea el arcoiris de 0 a 255 en una tupla RGB 
        Parametros:
            pos : 0 a 255 mapea el arcoiris en 3 regiones de 84 de ancho
            1ra region suma de R y G , pero R disminuye y G aumenta
            2da region suma de G y B , pero G disminuye y B aumenta
            3ra region suma de B y R , pero B disminuye y R aumenta
            
        Retorno:
            una tupla en forma (r, g, b)
    """
    
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    
    if pos < 85: # 1ra region suma de R y G , pero R disminuye y G aumenta
        return (255 - pos * 3, pos * 3, 0)
    
    if pos < 170: # 2da region suma de G y B , pero G disminuye y B aumenta
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    
    pos -= 170 # 3ra region suma de B y R , pero B disminuye y R aumenta
    return (pos * 3, 0, 255 - pos * 3)

def cicloArcoiris(espera):
    """Distribuye el arcoiris en el anillo o tira neopixels usando funcion iris
        Global: usa 2 variables globales
            NUMBER_PIXELS : del anillo o tira neopixel
            tira : objeto neopixel
        
        Parametros:
            espera : segundos, tiempo de espera entre ciclos de arcoiris
                    
        Retorno: SIN retorno
    """
    global NUMBER_PIXELS, tira
    for j in range(255):
        for i in range(NUMBER_PIXELS):
            rc_index = (i * 256 // NUMBER_PIXELS) + j
            # print(j, i, rc_index, rc_index & 255)
            tira[i] = iris(rc_index & 255) # modulo a 256 hecho con una funcion AND
        tira.write()
        # sleep(.25)
    sleep(espera)
# END FUNCTIONS -----------

contador = 0
tira.fill((0,0,0))
tira.write()

try:    
    while True:
        print(f"Numero de ciclo {contador}")
        cicloArcoiris(.01)
        contador += 1
except KeyboardInterrupt:
    tira.fill((0,0,0))
    tira.write()