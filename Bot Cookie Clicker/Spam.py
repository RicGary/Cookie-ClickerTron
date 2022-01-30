"""
Testando directkeys.py
"""
from directkeys import *
import time

CODIGO_LETRAS = {97: '0x41', 98: '0x42', 99: '0x43', 100: '0x44', 101: '0x45', 102: '0x46', 103: '0x47', 104: '0x48',
                 105: '0x49', 106: '0x4A', 107: '0x4B', 108: '0x4C', 109: '0x4D', 110: '0x4E', 111: '0x4F', 112: '0x50',
                 113: '0x51', 114: '0x52', 115: '0x53', 116: '0x54', 117: '0x55', 118: '0x56', 119: '0x57', 120: '0x58',
                 121: '0x59', 122: '0x5A', 32: '0x20'}


def _SPAM_(palavra, vezes, separar=False):

    """
    Código feito de teste para spamar mensagens.

    :param palavra: Palavra desejada
    :param vezes: Quantia de vezes para repetir
    :param separar: Separa por mensagens
    :return:
    """

    palavra = palavra.translate(CODIGO_LETRAS)

    time.sleep(10)

    for _ in range(vezes):
        for i in range(0, len(palavra), 4):
            PressKey(eval(palavra[i:i+4]))

        if separar:
            #Enter
            PressKey(0x0D)
            ReleaseKey(0x0D)

        else:
            #Espaço
            PressKey(0x20)
            ReleaseKey(0x20)

    if not separar:
        PressKey(0x0D)


if __name__ == '__main__':
    _SPAM_(input('Qual palavra deseja usar para atormentar? '), 1000, False)