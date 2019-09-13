from bs4 import BeautifulSoup
from selenium import webdriver
import os
import time

class SeleniumClass(object):

    def __init__(self):
        self.browser()
        #self.main_url = settings["MAIN_URL"]
        #self.book_url = settings["BOOK_URL"]
        #self.login = settings["LOGIN"]
        #self.password = settings["PASSWORD"]

        #self.RESULT_COOKIES = ""
        #self.RESULT_URL = ""

    def browser(self):

        driver = webdriver.Chrome(os.path.dirname(os.path.abspath(__file__))+"/chromedriver")
        driver.get("https://znanium.com")
        time.sleep(1)

        button = driver.find_element_by_xpath('//*[@id="loginButton"]')
        button.click()

        time.sleep(5)

        #ID абонента
        userid_element = driver.find_element_by_xpath('//*[@id="abonent_id"]')
        userid_element.click()
        userid_element.clear()
        userid_element.send_keys("")

        #Логин
        login_element = driver.find_element_by_xpath('//*[@id="username"]')
        login_element.click()
        login_element.clear()
        login_element.send_keys("")

        #Пароль
        passwd_element = driver.find_element_by_xpath('//*[@id="password"]')
        passwd_element.click()
        passwd_element.clear()
        passwd_element.send_keys("")

        #Кнопка входа
        login_element = driver.find_element_by_xpath('//*[@id="okButton"]')
        login_element.click()

        time.sleep(10)

        driver.get("http://znanium.com/bookread2.php?book=851215")

        #Меню скачивания
        #/html/body/div[1]/div[7]/div[3]/a/span
        #

        #Скачивание PDF
        #/html/body/div[18]/div[2]/div/div/ul[1]/li[3]/div/span

        #self.driver = webdriver.Chrome(os.path.dirname(os.path.abspath(__file__))+"/chromedriver")
        #self.get_cookies()

    def get_cookies(self):
        new_cookies = {}
        driver = self.driver
        driver.get(self.main_url)
        time.sleep(1)

        try:
            #Закрываем всплывающее окно с предложением о какой-то фигне
            button = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[3]/button")
            button.click()
            time.sleep(1)
        except:
            pass

        #Заполнение логина/пароля на формах
        login_element = driver.find_element_by_xpath('//*[@id="login"]')
        login_element.click()
        login_element.clear()
        login_element.send_keys(self.login)
        password_element = driver.find_element_by_xpath('//*[@id="password"]')
        password_element.click()
        password_element.clear()
        password_element.send_keys(self.password)
        time.sleep(1)

        #Вход на сайт
        button = driver.find_element_by_xpath('//*[@id="button1id"]')
        button.click()
        time.sleep(1)
        cookies = driver.get_cookies()
        
        #Запись новых данных
        for element in cookies:
            new_cookies[element["name"]] = element["value"]
        settings_module.SetCookies(new_cookies)