


#-_-_-_-_-_-_LİBRAYS_-_-_-_-_-_-_#



import os
import string
from random import sample
from time import time
from tkinter import Y
from urllib import response
from ip2geotools.databases.noncommercial import  DbIpCity
import socket
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from pygame import image
import qrcode 
from turtle import *
import pyfiglet
import sys
from datetime import datetime
import time
import instaloader


os.system("title Code Hub Community")
os.system("color 0a")
os.system("cls")



#-_-_-_-_-_-_FUNCTİONS_-_-_-_-_-_-_#



def port_scanner():
  ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
  print(ascii_banner)
  
  # Defining a target
  if len(sys.argv) == 2:
     
     # translate hostname to IPv4
     target = socket.gethostbyname(sys.argv[1])
  else:
     print("Invalid amount of Argument")
 
 # Add Banner
  print("-" * 50)
  print("Scanning Target: " + target)
  print("Scanning started at:" + str(datetime.now()))
  print("-" * 50)
  
  try:
     
      # will scan ports between 1 to 65,535
     for port in range(1,65535):
          s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
          socket.setdefaulttimeout(1)
         
          # returns an error indicator
          result = s.connect_ex((target,port))
          if result ==0:
              print("Port {} is open".format(port))
          s.close()
         
  except KeyboardInterrupt:
          print("\n Exiting Program !!!!")
          sys.exit()
  except socket.gaierror:
          print("\n Hostname Could Not Be Resolved !!!!")
          sys.exit()
  except socket.error:
          print("\ Server not responding !!!!")
          sys.exit()

def net_ping_clear():
    os.system("ipconfig")
    v1 =(input(" Default Gateway yazan yeri giriniz: "))
    os.system(" ping -t "+ v1 )

def net_password_clear():
    os.system("netsh wlan show profile")
    net_name = input("Network Name: ")
    os.system("netsh wlan show profile "+net_name+" key=clear")
    print(" Key Content:  Yazan kısım internet şifrenizi gösterir.")

def insta_veri():
  URL = "https://www.instagram.com/"

  def verileri_al(kullanici_adi):
      son_url = URL + kullanici_adi
      request = Request(son_url, headers={'User-Agent':'Mozilla/5.0'})
      html_verisi = urlopen(request).read()
      soup = BeautifulSoup(html_verisi, 'html.parser')
      veri = soup.find("meta",property="og:description").attrs['content']
      veri = veri.split("-")[0]
      veri = veri.split(" ")

      print("takipci sayisi: "+veri[0])
      print("takip edilen sayisi: "+veri[2])
      print("gonderi sayisi: "+veri[4])
  kullanici_adi = input("kullanici adi giriniz: ")
  verileri_al(kullanici_adi)

def pass_creative():
    letters = string.ascii_letters
    digits = string.digits
    puncs = string.punctuation
    total = letters + digits + puncs

    length = int(input("Şifre uzunluğu: "))
    password = "".join(sample(total, length))

    print("Şifre: ", password)

def web_ip():
  url = input('Web site urlsi giriniz: ')
  ip = socket.gethostbyname(url)
  print('CODE HUB')
  response = DbIpCity.get(ip, api_key='free')

  print('İP ADRESİ: ', ip)
  print('ŞEHİR: ', response.city)
  print('ÜLKE: ', response.country)
  print('BÖLGE: ', response.region) 
    
def win10logo():
  speed(2)
  bgcolor("black")
  penup()
  goto(-50, 60)
  pendown()
  color("#00adef")
  begin_fill()
  goto(100, 100)
  goto(100, -100)
  goto(-50, -60)
  goto(-50, 60)
  end_fill()
  color("black")
  goto(15, 100)
  color("black")
  width(10)
  goto(15, -100)
  penup()
  goto(100, 0)
  pendown()
  goto(-100, 0)
  done()

def qrcodecreative():
  code = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=100,
    border=4,
 )

  text = input('Lütfen QR Kod için bir Sitring değer giriniz: ')

  code.add_data(text)
  code.make(fit=True)

  image = code.make_image(fill_color="white", back_color="black")
  image.save('qrcode.png')

