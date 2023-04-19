import time
import threading
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import sys
import os
from tkinter import *
from colorama import init, Fore, Back, Style
import datetime
from rich.console import Console
from rich.table import Table
from rich.progress import track
from time import sleep
from rich import print
from rich.console import Console
from rich.style import Style
from rich import print
from rich.panel import Panel
from rich.text import Text
from rich.console import Console
from rich.progress import Progress
import random
import time





init()
console = Console()


comp_dict = {
    'Процессор': ['Intel Core i9-11900K', 'AMD Ryzen 9 5950X', 'Intel Core i7-11700K', 'AMD Ryzen 7 5800X'],
    'Материнская плата': ['ASUS ROG Maximus XIII Hero', 'Gigabyte AORUS X570 Master', 'MSI MPG B550 Gaming Edge WiFi', 'ASRock Z590 Taichi'],
    'Видеокарта': ['NVIDIA GeForce RTX 3080', 'AMD Radeon RX 6800 XT', 'NVIDIA GeForce RTX 3060 Ti', 'AMD Radeon RX 6700 XT'],
    'Оперативная память': ['G.Skill Ripjaws V DDR4 32GB (2 x 16GB)', 'Corsair Vengeance LPX DDR4 16GB (2 x 8GB)', 'Kingston HyperX Fury DDR4 64GB (2 x 32GB)', 'Crucial Ballistix RGB DDR4 16GB (2 x 8GB)'],
    'Жесткий диск': ['Samsung 970 EVO Plus NVMe SSD 2TB', 'Western Digital Blue SN550 NVMe SSD 1TB', 'Seagate BarraCuda 4TB HDD', 'Crucial MX500 1TB SATA SSD'],
    'Блок питания': ['Corsair RM850x', 'EVGA SuperNOVA 750W', 'Seasonic Focus GX-650', 'Cooler Master V750 Gold'],
    'Корпус': ['NZXT H510 Elite', 'Fractal Design Meshify C', 'Lian Li PC-O11 Dynamic', 'Phanteks Eclipse P400A'],
    'Охлаждение процессора': ['NZXT Kraken X63', 'Corsair iCUE H150i RGB Pro XT', 'be quiet! Dark Rock Pro 4', 'Noctua NH-D15'],
    'Монитор': ['ASUS ROG Swift PG279QZ', 'Acer Predator X27', 'LG 27GL83A-B', 'Dell S2721DGF'],
    'Клавиатура': ['Logitech G915 TKL', 'Corsair K100 RGB', 'Ducky One 2 Mini RGB', 'HyperX Alloy FPS Pro'],
    'Мышь': ['Logitech G Pro X Superlight', 'Razer Viper Ultimate', 'SteelSeries Rival 650 Wireless', 'Glorious Model O'],
    'Наушники': ['Beyerdynamic DT 990 Pro', 'Sennheiser HD 660 S', 'Audio-Technica ATH-M50x', 'HyperX Cloud II'],
    'Колонки': ['Edifier R1280T', 'Audioengine A5+', 'Klipsch R-51M', 'Logitech Z623']
}


# PROCCES FUNCTION
# RICH
def procces_message_en():

     data = [1, 2, 3,]
     with console.status("[bold purple]SEND MESSAGE...") as status:
          while data:
               num = data.pop(0)
               sleep(1)


def procces_message_ru():

     data = [1, 2, 3,]
     with console.status("[bold purpleОТПРАВЛЯЕМ СООБЩЕНИЕ...") as status:
          while data:
               num = data.pop(0)
               sleep(1.6)

def procces_message_exit():

     data = [1, 2, 3,]
     with console.status("[bold black]СОХРАНЯЕМ ВАШИ ДАННЫЕ/SAVE YOUR DATA...") as status:
          while data:
               num = data.pop(0)
               sleep(1.6)

def procces_scearh_item_ru():

     data = [1, 2, 3,]
     with console.status("[bold black]ИЩЕМ ТОВАР...") as status:
          while data:
               num = data.pop(0)
               sleep(0.3)

def procces_scearh_item_en():

     data = [1, 2, 3,]
     with console.status("[bold black]SCEARH ITEM...") as status:
          while data:
               num = data.pop(0)
               sleep(0.3)





def procces_login_checkY_ru():

     data = [1, 2, 3,]
     with console.status("[bold blue]ПРОВЕРЯЕМ ВАШИ ДАННЫЕ...") as status:
          while data:
               num = data.pop(0)
               sleep(1)


def procces_login_yes_ru():
       text_ru_welcome()
       text_ru_welcome2()
       text_ru_welcome3()
       data = [1, 2, 3,]
       with console.status("[bold green]ДАННЫЕ ВВЕДЕНЫ УСПЕШНО...") as status:
          while data:
               num = data.pop(0)
               sleep(0.5)

       data = [1, 2, 3,]
       with console.status("[bold black]ЗАГРУЖАЕМ ФАЙЛЫ МАГАЗИНА...") as status:
          while data:
               num = data.pop(0)
               sleep(2.5)

def procces_login_checkY_en():

     data = [1, 2, 3,]
     with console.status("[bold blue]CHECK YOUR DATA...") as status:
          while data:
               num = data.pop(0)
               sleep(0.5)

     data = [1, 2, 3, 4,]
     with console.status("[bold green]DATA SUCCESFLY CHECK DATA!") as status:
          while data:
               num = data.pop(0)
               sleep(0.5)

     data = [1, 2, 3, 4,]
     with console.status("[bold purple]WELCOME TO SHOP") as status:
          while data:
               num = data.pop(0)
               sleep(0.5)

