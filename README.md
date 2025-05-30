# CL12-uP: Neopixel >draft<

Forma parte de la serie '**Workshop about Python and micropython with Pico W in CMM Benito**' Martin Madrid

## Clase 11 - Indice - 90 minutos

- Tutoriales, Programas que vamos a seguir y Conexionado

- Neopixel básico

- Neopixel avanzado

- Neopixel + wifi con internet 

## Tutoriales y Programas que vamos a seguir

### Tutoriales resumen

Hay muchísimos tutoriales sobre los neopixeles , porque son muy populares y sencillos de usar. **Pero ¡cuidado! NO hay que usar librerías externas** desde micrtopython 1.18 ( marzo 2022). Muchos tutoriales aun sigen indicando una libreria particular

De **Sunfounder** : ¡Cuidado! esta anticuada, NO hay que usar loberías externas

[3.3 RGB LED Strip &mdash; SunFounder Kepler Kit for Raspberry Pi Pico W 1.0 documentation](https://docs.sunfounder.com/projects/kepler-kit/en/latest/pyproject/py_neopixel.html)

Mas interesante el que incluye una conexion a internet

[8.2 Follow the @CheerLights &mdash; SunFounder Kepler Kit for Raspberry Pi Pico W 1.0 documentation](https://docs.sunfounder.com/projects/kepler-kit/en/latest/pyproject/iotproject/2.cheerlight.html)

De **codedojo**

[NeoPixel - Learning MicroPython](https://dmccreary.github.io/learning-micropython/basics/05-neopixel/)

Otros de interes

[Raspberry Pi Pico W con Adafruit IO control de Neopixel - Proyecto IOT- Código en MicroPython - YouTube](https://youtu.be/Hee9fIwVGFs?si=GsTk0Ec0jnnXPvGk)

----

### Tabla resumen de programas

| Programa                                                               | Lenguaje | Objetivo de Aprendizaje    | Hw adicional                                                                     |
| ---------------------------------------------------------------------- | -------- | -------------------------- | -------------------------------------------------------------------------------- |
| [R_bhwt_neopx1_3col_1_0.py](R_bhwt_neopx1_3col_1_0.py)                 | uPy      | probar 1er pixel 3 colores | Tira de neopixel en GPIO15, importante alimentar con +5volt, y compartir tierras |
| [R_bhwt_neopx8_3col_1_0.py](R_bhwt_neopx8_3col_1_0.py)                 |          |                            |                                                                                  |
| [R_bhwt_neopx8iris_1_0.py](R_bhwt_neopx8iris_1_0.py)                   |          |                            |                                                                                  |
| [R_bhwt_neopx16iris_1_0.py](R_bhwt_neopx16iris_1_0.py)                 |          |                            |                                                                                  |
| [R2425CL12_neopxWifi_cheer1_1_2.py](R2425CL12_neopxWifi_cheer1_1_2.py) |          |                            |                                                                                  |

### Conexionado

Los neopixel tienen 4 pines :

- GND : al negativo

- Vcc = +4 a +7volt : alimentaremos a +5 volt

- Din : cualquier pin GPIO nos vale : usaremos el GPIO15

- Dout (opcional) : para encadenar mas neopixels

![](./Pico_1neopxgpio15_bb.png)

## Neopixel básico

Usare las CL10 y CL11 de 2023, que he resumido en este pdf parte 1. [R2425_CL12_neopx.pdf](R2425_CL12_neopx.pdf)

### ¿Qué son?

Son celdas de 3 leds (RGB) cada uno de los cuales que pueden ser controlados individualmente con lo que se pueden producir todos los colores. Además podemos dirigirnos a cada celda de la cadena.

### Libreria y Manejo básico

[Quick reference for the RP2 &mdash; MicroPython latest documentation](https://docs.micropython.org/en/latest/rp2/quickref.html#neopixel-and-apa106-driver)

```
from machine import Pin
from neopixel import NeoPixel

pin = Pin(15, Pin.OUT)   # crea un objeto pin
np = NeoPixel(pin, 8)   # crea un objeto neopixel con 8 pixels
np[0] = (255, 255, 255) # fija el 1er pixel a white
np.write()              # escribe la 'pizarra' al neopixel , siempre toda
r, g, b = np[0]         # leemos el color del 1er pixel
np.fill((0,0,0)         # escribimos la pizarra todos los pixekles con 1 color
```

Como se ve el manejo es muy básico y casi cualquier cosa de interes , ha de hacerse programando en upython

---

## Manejo Avanzado

Seguir el pdf parte 2 . [R2425_CL12_neopx.pdf](R2425_CL12_neopx.pdf)

### Consumo

Es muy importante 

1. Alimentar la tira de neopixel a 5volt si es posible, aunque a 3.3 también funcionan

2. Tener en cuanta que cada uno de los 3 led de cada celda puede llegar a consumir en pico 20mA , es decir el color blanco consumiría 60mA máximo.
   
   1. Ejemplo de medida real tira de 8 neopixel todos los 3 colores RGB a 255  => blanco , consumo 308mA incluyendo el PICO W, que consume con la tira apagada =23mA
   2. Consumo máximo de 8 nepixel en blanco = 36mA por led

## Neopixel + wifi con conexión a internet

Vamos a usar la conexión a internet para leer de una web un color y 'escribirlo' en nuestro neopixel . Ver la parte 3 del pdf

## Preguntas sobre la Clase 1 - 10 minutos

Sección para que los alumnos pregunten sus dudas durante la clase

---

TO DO :
