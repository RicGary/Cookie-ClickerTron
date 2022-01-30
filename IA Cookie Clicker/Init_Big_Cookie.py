import numpy as np
import cv2

def InitCoordsBigCookie(tela, template, metodo=cv2.TM_CCOEFF_NORMED):
    """
    Função para pegar as coordenadas iniciais de onde clicar.


    :param tela: Local do arquivo da tela | 'Imagens/Cookie Clicker.JPG'
    :param template: Local do arquivo de template | 'Imagens/InitCookie.JPG'
    :param metodo: Método de detecção | 2 - cv2.TM_CCOEFF_NORMED
    :return: Coordenadas
    """

    #                                      h      w
    Screen = cv2.imread(tela)  # Sixe -> (1080, 1920)
    Cookie_template = cv2.imread(template, 0)  # Size -> (324, 320)
    Copy_Screen = cv2.imread(tela, 0)

    h, w = Cookie_template.shape
    # Melhor testado 2.
    method = metodo

    """
    1 - cv2.TM_CCOEFF   
    2 - cv2.TM_CCOEFF_NORMED
    3 - cv2.TM_CCORR
    4 - cv2.TM_CCORR_NORMED
    5 - cv2.TM_SQDIFF
    6 - cv2.TM_SQDIFF_NORMED
    """

    Result = cv2.matchTemplate(Copy_Screen, Cookie_template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(Result)

    y, x = max_loc

    """  
    # Debbug
    #####################################################
    inf_dir = (h + y, w + x)

    cv2.rectangle(Screen, (y, x), inf_dir, 255, 5)
    cv2.circle(Screen, (h//2 + y, w//2 + x), 5, 255, -1)
    #####################################################
    # Coordenadas Centrais do Cookie = (h//2 + y, w//2 + x)
    
    cv2.imshow('Debbug', Screen)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    """
    #           h            w
    return [h // 2 + y, w // 2 + x]


if __name__ == '__main__':
    print(InitCoordsBigCookie('Imagens/Cookie Clicker.JPG', 'Imagens/InitCookie.JPG'))