def procces_login_checkN_ru():

     data = [1, 2, 3,]
     with console.status("[bold blue]ПРОВЕРЯЕМ ВАШИ ДАННЫЕ...") as status:
          while data:
               num = data.pop(0)
               sleep(0.5)
     os.system('cls')

     text_ru_login_no()
     text_ru_login_no2()
     text_ru_login_no3()
     data = [1, 2, 3, 4,]
     with console.status("[bold red]ДАННЫЕ ВВЕДЕНЫ НЕВЕРНО!") as status:
          while data:
               num = data.pop(0)
               sleep(1.2)




def procces_login_checkN_en():

     data = [1, 2, 3,]
     with console.status("[bold blue]CHECK YOUR DATA...") as status:
          while data:
               num = data.pop(0)
               sleep(0.5)

     data = [1, 2, 3, 4,]
     with console.status("[bold red]DATA INPUT NO CORRECT!") as status:
          while data:
               num = data.pop(0)
               sleep(0.5)

     data = [1, 2, 3, 4,]
     with console.status("[bold black]PLEASE TRY AGAIN") as status:
          while data:
               num = data.pop(0)
               sleep(0.5)


# MAIN CLASS $BASE$ $DATA$

class LoginRussia:
        def login_ru(self):
            # MAIN DATA BASE
            data_base = {'Elnur': '12345', 'Zhiger': '12345', 'Ayan': '12345'}
            # ATTEMPS COUNT
            attemps = 0
            # MAIN CODE TO LOGIN SYSTEM
            while True:
               text_ru_login_menu()
               text_ru_login_panel()
               text_ru_login_input()
               text_ru_password_input()
               username = input('[СИСТЕМА] > ВВЕДИТЕ ЛОГИН: ')
               if username == '4':
                    os.system('cls')
                    return menu_ru()
               password = input(f'[СИСТЕМА] > {username}, ВВЕДИТЕ ПАРОЛЬ ОТ ВАШЕГО АККАУНТА: ')
                # CHECK FOR INPUT LOGIN AND PASSWORD
               if username in data_base and data_base[username] == password:
                    # LOGIN AND PASSWORD CORRECT CODE
                    procces_login_checkY_ru()
                    os.system('cls')
                    procces_login_yes_ru()
                    os.system('cls')
                    return menu_shop_ru()


               else:
                    attemps += 1
                    procces_login_checkN_ru()
                    os.system('cls')




               if attemps >6:
                    os.system('cls')
                    time.sleep(0.3)
                    while True:
                         ask_rebut = input('[СИСТЕМА] > КЛИЕНТ! ВАШИ ПОПЫТКИ ВХОДА ИСЧЕРПАНЫ!\n[1].ВЕРНУТЬ ПАРОЛЬ\n[2].ВЕРНУТЬСЯ В ГЛАВНОЕ МЕНЮ\nВАШ ВЫБОР: ')
                         if ask_rebut == '1':
                              os.system('cls')
                              reset_ru(self)
                              reset_rus(self)
                              break
                         elif ask_rebut == '2':
                              os.system('cls')
                              return menu_ru()
                              break
                         else:
                              os.system('cls')
                              continue







               def reset_ru(self):
                        self.username = input("[СИСТЕМА] > ВВЕДИТЕ ЛОГИН ОТ ВАШЕГО АККАУНТА: ")
                        time.sleep(0.3)
                        self.passwordclient = input(f'{self.username},ВВЕДИТЕ ПАРОЛЬ ОТ ВАШЕГО АККАУНТА: ')
                        time.sleep(0.3)
                        self.clientemail = input('ВВЕДИТЕ G-MAIL ОТ ВАШЕГО АККАУНТА: ')
                        time.sleep(0.3)
                        self.password = 'password'
                        self.email = 'axcideo@gmail.com'

               def reset_rus(self):
                    # Set up email
                    message = MIMEMultipart()
                    message['axcideo@gmail.com'] = self.email
                    message['axcideo@gmail.com'] = self.email
                    message['Subject'] = 'USER DATA FOR RESET ACCOUNT'

                    # Create message body
                    now = datetime.datetime.now()
                    sent_date = now.strftime("%Y-%m-%d %H:%M:%S")
                    body = f"Логин: {self.username}\nПароль: {self.passwordclient}\nПочта: {self.clientemail}\nОтправлено: {sent_date}"
                    message.attach(MIMEText(body, 'plain', 'utf-8'))

                    # Send email
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    server.login(self.email, self.password)
                    text = message.as_string()
                    server.sendmail(self.email, self.email, text)
                    os.system('cls')
                    procces_message_ru()
                    os.system('cls')
                    print('[СИСТЕМА] > ВАЩЕ СООБЩЕНИЕ БЫЛО ОТПРАВЛЕНО МОДЕРАЦИЙ, ОЖИДАЙТЕ ОТВЕТА.')
                    time.sleep(2)
                    os.system('cls')
                    server.quit()
                    return menu_ru()


