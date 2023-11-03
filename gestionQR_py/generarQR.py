# -*- coding: utf-8 -*-

import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import CircleModuleDrawer, GappedSquareModuleDrawer, HorizontalBarsDrawer, RoundedModuleDrawer, SquareModuleDrawer, VerticalBarsDrawer
import argparse
import os

# Preparamos el formato para el codigo QR
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Obtenemos el valor del codigo QR, o bien por parametro o bien pidiendolo al usuario
parser = argparse.ArgumentParser()
parser.add_argument("-d", "--dato", type=str, 
    help="Dato con el que se generara el codigo QR (URL, texto, ...)")
parser.add_argument("-t", "--tipo", type=str, 
    help="Tipo de QR [circulo, cuadrado, Barra_Vertical, Barra_Horizontal, redondeado, Cuadrado_Grande]")
parser.add_argument("-i", "--imagen", type=str, 
    help="Ruta y nombre de fichero de imagen .png con QR que se generara")
args = parser.parse_args()

# Obtenemos el parametro -d (dato)
if args.dato:
    valorQR = args.dato
else:
    valorQR = input("Introduzca el valor del codigo QR: ")

# Obtenemos el parámetro -t (tipo) Si no se pasa se pone por defecto cuadrado_grande
if args.tipo:
    tipoQR =  args.tipo
else:
    tipoQR = 'cuadrado_grande'
tipoQR = tipoQR.upper()

# Obtenemos el parametro -i (fichero de imagen QR)
if args.imagen:
    imagenQR = args.imagen
else:
    imagenQR = os.path.dirname(os.path.abspath(__file__)) + '\codigo_qr.png'

# Aplicamos el valor al objeto QR
qr.add_data(valorQR)

# Establecemos el tipo de QR segun el indicado por parametro -t
if tipoQR == 'CIRCULO':
    tipoQRC = CircleModuleDrawer()
elif tipoQR == 'CUADRADO':
    tipoQRC = GappedSquareModuleDrawer()
elif tipoQR == 'BARRA_VERTICAL':
    tipoQRC = VerticalBarsDrawer()
elif tipoQR == 'BARRA_HORIZONTAL':
    tipoQRC = HorizontalBarsDrawer()
elif tipoQR == 'REDONDEADO':
    tipoQRC = RoundedModuleDrawer()
elif tipoQR == 'CUADRADO_GRANDE':
    tipoQRC = SquareModuleDrawer()

# Generamos el codigo QR y lo almacenamos en el fichero de imagen PNG
img = qr.make_image(image_factory=StyledPilImage, module_drawer=tipoQRC)
f = open(imagenQR, "wb")
img.save(f)
