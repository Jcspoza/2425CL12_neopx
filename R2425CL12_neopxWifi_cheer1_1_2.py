# Hardware platform: Pico W
# Author : JC Santamaria 
# Date : 2023 - 7 - 26
# Goal : Usar una conexion wifi para tomar info de internet- sencillo
# Ref https://docs.sunfounder.com/projects/kepler-kit/en/latest/iotproject/2.cheerlight.html
# Version 1.1 : uso neopixel standard + cambios en conversion de color hex
# version 1.2 : try & except- evita que se quede led encendido

# INSTRUCCIONES ADICIONALES
# 1-Ver color sin complicarse
# escribir en navegador http://api.thingspeak.com/channels/1417/field/2/last.json.
# se vera algo como
# {"created_at":"2023-06-29T18:56:09Z","entry_id":972700,"field2":"#ffa500"}
# en 'field2' estan los 3 colores RGB
# 2- Ver y fijar color con 'CheerLights' en Discord
# 2.1 conseguir invitacion desde twiteer: buscar CheerLights-> click en invitacion
# 2.2 ya en discord cheerlight -> ir a canal general
# 2.3 invocar al bot con "/cheerlights "
# 2.4 seleccionar el boton "Get Color" o "Set Color"
# Si "Set Color" click en las selecciones

import urequests
import json
from machine import Pin
from time import sleep
from neopixel import NeoPixel
from do_connect import *

# Informative block - start
p_ucontroler = "Pico W & Pico _"
p_keyOhw = "External neopixel x 1 on GPIO17"
p_project = "IoT Cheerlight w Neopixel"
p_version = "1.2"
print(f"Microcontroler: {p_ucontroler} - Key other HW : {p_keyOhw}")
print(f"Program: {p_project} - Version: {p_version}")
# Informative block - end

# START FUNCTIONS DEFINITIONS ------------
def hexArgb(he):
    """Convierte un codigo de color a un tupla RGB
        Parametro : he = cadena con el codigo de color, ej '#ff00ff'
        Salida Tupla RGB
    """
    h = he.lstrip('#') # Retorna una copia eliminado '#' del principio (left)
    r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    return (r, g, b)

def lee_color():
    url = "http://api.thingspeak.com/channels/1417/field/2/last.json"
    try:
        r = urequests.get(url)
        if r.status_code > 199 and r.status_code < 300:
            cheerlights = json.loads(r.content.decode('utf-8'))
            print(cheerlights['field2'])
            colour = hexArgb(cheerlights['field2'])
            r.close() # libera memoria
            return colour
        else:
            return None
    except Exception as e:
        print(e)
        return None

# END FUNCTIONS DEFINITIONS ------------

# Aqui definimos la espera entre cada cambio a segundos
ESPERA = 10

# 1- Crea el objeto neopixel
NUMERO_PIXELS = 1
NEOPIXEL_PIN = 17
tira = NeoPixel(Pin(NEOPIXEL_PIN),NUMERO_PIXELS )

# 2- Nos conectamos a Internet
do_connect()

# 3- apagamos elneopixel
tira.fill((0,0,0)) # rojo a 0, verde a 0 y azul a 0
tira.write() # escribimos en neopixel

# 3- usamso un try-excep para que al salir con stop o control-C el neopixel se apague
try:
    while True: # 4- Bulce de lee color de cheerlights y escribe en enopixel
        color = lee_color() # 4.1 - lee el color de intenet feed cheerlights
        if color is not None:
            print("Color en int = ", color) # solo para debug, escribe nuevo color
            tira.fill(color)# 4.3 escribe color nuevo y espera
            tira.write()
        sleep(ESPERA)
except:
        tira.fill((0,0,0))
        tira.write()