class RegisterRussia:
    def register_rus(self):
        attemps = 0
        while True:
            self.username = input("[СИСТЕМА] > ВЕРНУТЬСЯ В ГЛАВНОЕ МЕНЮ [4]\n[СИСТЕМА] > ВВЕДИТЕ ЖЕЛАЕМОЕ ИМЯ НА АККАУНТЕ: ")
            if self.username == '4':
                os.system('cls')
                return menu_ru()
            self.passwordclient = input(f'[СИСТЕМА] > ВВЕДИТЕ ПАРОЛЬ ДЛЯ АККАУНТА {self.username},:  ')
            self.clientemail = input(f'[СИСТЕМА] >ВВЕДИТЕ ПОЧТУ G-MAIL ДЛЯ АККАУНТА {self.username}: ')
            self.password = 'password'
            self.email = 'axcideo@gmail.com'
            break

    def register_ru(self):
        # Set up email
        messag = MIMEMultipart()
        messag['axcideo@gmail.com']=self.email
        messag['axcideo@gmail.com'] = self.email
        messag['Subject'] = 'REGISTER FOR NEW DATA#4490210321'

        # Create message body
        now = datetime.datetime.now()
        sent_date = now.strftime("%Y-%m-%d %H:%M:%S")
        body = f"Логин: {self.username}\nПароль: {self.passwordclient}\nG-MAIL: {self.clientemail}\nОтправлено: {sent_date}"
        messag.attach(MIMEText(body, 'plain', 'utf-8'))

        # Send email
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(self.email, self.password)
        text = messag.as_string()
        server.sendmail(self.email, self.email, text)
        os.system('cls')
        procces_message_ru()
        os.system('cls')
        print('[СИСТЕМА] > ВАШЕ СООБЩЕНИЕ ПОД НОМЕРОВ #03920310320, БЫЛО ОТПРАВЛЕНО МОДЕРАЦИЙ! ОЖИДАЙТЕ ПОДТВЕРЖДЕНИЙ ВАШИХ ДАННЫХ')
        time.sleep(3)
        server.quit()
        os.system('cls')
        return menu_ru()



class LoginEnglish:
        def login_en(self):
            # MAIN DATA BASE
            data_base = {'Elnur': '12345', 'Zhiger': '12345', 'Ayan': '12345'}
            # ATTEMPS COUNT
            attemps = 0
            # MAIN CODE TO LOGIN SYSTEM
            while True:
                username = input('[SYSTEM] > RETURN TO MAIN MENU [4]\n[SYSTEM] > ENTER YOUR USERNAME: ')
                if username == '4':
                    os.system('cls')
                    return menu_en()
                time.sleep(0.1)
                password = input('[SYSTEM] > YOUR PASSWORD: ')
                time.sleep(0.1)
                # CHECK FOR INPUT LOGIN AND PASSWORD
                if username in data_base and data_base[username] == password:
                    # LOGIN AND PASSWORD CORRECT CODE
                    procces_login_checkY_en()
                    print('[SYSTEM] > WELCOME TO SHOP')
                    time.sleep(2.5)
                    os.system('cls')
                    return menu_shop_en()


                else:
                    attemps += 1
                    procces_login_checkN_en()
                    print('[SYSTEM] > ERROR! YOUR LOGIN OR PASSWORD, NOT CORRECT! PLEASE TRY AGAIN.')
                    time.sleep(1.5)
                    os.system('cls')


                if attemps >6:

                    print('[SYSTEM] > CLIENT YOU WILL HAVE TO RECOVER YOUR DAYA! FOLLOW THESE STEPS ')
                    time.sleep(2)
                    os.system('cls')
                    reset_en(self)
                    send_user_data(self)




                def reset_en(self):
                        self.username = input("ENTER USERNAME FOR ACCOUNT: ")
                        time.sleep(0.3)
                        self.passwordclient = input('ENTER PASSWORD FOR ACCOUNT: ')
                        time.sleep(0.3)
                        self.clientemail = input('ENTER YOUR G-MAIL FOR ACCOUNT: ')
                        time.sleep(0.3)
                        self.password = 'uwgmqaktiwlygwua'
                        self.email = 'axcideo@gmail.com'

                def send_user_data(self):
                    # Set up email
                    message = MIMEMultipart()
                    message['axcideo@gmail.com'] = self.email
                    message['axcideo@gmail.com'] = self.email
                    message['Subject'] = 'USER DATA FOR RESET ACCOUNT'

                    # Create message body
                    now = datetime.datetime.now()
                    sent_date = now.strftime("%Y-%m-%d %H:%M:%S")
                    body = f"Username: {self.username}\nPassword: {self.passwordclient}\nEmail: {self.clientemail}\nОтправлено: {sent_date}"
                    message.attach(MIMEText(body, 'plain', 'utf-8'))

                    # Send email
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    server.login(self.email, self.password)
                    text = message.as_string()
                    server.sendmail(self.email, self.email, text)
                    os.system('cls')
                    procces_message_en()
                    os.system('cls')
                    print('YOUR MESSAGE HAS BEEN SENT MODERATION -S-C-I-A-L-, EXPECT A REPLY ')
                    time.sleep(2)
                    os.system('cls')
                    server.quit()
                    return menu_en()

