#!/usr/bin/env python3

""" This script resizes all the images to A4 size in a given directory
	and merges them into a single PDF file.
"""

from os import listdir
from fpdf import FPDF


path = 'convert/'

img_list = listdir(path)
img_list.sort()

pdf = FPDF('P', 'mm', 'A4')

x = 0
y = 0
w = 210
h = 297

for img in img_list:
	pdf.add_page()
	pdf.image(path+img, x, y, w, h)

pdf.output('output.pdf', 'F')
