"""
    Создание PDF-файла книги c библиo oнлaйн
"""

import requests
import os
import glob

from PyPDF2 import PdfFileWriter, PdfFileReader
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF

import browser_module
import settings_module

PDF_FILE = "OUTPUT.pdf"
URL_DENY = "https://biblio-online.ru/images/page_deny.svg"

def cookies_validator(cookies, url):
    r = requests.get(url, allow_redirects=True, cookies=cookies)
    if r.url == URL_DENY:
        return False
    return True

class FinalProcessingClass(object):
    def __init__(self, input_paths):
        self.input_paths = input_paths
        self.merger()
        self.remover()

    def merger(self):
        pdf_writer = PdfFileWriter()
    
        for path in self.input_paths:
            pdf_reader = PdfFileReader(path)
            for page in range(pdf_reader.getNumPages()):
                pdf_writer.addPage(pdf_reader.getPage(page))
    
        with open(PDF_FILE, 'wb') as fh:
            pdf_writer.write(fh)
        print("Создали PDF <3")

    def remover(self):
        remove_list = []
        for file in glob.glob("*.svg"):
            remove_list.append(file)
        for file in glob.glob("*.pdf"):
            remove_list.append(file)
        
        remove_list.remove(PDF_FILE)
        for item in remove_list:
            os.remove(item)
        print("Удаление файлов успешно")

class FileProcessing(object):
    def __init__(self, number, book_url, cookies):
        #TODO Получить cookies
        self.cookies = cookies
        self.result = "processing"
        self.number = number
        self.book_url = book_url
        self.get_book()
        self.to_pdf()
    
    def get_book(self):
        print(self.book_url + self.number)
        r = requests.get(self.book_url + self.number, allow_redirects=True, cookies=self.cookies)
        open("file"+self.number+".svg", 'wb').write(r.content)

    def to_pdf(self):
        try:
            drawing = svg2rlg("file"+self.number+".svg")
            renderPDF.drawToFile(drawing, "file"+self.number+".pdf")
        except AttributeError:
            print("Страницы закончились")
            self.result = "ready"

class MainClass(object):
    def __init__(self):
        sobj = settings_module.GetSettings()
        self.settings = sobj.settings

        cobj = settings_module.GetCookies()
        self.cookies = cobj.cookies

        self.main()

    def main(self):
        cookies_flag = cookies_validator(self.cookies,self.settings["TESTING_URL"])
        if cookies_flag == False:
            browser_module.SeleniumClass(self.settings)
            cobj = settings_module.GetCookies()
            self.cookies = cobj.cookies
            
        pdf_filelist = []
        page_number = 1

        while True:
            obj = FileProcessing(str(page_number), self.settings["BOOK_URL"], self.cookies)
            if obj.result == "ready":
                break
            pdf_filelist.append("file"+str(page_number)+".pdf")
            page_number += 1

        FinalProcessingClass(pdf_filelist)

if __name__ == "__main__":
    MainClass()