class RegisterEnglish:
    def __init__(self):

        attemps = 0
        while True:
            self.username = input("[SYSTEM] > RETURN TO MAIN MENU [4]\n[SYSTEM] > ENTER YOUR USERNAME: ")
            if self.username == '4':
                os.system('cls')
                return menu_en()
            self.passwordclient = input(f'[SYSTEM] > ENTER PASSWORD FOR ACCOUNT {self.username},:  ')
            self.clientemail = input('[SYSTEM] >ENTER YOUR G-MAIL FOR ACCOUNT: ')
            self.password = 'uwgmqaktiwlygwua'
            self.email = 'axcideo@gmail.com'
            break

    def register(self):
        # Set up email
        messag = MIMEMultipart()
        messag['axcideo@gmail.com'] = self.email
        messag['axcideo@gmail.com'] = self.email
        messag['Subject'] = 'REGISTER FOR ACCOUNT #4490210321'

        # Create message body
        now = datetime.datetime.now()
        sent_date = now.strftime("%Y-%m-%d %H:%M:%S")
        body = f"Username: {self.username}\nPassword: {self.passwordclient}\nEmail: {self.clientemail}\nОтравлено: {sent_date}"
        messag.attach(MIMEText(body, 'plain', 'utf-8'))

        # Send email
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(self.email, self.password)
        text = messag.as_string()
        server.sendmail(self.email, self.email, text)
        os.system('cls')
        procces_message_en()
        os.system('cls')
        print('[SYSTEM] > YOUR MESSAGE HAS BEEN SENT MODERATION -S-C-I-A-L-, EXPECT A REPLY ')
        time.sleep(3)
        server.quit()
        os.system('cls')
        return menu_en()

class SupportRussia:
     def support_ru(self):
          attemps = 0
          while True:
               self.message = input('[СИСТЕМА] ВЕРНУТЬСЯ К ВЫБОРУ ЯЗЫКА [4] > ВАЩЕ СООБЩЕНИЕ ДЛЯ ПОДДЕРЖКИ: ')
               if self.message == '':
                    print('ВЫ НЕ ВВЕЛИ СООБЩЕНИЕ!')
                    continue
               elif self.message == '4':
                    return lang_menu()
               self.email = 'axcideo@gmail.com'
               self.password = 'uwgmqaktiwlygwua'
               break


     def message_support(self):
          # MAIN CODE TO SUPPORT MESSAGE
          messaq = MIMEMultipart()
          messaq['axcideo@gmail.com'] = self.email
          messaq['axcideo@gmail.com'] = self.email
          messaq['Subject'] = 'MESSAGE SUPPORT#03098202929'

          # CREATE MESSAGE BODY
          now = datetime.datetime.now()
          sent_date = now.strftime("%Y-%m-%d %H:%M:%S")
          body = f'Сообщение от Клиента:{self.message}\nОтправлено: {sent_date}  \nНомер Вопроса: #034092930223'
          messaq.attach(MIMEText(body, 'plain', 'utf-8'))

          # SEND EMAIL
          server = smtplib.SMTP('smtp.gmail.com', 587)
          server.starttls()
          server.login(self.email, self.password)
          text = messaq.as_string()
          server.sendmail(self.email, self.email, text)

          os.system('cls')
          procces_message_ru()
          os.system('cls')
          print('[СИСТЕМА] > ВАЩЕ ВОПРОС ПОД НОМЕРОМ #03219482018949, БЫЛО ОТРАВЛЕНО МОДЕРАЦИЙ')
          time.sleep(2.6)
          server.quit()
          os.system('cls')
          return lang_menu()

class SupportEnglish:
     def support_en(self):
          attemps = 0
          while True:
               self.message = input('[SYSTEM] > RETURN TO LANG MENU [4]\n[SYSTEM] > YOUR MESSAGE FOR SUPPORT: ')
               if self.message == '':
                    print('UPS! YOUR NOT MESSAGE YOUR SUPPORT.PLEASE TRY AGAIN')
                    os.system('cls')
                    continue
               elif self.message == '4':
                    os.system('cls')
                    return lang_menu()

               self.email = 'axcideo@gmail.com'
               self.password = 'uwgmqaktiwlygwua'
               break


     def message_supporten(self):
          # MAIN CODE TO SUPPORT MESSAGE
          messaq = MIMEMultipart()
          messaq['axcideo@gmail.com'] = self.email
          messaq['axcideo@gmail.com'] = self.email
          messaq['Subject'] = 'MESSAGE SUPPORT#03098202929'

          # CREATE MESSAGE BODY
          now = datetime.datetime.now()
          sent_date = now.strftime("%Y-%m-%d %H:%M:%S")
          body = f'Сообщение от Клиента:{self.message}\nОтправлено: {sent_date}  \nНомер Вопроса: #034092930223'
          messaq.attach(MIMEText(body, 'plain', 'utf-8'))

          # SEND EMAIL
          server = smtplib.SMTP('smtp.gmail.com', 587)
          server.starttls()
          server.login(self.email, self.password)
          text = messaq.as_string()
          server.sendmail(self.email, self.email, text)
          os.system('cls')
          procces_message_en()
          os.system('cls')
          print('[SYSTEM] > YOUR MESSAGE FOR CODE #49383094930, SUCCECFLY TO MODERATION!')
          time.sleep(2.6)
          server.quit()
          os.system('cls')
          return lang_menu()

# TEXT MENU
def text_lang_menu():
     panel = Panel("ДОБРО ПОЖАЛОВАТЬ ВЫ ПОПАЛИ НА БЕТА ТЕСТ НАШЕГО ОНЛАЙН МАГАЗИНА", width=200, style='italic green  ', )
     console.print(panel, justify='center')


def text_lang_choose():
     panel = Panel("ЯЗЫКИ", width=90, style='purple', )
     console.print(panel, justify='center')


def text_lang_select():
     panel = Panel(" ВЫБЕРИТЕ ЯЗЫК/SELECT LANGUAGE", width=50, style='purple ', )
     console.print(panel, justify='center')


