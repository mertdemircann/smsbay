#!/usr/bin/env python3
# -*- kodlama: utf-8 -*-

import requests
from os import system as s

import os

os.system("pip install requests")

os.system("apt-get update")

os.system("apt-get upgrade")

os.system("apt-get install curl")

os.system("apt-get install python")

os.system("apt-get install figlet")

os.system("clear")

banner = """
_   ___       __   ____     __          
  / _ )__ __/ /  / / /____/ /_____ ____
 / _  / // / _ \/_  _/ __/  '_/ -_) __/
/____/\_, /_//_/ /_/ \__/_/\_\\__/_/
     /___/     
>>>>> Coder By H4cker <<<<<<

|> Instagram = byh4cker
|> YouTube = H4cker tarafından
|> WebSitesi = https://www.byh4cker.com/
"""

print(banner)

sor = input("Telefon Numarası Örn:+905555555555 >>> ")

mesaj = input("Mesajınız >>> ")

drlm = input("\n| Mesajınız gönderilsin mi?[y/n] >>> ")

if drlm == "y" or drlm == "Y":
    print("\n"+sor+"\n"+arlk+"\n")
    resp = requets.post('https://texbelt.com/text',{
 'phone': sor,
 'message': arlk,
 'key': 'textbelt',
   })
   print(resp.json())
   
elif drlm == "n" or drlm == "N":
    quit()
    else:
       print ( " \|Hata.")