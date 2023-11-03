# -*- coding: utf-8 -*-
# Hay que instalar las librerias 
#   pip install opencv-python
#   pip install pillow
#   pip install qrcode

import argparse
import cv2

# Obtenemos el fichero de imagen QR para leer, o bien por parametro o bien pidiendolo al usuario
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--fichero", type=str, 
    help="Ruta y nombre del fichero de imagen QR a leer")
args = parser.parse_args()

# Obtenemos el parametro -f (fichero QR a leer)
if args.fichero:
    ficheroQR = args.fichero
else:
    ficheroQR = input("Introduzca el fichero QR a leer: ")

# Leer un codigo QR de imagen
img = cv2.imread(ficheroQR)
det = cv2.QRCodeDetector()
valorQRLeido, pts, st_code = det.detectAndDecode(img)

# Guarda el valor leido del QR en un archivo
textoQR = ficheroQR.rsplit('.', 1)[0] + '.txt'
with open(textoQR, "w", encoding="utf-8") as archivo:
    archivo.write(valorQRLeido)

#print(valorQRLeido)