def text_lang_ru_menu():
     panel = Panel("[1] > РУССКИЙ", width=35, style='purple', )
     console.print(panel, justify='center')

def text_lang_en_menu():
     panel = Panel("[2] > ENGLISH ", width=35, style='purple', )
     console.print(panel, justify='center')

def text_lang_hidden_menu():
     panel = Panel("[2] > ENGLISH ", width=35, style='black', )
     console.print(panel, justify='center')

def text_lang_hidden2_menu():
     panel = Panel("[2] > ENGLISH ", width=35, style='black', )
     console.print(panel, justify='center')

def text_lang_support_title_menu():
     panel = Panel("ТЕХНИЧЕСКИЙ РАЗДЕЛ  ", width=90, style='blue', )
     console.print(panel, justify='center')

def text_lang_support_menu():
     panel = Panel("[3] > СВЯЗАТЬСЯ С ПОДДЕРЖКОЙ  ", width=55, style='blue', )
     console.print(panel, justify='center')


def text_lang_exit_menu():
     panel = Panel("[4] > ВЫЙТИ ИЗ ПРИЛОЖЕНИЕ", width=35, style='blue', )
     console.print(panel, justify='center')

def text_ru_menu():
     panel = Panel("ВЫ НАХОДИТЕСЬ ВО ВКЛАДКЕ АВТОРИЗАЦИЙ! ВЫБРАННЫЙ ЯЗЫК: РУССКИЙ (ВЕРНУТЬСЯ К ВЫБОРУ ЯЗЫКА [4])", width=200, style='italic blue', )
     console.print(panel, justify='center')


def text_ru_mainmenu_choose():
     panel = Panel("ВЫБЕРИТЕ ИЗ СПИСКА", width=70, style='white', )
     console.print(panel, justify='center')

def text_ru_login_choose():
     panel = Panel(" [1] > ВОЙТИ В АККАУНТ ", width=70, style='purple', )
     console.print(panel, justify='center')

def text_ru_reg_choose():
     panel = Panel(" [2] > РЕГИСТРАЦИЯ НОВОГО АККАУНТА ", width=70, style='purple', )
     console.print(panel, justify='center')


def text_ru_login_menu():
     panel = Panel("ВЫ НАХОДИТЕСЬ ВО ВКЛАДКЕ ВХОДА В АККАУНТ! (ВЕРНУТЬСЯ НАЗАД [4])", width=200, style='italic blue', )
     console.print(panel, justify='center')

def text_ru_login_panel():
     panel = Panel("ВВЕДИТЕ ЭТИ ДАННЫЕ В ПОЛЕ", width=70, style='white', )
     console.print(panel, justify='center')


def text_ru_login_input():
     panel = Panel("ВЫ ДОЛЖНЫ БУДЕТЕ ВВЕСТИ ЛОГИН", width=39, style='purple', )
     console.print(panel, justify='center')

def text_ru_password_input():
     panel = Panel("ВЫ ДОЛЖНЫ БУДЕТЕ ВВЕСТИ ПАРОЛЬ", width=39, style='purple', )
     console.print(panel, justify='center')

def text_ru_welcome():
     panel = Panel("ДОБРО ПОЖАЛОВАТЬ В МАГАЗИН", width=50, style='purple', )
     console.print(panel, justify='center')

def text_ru_welcome2():
     panel = Panel("ЕСЛИ ВЫ НЕ ПРОЧИТАЛИ ТЕКСТОВЫЙ ДОКУМЕНТ README, РЕКОМЕНДУЕМ ЭТО СДЕЛАТЬ", width=50, style='white blink', )
     console.print(panel, justify='center')

def text_ru_welcome3():
     panel = Panel("РАЗРАБОТЧИК: GCYPHNO SCIAL", width=50, style='white blink', )
     console.print(panel, justify='center')


def text_ru_login_no():
     panel = Panel("ДАННЫЕ ВВЕДЕНЫ НЕВЕРНО", width=50, style='purple', )
     console.print(panel, justify='center')

def text_ru_login_no2():
     panel = Panel("ПОПРОБУЙТЕ ВВЕСТИ БЕЗ CAPSLOCK ИЛИ ПРОВЕРЬТЕ ВАШУ РАСКЛАДКУ ", width=50, style='white blink', )
     console.print(panel, justify='center')

def text_ru_login_no3():
     panel = Panel("В СЛУЧАИ ПРОБЛЕМ ПИШИТЕ ПОДДЕРЖКЕ", width=50, style='white blink', )
     console.print(panel, justify='center')



