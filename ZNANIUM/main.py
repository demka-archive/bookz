"""
    Создание PDF-файла книги c инфрам
"""

import requests
import os
import glob

from PyPDF2 import PdfFileWriter, PdfFileReader
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF

import browser_module

class MainClass(object):
    def __init__(self):
        self.processing()
    def processing(self):
        obj = browser_module.SeleniumClass()

if __name__ == "__main__":
    MainClass()