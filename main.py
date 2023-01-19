import random
import os
import time
import requests
import colorama 
from colorama import Style, Fore, Back
from fp.fp import FreeProxy

try:
    from fp.fp import FreeProxy
except ModuleNotFoundError:
    os.system("pip install free-proxy")



colorama.init(autoreset=True)
print(f"{Fore.BLUE}            ╱╱╱╱╱╱╭╮")
print(f"{Fore.CYAN}            ╱╱╱╱╱╱┃┃")
print(f"{Fore.GREEN}            ╭╮╭┳━╮┃┃╭┳━╮╭━━┳╮╭╮╭┳━╮      ")
print(f"{Fore.LIGHTBLUE_EX}            ┃┃┃┃╭╮┫╰╯┫╭╮┫╭╮┃╰╯╰╯┃╭╮╮     ")
print(f"{Fore.LIGHTCYAN_EX}            ┃╰╯┃┃┃┃╭╮┫┃┃┃╰╯┣╮╭╮╭┫┃┃┃╭╮     ")
print(f"{Fore.LIGHTGREEN_EX}            ╰━━┻╯╰┻╯╰┻╯╰┻━━╯╰╯╰╯╰╯╰╯╰╯     ")
print("")
print(f"{Fore.LIGHTGREEN_EX}[0] {Fore.WHITE}mixed proxies\n{Fore.LIGHTGREEN_EX}[1] {Fore.WHITE} HTTP proxies\n{Fore.LIGHTGREEN_EX}[2] {Fore.WHITE}proxies from a country code\n{Fore.LIGHTGREEN_EX}[3] {Fore.WHITE} google proxies\n{Fore.LIGHTGREEN_EX}[4] {Fore.WHITE} anonymous proxies")
option = input(">> ")

if option == "1":
    os.system("cls")
    num = input("enter a number to generate bigger number = more time >> ")
    print(f"{Fore.CYAN} generatiing ....")
    with open("http_proxies.txt", "w", encoding='utf-8') as file:
    
     
     for i in range(int(num)):
      http=FreeProxy(https=True, rand=True).get()
      file.write(http+"\n")
    print(f"{Fore.GREEN} generated {(num)} of http proxies")

elif option == "2":
    os.system("cls")
    cn = input(" enter a country id (2 alpha). check https://www.iban.com/country-codes for country codes : ")
    enter = cn.upper()
    num = input("enter a number to generate : ")
    print(f"{Fore.CYAN} generatiing ....")

    try:
       with open("country_proxies.txt", "w", encoding='utf-8') as file:
    
     
         for i in range(int(num)):
          country=FreeProxy(country_id=[(enter)], rand=True).get()
          file.write(country+"\n")
       print(f"{Fore.GREEN} generated {(num)} of country proxies")
    except ValueError:
       print(f"{Fore.RED} Put numbers. press enter to exit")
       uu = input("")
       if uu == "":
          os.system("exit")
       else:
          os.system("exit")

elif option == "0":
    os.system("cls")
    num = input("enter a number to generate : ")
    print(f"{Fore.CYAN} generatiing ....")

    try:
       with open("proxies.txt", "w", encoding='utf-8') as file:
    
     
         for i in range(int(num)):
          rnd=FreeProxy(rand=True).get()
          file.write(rnd+"\n")
       print(f"{Fore.GREEN} generated {(num)} of proxies")
    except ValueError:
       print(f"{Fore.RED} Put numbers. press enter to exit")
       uu = input("")
       if uu == "":
          os.system("exit")
       else:
          os.system("exit")

    
elif option == "3":
    os.system("cls")
    num = input("enter a number to generate : ")
    print(f"{Fore.CYAN} generatiing ....")

    try:
       with open("google_proxies.txt", "w", encoding='utf-8') as file:
    
     
         for i in range(int(num)):
          google=FreeProxy(google=True, rand=True).get()
          file.write(google+"\n")
          
       print(f"{Fore.GREEN} generated {(num)} of google proxies")
    except ValueError:
       print(f"{Fore.RED} Put numbers. press enter to exit")
       uu = input("")
       if uu == "":
          os.system("exit")
       else:
          os.system("exit")

elif option == "4":
    os.system("cls")
    num = input("enter a number to generate : ")
    print(f"{Fore.CYAN} generatiing ....")

    try:
       with open("anoymous_proxies.txt", "w", encoding='utf-8') as file:
    
     
         for i in range(int(num)):
          anm=FreeProxy(anonym=True, rand=True).get()
          file.write(anm+"\n")
       print(f"{Fore.GREEN} generated {(num)} of anoymous proxies")
    except ValueError:
       print(f"{Fore.RED} Put numbers. press enter to exit")
       uu = input("")
       if uu == "":
          os.system("exit")
       else:
          os.system("exit")

elif option == "5":
   os.sytem("cls")
   print(f" {Fore.GREEN} made by unknown\n{Fore.white} github = ishrak3232\n discord -\nhttps://discord.gg/JD63T8Wg\nhttps://discord.gg/rponfire\n\ndiscord id - 1064034946928357478")

else:
    print("")
    print(f"{Fore.RED}Not a valid input !\n")
    time.sleep(3)
    os.system("exit")