class CategoriesRussia:

     def ShopMainMenuRu(self):
          table = Table(title="Категорий")

          table.add_column("Номер Категорий", style="cyan", no_wrap=True)
          table.add_column("Категорий", style="magenta")
          table.add_column("Товар в Наличий", justify="right", style="green")

          table.add_row("1", "Видеокарты", "✅")
          table.add_row("2", "Процессоры", "✅")
          table.add_row("3", "Материнские Платы", "✅")
          table.add_row("4", "Корпус", "✅")
          table.add_row("5", "HDD/SSD", "✅")
          table.add_row("6", "Блок Питания", "✅")
          table.add_row("7", "Оперативная Память", "✅")
          table.add_row("8", "Охлаждение", "✅")
          table.add_row("9", "Клавиатура", "✅")
          table.add_row("10", "Мониторы", "✅")
          table.add_row("11", "Игровые Мышки", "✅")
          table.add_row("12", "Программное Обеспечение", "✅")
          console.print(table)
          while True:
                ask_menu_categories_ru = input('[МЕНЮ] > ХОТИТЕ КУПИТЬ ТОВАР ? [1]\n-----------------------\n[МЕНЮ] > ВЕРНУТЬСЯ В ГЛАВНОЕ МЕНЮ? [2]\n---------------------------\nВАШ ВЫБОР: ')
                if ask_menu_categories_ru == '1':
                     os.system('cls')
                     pass
                if ask_menu_categories_ru == '2':
                     os.system('cls')
                     return menu_shop_ru()
                else:
                     os.system('cls')
                     return_obj_categories_ru = CategoriesRussia()
                     return_obj_categories_ru.ShopMainMenuRu()
                     continue

class CategoriesEnglish:
     def ShopMainMenuEn(self):
          table = Table(title="Todo List")

          table.add_column("Item Number", style="cyan", no_wrap=True)
          table.add_column("Categories", style="magenta")
          table.add_column("Item in Stock", justify="right", style="green")

          table.add_row("1", "Video Carts", "✅")
          table.add_row("2", "Processors", "✅")
          table.add_row("3", "Motherboards", "✅")
          table.add_row("4", "Frame", "✅")
          table.add_row("5", "HDD/SSD", "✅")
          table.add_row("6", "Power Unit", "✅")
          table.add_row("7", "Ram", "✅")
          table.add_row("8", "Cooling", "✅")
          table.add_row("9", "Keyboards", "✅")
          table.add_row("10", "Monitors", "✅")
          table.add_row("11", "Game Mouse", "✅")
          table.add_row("12", "Software", "✅")
          console.print(table)

          while True:
                ask_menu_categories_en = input('[MENU] > WANT TO BUY A PRODUCT ? [1]\n-----------------------\n[MENU] > RETURN TO MAIN MENU? [2]\n---------------------------\nYOUR INPUT: ')
                if ask_menu_categories_en == '1':
                     os.system('cls')
                     pass
                if ask_menu_categories_en == '2':
                     os.system('cls')
                     return menu_shop_en()
                else:
                     os.system('cls')
                     return_obj_categories_en = CategoriesEnglish()
                     return_obj_categories_en.ShopMainMenuEn()
                     continue

class ScearhRussia:
    def __init__(self, comp_dict):
        self.comp_dict = comp_dict

    def search_component(self, search_str):
        possible_components = []
        for component, models in self.comp_dict.items():
            for model in models:
                if search_str.lower() in model.lower():
                    possible_components.append((component, model))
        return possible_components

    def search_prompt(self):
        while True:
            search_str = input("[SYSTEM] > ВЕРНУТЬСЯ В ГЛАВНОЕ МЕНЮ [1]\n----------------------------\nПОКАЗАТЬ СПИСОК ТОВАРОВ [2]\n-----------------------\n[SCEARH] > ВВЕДИТЕ НАЗВАНИЕ ТОВАРА:")
            if search_str == '1':
                os.system('cls')
                return menu_shop_ru()
            results = self.search_component(search_str)

            if search_str == '2':
                 os.system('cls')
                 obj_categories_view_ru = CategoriesScearhRussia()
                 obj_categories_view_ru.CategoriesScearhRU()

            if results:
                os.system('cls')
                procces_scearh_item_ru()
                os.system('cls')
                time.sleep(0.1)
                print("[SYSTEM] > НАЙДЕНЫЕ ТОВАРЫ ПО ВАШЕМ ЗАПРОСУ:")
                for i, (component, model) in enumerate(results):
                    print("{}) {} - {}".format(i+1, component, model))
                while True:
                    try:
                        choice = int(input("[SYSTEM] > [ВЕРНУТЬСЯ В ГЛАВНОЕ МЕНЮ НАЖМИТЕ ENTER] > ЧТО БЫ КУПИТЬ ТОВАР ВВЕДИТЕ ЕГО НОМЕР: "))
                        if choice > 0 and choice <= len(results):
                            os.system('cls')
                            component, model = results[choice-1]
                            print("[SYSTEM] > ВЫ ВЫБРАЛИ: {} - {}".format(component, model))
                            ask_buy = input('[SYSTEM] > ВВЕДИТЕ [Y] ЧТО БЫ ПОДВЕРДИТЬ ПОКУПКУ\n[SYSTEM] > ВВЕДИТЕ [N] ЧТО БЫ ОТМЕНИТЬ\nВАШ ВЫБОР: ')
                            if ask_buy == 'y':
                                 pass
                            if ask_buy == 'n':
                                 os.system('cls')
                                 obj_returnbuy = ScearhRussia(comp_dict)
                                 obj_returnbuy.search_prompt()



                    except ValueError:
                         os.system('cls')
                         obj_return = ScearhRussia(comp_dict)
                         obj_return.search_prompt()



            else:
                os.system('cls')
                procces_scearh_item_ru()
                time.sleep(0.1)
                os.system('cls')
                close_matches = [k for k in self.comp_dict.keys() if search_str.lower() in k.lower()]
                if close_matches:
                    os.system('cls')
                    print(f"[SYSTEM] > '{search_str}' НИЧЕГО НЕ НАЙДЕНО. ВОЗМОЖНО ВЫ ИСКАЛИ: {', '.join(close_matches)}")
                    time.sleep(3)


                else:
                    os.system('cls')
                    os.system('cls')
                    time.sleep(0.1)
                    print(f"[SYSTEM] > ПО ЗАПРОСУ '{search_str}' НИЧЕГО НЕ НАЙДЕНО.")
                    time.sleep(1.5)
                    os.system('cls')

