import os
from turtle import Turtle
import psutil
from plyer import notification
import time
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

os.system("title Librays Downloader")
os.system("color 0a")
os.system("cls")
print("""

 ██████╗ ██████╗ ██████╗ ███████╗    ██╗  ██╗██╗   ██╗██████╗ 
██╔════╝██╔═══██╗██╔══██╗██╔════╝    ██║  ██║██║   ██║██╔══██╗
██║     ██║   ██║██║  ██║█████╗      ███████║██║   ██║██████╔╝
██║     ██║   ██║██║  ██║██╔══╝      ██╔══██║██║   ██║██╔══██╗
╚██████╗╚██████╔╝██████╔╝███████╗    ██║  ██║╚██████╔╝██████╔╝
 ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝    ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ 
                    C  O  M  M  U  N  I  T  Y


""")
os.system("pip install requests")
os.system("pip install random")
os.system("pip install time")
os.system("pip install tkinter")
os.system("pip install urllib")
os.system("pip install ip2geotools")
os.system("pip install socket")
os.system("pip install bs4")
os.system("pip install urllib")
os.system("pip install pygame")
os.system("pip install qrcode")
os.system("pip install turtle")
os.system("pip install pyfiglet")
os.system("pip install sys")
os.system("pip install string")
os.system("pip install os")
print(f"{Fore.BLUE}İndirme işlemi bitti")





battery=psutil.sensors_battery()

percent = battery.percent
notification.notify(
        title="Code Hub Community",
        message="Kütüphane Yüklemleri Tamamlandı",
        timeout=10
    )

time.sleep(10)
    
os.system("exit")
os.system("exit()")