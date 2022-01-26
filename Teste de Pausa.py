import keyboard
from sys import exit

"""
Teste para pausar o bot.
"""
while True:
    if keyboard.is_pressed('e'):
        while True:
            print('Running...')
            if keyboard.is_pressed('q'):
                print('Stop')
                exit(0)
