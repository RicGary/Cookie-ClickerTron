from directkeys import *
from time import sleep
import keyboard as key
from sys import exit

# Inicia o código
while True:
    # Apertar o botão E faz a IA começar
    if key.is_pressed('e'):
        while True:

            # Coordenada Cookie
            # Extensão = 229, 310
            # Diferença = 41, 70
            click(270, 380)
            sleep(0.0005)

            # Coordenada Cursor
            # Extensão = 1200, 300
            moveMouseTo(1200+41, 300+70)

            # Se pressionar Q a IA para
            if key.is_pressed('q'):
                print('Stop')
                exit(0)