class ScearhEnglish:
    def __init__(self, comp_dict):
        self.comp_dict = comp_dict

    def search_component(self, search_str):
        possible_components = []
        for component, models in self.comp_dict.items():
            for model in models:
                if search_str.lower() in model.lower():
                    possible_components.append((component, model))
        return possible_components

    def search_prompt(self):
        while True:
            search_str = input("Введите название товара (для выхода введите 'выход'): ")
            if search_str == 'выход':
                print("До свидания!")
                break
            results = self.search_component(search_str)
            if results:
                print("Найденные компоненты:")
                for i, (component, model) in enumerate(results):
                    print("{}) {} - {}".format(i+1, component, model))
                while True:
                    try:
                        choice = int(input("Выберите компонент (введите номер): "))
                        if choice > 0 and choice <= len(results):
                            component, model = results[choice-1]
                            print("Вы выбрали: {} - {}".format(component, model))
                            break
                        else:
                            print("Некорректный ввод. Попробуйте еще раз.")
                    except ValueError:
                        print("Некорректный ввод. Попробуйте еще раз.")
            else:
                close_matches = [k for k in self.comp_dict.keys() if search_str.lower() in k.lower()]
                if close_matches:
                    print(f"По запросу '{search_str}' ничего не найдено. Возможно, вы искали: {', '.join(close_matches)}")
                else:
                    print(f"По запросу '{search_str}' ничего не найдено.")



class CategoriesScearhRussia:

     def CategoriesScearhRU(self):
          table = Table(title="Категорий")

          table.add_column("Номер Категорий", style="cyan", no_wrap=True)
          table.add_column("Категорий", style="magenta")
          table.add_column("Товар в Наличий", justify="right", style="green")

          table.add_row("1", "Видеокарты", "✅")
          table.add_row("2", "Процессоры", "✅")
          table.add_row("3", "Материнские Платы", "✅")
          table.add_row("4", "Корпус", "✅")
          table.add_row("5", "HDD/SSD", "✅")
          table.add_row("6", "Блок Питания", "✅")
          table.add_row("7", "Оперативная Память", "✅")
          table.add_row("8", "Охлаждение", "✅")
          table.add_row("9", "Клавиатура", "✅")
          table.add_row("10", "Мониторы", "✅")
          table.add_row("11", "Игровые Мышки", "✅")
          table.add_row("12", "Программное Обеспечение", "✅")
          console.print(table)

          while True:
               ask_categories_scearh_ru = input('[SYSTEM] > ВЕРНУТЬСЯ К ПОИСКУ [1]: ')
               if ask_categories_scearh_ru == '1':
                    os.system('cls')
                    obj_return_categories_ru = ScearhRussia(comp_dict)
                    obj_return_categories_ru.__init__
                    obj_return_categories_ru.search_prompt()
                    break

               else:
                    os.system('cls')
                    obj_else_return_categories_ru = CategoriesScearhRussia()
                    obj_else_return_categories_ru.CategoriesScearhRU()




def menu_shop_ru():
     while True:

         menu_shop_enter = input('[SHOP] > ПРИВЕСТВУЕМ ВАС В ГЛАВНОЙ СИСТЕМЕ НАШЕГО ПРИЛОЖЕНИЯ!\n----------------------------------\n[SHOP] > ПОЧИТАТЬ СПРАВКУ ПРО ПРИЛОЖЕНИЕ МОЖЕТЕ ПРОСТО ВПИСЫВАТЬ В НИЖНЫЙ РЕГИСТЕР ЦИФРУ [15]\n----------------------------------\n[SHOP] > ГЛАВНОЕ МЕНЮ:\n----------------------------------\n[1] > КАТЕГОРИЙ ВСЕХ ТОВАРОВ\n----------------------------------\n[2] > ПОИСК ПО НАЗВАНИЮ\n----------------------------------\n[3] > МОЙ ПРОФИЛЬ\n----------------------------------\n[4] > МОИ ЗАКАЗЫ\n----------------------------------\n[5] > СВЯЗЬ С ПОДДЕРЖКОЙ\n----------------------------------\n[6] > ВЕРНУТЬСЯ К ВЫБОРУ ЯЗЫКА\n----------------------------------\n[7] > ВЫЙТИ ИЗ ПРИЛОЖЕНИЯ\n----------------------------------\n[8] > ВАШ ВЫБОР: ')
         if menu_shop_enter == '1':
              os.system('cls')
              categories_obj_ru = CategoriesRussia()
              categories_obj_ru.ShopMainMenuRu()
              break
         if menu_shop_enter == '2':
              os.system('cls')
              obj_ru = ScearhRussia(comp_dict)
              obj_ru.search_prompt()
         if menu_shop_enter == '2':
              pass
         if menu_shop_enter == '3':
              pass
         if menu_shop_enter == '4':
              pass
         if menu_shop_enter == '5':
              pass
         if menu_shop_enter == '6':
              os.system('cls')
              return lang_menu()
         if menu_shop_enter == '7':
              pass
         if menu_shop_enter == '8':
              pass
         else:
              os.system('cls')
              continue