def instaloder2():

    ig = instaloader.Instaloader()
    profile = input("Kullanıcı adı giriniz: ")
    ig.download_profile(profile, profile_pic=True)
    print("Biyografi:", profile.biography)
    #bu şekilde kullanıcının biyografisini görüntüleriz.
    print("İnternet Sitesi", profile.external_url)
    #bu şekilde kullanıcın internet sitesini görüntüleriz.

def dnsReset():
    os.system('echo off')
    os.system('tittle CodeHub')
    os.system('colo a')
    os.system('cls')
    os.system('ipconfig/flushdns')
    print("DNS Adresiniz Yenilendi")

def proxyReset():
    os.system('echo off')
    os.system('tittle CodeHub')
    os.system('colo a')
    os.system('cls')
    os.system('netsh winhttp reset')
    print("Proxy Adresiniz Yenilendi")


#-_-_-_-_-_-_İFELİFELSE_-_-_-_-_-_-_#



while True:
    print("""

 ██████╗ ██████╗ ██████╗ ███████╗    ██╗  ██╗██╗   ██╗██████╗ 
██╔════╝██╔═══██╗██╔══██╗██╔════╝    ██║  ██║██║   ██║██╔══██╗
██║     ██║   ██║██║  ██║█████╗      ███████║██║   ██║██████╔╝
██║     ██║   ██║██║  ██║██╔══╝      ██╔══██║██║   ██║██╔══██╗
╚██████╗╚██████╔╝██████╔╝███████╗    ██║  ██║╚██████╔╝██████╔╝
 ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝    ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ 
                    C  O  M  M  U  N  I  T  Y


""")
    time.sleep(3)
    print("""

 >1  Port Scanner
 >2  Net Ping Clear
 >3  Net Password Show
 >4  Instagram User İnfo
 >5  Password Creativ
 >6  Web IP Adresi
 >7  Win10 Logo
 >8  QR Code Creativ
 >9  Instagram PP download
 >10 DNS Reset
 >11 Proxy Reset
 >q  Exit
 >y  Communication


""")
    secim = input("Seçiminizi giriniz: ")
    if secim == "1":
        port_scanner()
        print("wait 10 seconds")
        time.sleep(10)
        os.system("cls")
        continue
    elif secim == "2":
        net_ping_clear()
        print("wait 10 seconds")
        time.sleep(10)
        os.system("cls")
        continue
    elif secim == "3":
        net_password_clear()
        print("wait 10 seconds")
        time.sleep(10)
        os.system("cls")
        continue
    elif secim == "4":
        insta_veri()
        print("wait 10 seconds")
        time.sleep(10)
        os.system("cls")
        continue
    elif secim == "5":
        pass_creative()
        print("wait 10 seconds")
        time.sleep(10)
        os.system("cls")
        continue
    elif secim == "6":
        web_ip()
        print("wait 10 seconds")
        time.sleep(10)
        os.system("cls")
        continue
    elif secim == "7":
        win10logo()
        print("wait 10 seconds")
        time.sleep(10)
        os.system("cls")
        continue
    elif secim == "8":
        qrcodecreative()
        print("wait 10 seconds")
        time.sleep(10)
        os.system("cls")
        continue
    elif secim == "9":
        instaloder2()
        print("wait 10 seconds")
        time.sleep(10)
        os.system("cls")
        continue
    elif secim == "10":
        dnsReset()
        print("wait 5 seconds")
        time.sleep(5)
        os.system("cls")
        continue
    elif secim == "11":
        proxyReset()
        print("wait 5 seconds")
        time.sleep(5)
        os.system("cls")
        continue
    elif secim == "y":
        print("""
      
      Discord: https://discord.io/yazlm
      Blogger: https://codehubcommunity.blogspot.com
      Github:  https://github.com/ErenRip
      Youtube: https://www.youtube.com/channel/UCryC_n_60Kd6CEI94wOi87Ay
      G-Mail:  erenripilt@gmail.com

     
      wait 10 seconds
      """)
        time.sleep(10)
        os.system("cls")
        continue
        
    elif secim == "q":
        print("\n Exiting Program !!!!")
        sys.exit()
    else:
        print("\n Hatalı giriş yaptınız !!!!")