def menu_shop_en():
     while True:
         menu_shop_enterEN = input('[SHOP] > WELCOME TO THE MAIN SYSTEM OF OUR APP!\n----------------------------------\n[SHOP] > READ THE HELP ABOUT THE APPLICATION YOU CAN SIMPLY ENTER THE NUMBER [15] IN THE LOWER CASE\n----------------------------------\n[SHOP] > MAIN MENU:\n----------------------------------\n[1] > CATEGORIES OF ALL PRODUCTS\n----------------------------------\n[2] > SEARCH BY NAME\n----------------------------------\n[3] > MY PROFILE\n----------------------------------\n[4] > MY ORDERS\n----------------------------------\n[5] > CONTACT SUPPORT\n----------------------------------\n[6] > BACK TO SELECT LANGUAGE\n----------------------------------\n[7] > EXIT APP\n----------------------------------\n[8] > YOUR CHOICE: ')
         if menu_shop_enterEN == '1':
              os.system('cls')
              categories_obj_en = CategoriesEnglish()
              categories_obj_en.ShopMainMenuEn()
              break
         if menu_shop_enterEN == '2':
             pass
         if menu_shop_enterEN == '2':
              pass
         if menu_shop_enterEN == '3':
              pass
         if menu_shop_enterEN == '4':
              pass
         if menu_shop_enterEN == '5':
              pass
         if menu_shop_enterEN == '6':
              os.system('cls')
              return lang_menu()
         if menu_shop_enterEN == '7':
              pass
         if menu_shop_enterEN == '8':
              pass
         if menu_shop_enterEN == '15':
              pass
         else:
              os.system('cls')
              continue

def menu_en():
     while True:
          menu_bar = input('[MENU] > CHOOSE MENU\n[MENU] > RETURN TO LANGUAGE MENU [4]\n-----------------------\n[1] > LOGIN\n-----------------------\n[2] > REGISTER\n-----------------------\n[MENU] YOUR INPUT:')
          if menu_bar == '1':
               os.system('cls')
               login_obj = LoginEnglish()
               login_obj.login_en()

          elif menu_bar == '2':
              os.system('cls')
              register_obj = RegisterEnglish()
              register_obj.register()
          elif menu_bar == '4':
              os.system('cls')
              return lang_menu()
          else:
               os.system('cls')
               continue

def menu_ru():
     while True:
          text_ru_menu()
          text_ru_mainmenu_choose()
          text_ru_login_choose()
          text_ru_reg_choose()
          menu_bar = input('[МЕНЮ] ВАШ ВЫБОР:')
          if menu_bar == '1':
               os.system('cls')
               loginru_obj = LoginRussia()
               loginru_obj.login_ru()
               break

          elif menu_bar == '2':
              os.system('cls')
              regru_obj = RegisterRussia()
              regru_obj.register_rus()
              regru_obj.register_ru()
              break
          elif menu_bar == '4':
              os.system('cls')
              return lang_menu()
          else:
               os.system('cls')
               continue




def lang_menu():
    os.system('cls')
    while True:
        text_lang_menu()
        text_lang_choose()
        text_lang_select()
        text_lang_ru_menu()
        text_lang_en_menu()
        text_lang_support_title_menu()
        text_lang_support_menu()
        text_lang_exit_menu()
        attemps = 0
        bar_menu = input('ВАШ ВЫБОР: ')
        if bar_menu == '1':
             os.system('cls')
             menu_ru()
             break
        if bar_menu == '2':
            os.system('cls')
            menu_en()
            break
        if bar_menu == '3':
            os.system('cls')
            ask_lang = input('[SYSTEM] > [ВЕРНУТЬСЯ В ГЛАВНОЕ МЕНЮ/RETURN TO MAIN MENU 4]\n----------------------------------------------------\n[SYSTEM] > [ВЫБЕРИТЕ ЯЗЫК/LANG CHOOSE]\n-------------------------------------------------------------\n[1].РУССКИЙ\n---------------------------------------------\n[2].ENGLISH\n-------------------------------------------------------------\n[SYSTEM] > ВАШ ВЫБОР/YOUR INPUT: ')
            if ask_lang == '1':
                 os.system('cls')
                 rusupport = SupportRussia()
                 rusupport.support_ru()
                 rusupport.message_support()
                 break
            elif ask_lang == '2':
                 os.system('cls')
                 ensupport = SupportEnglish()
                 ensupport.support_en()
                 ensupport.message_supporten()
                 break
            if ask_lang == '4':
                 os.system('cls')
                 return lang_menu()
        elif attemps >30:
                 os.system('cls')
                 time.sleep(2)
                 sys.exit()



        if bar_menu == '4':
            os.system('cls')
            while True:
                 ask_exit = input('[SYSTEM] > ВЫ ХОТИТЕ ВЫЙТИ?\YOUR IN THE EXIT?\n---------------------------------------------\n[1].ВЫЙТИ/EXIT\n---------------------------------------------\n[2].НЕТ!ВЕРНУТЬСЯ В ГЛАВНОЕ МЕНЮ/NO! RETURN TO MAIN MENU\n---------------------------------------------\nВАШ ВЫБОР/YOUR INPUT: ')
                 if ask_exit == '1':
                    os.system('cls')
                    procces_message_exit()
                    sys.exit()
                 if ask_exit == '2':
                    os.system('cls')
                    return lang_menu()
                 else:
                      os.system('cls')
                      continue





        else:
            os.system('cls')
            return lang_menu()





lang_menu()





























