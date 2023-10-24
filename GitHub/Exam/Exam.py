import requests
from bs4 import BeautifulSoup

responsemin = requests.get("https://minfin.com.ua/ua/currency/usd/")
responsefin = requests.get("https://finance.i.ua")

responsedeg = requests.get("https://meteo.ua/ua/34/kiev#2023-10-21--15-00")

time_or_currency = input(f"Choose what do you want to check \tcurrency, enter c  or \tweather, enter w: ")

if time_or_currency == "c":
    currency = input(f"USD - u "
                     f"\nEUR - e"
                     f"\nGBP - p"
                     f"\nChoose currency: ")

    if(currency == "u"):
        operation = input(f"Buy - b"
                      f"\nSell - s"
                      f"\nChoose operation: ")

        if operation == "b":
            choose = int(input("Enter a number of US dollars: "))

            if responsemin.status_code == 200:
                soup = BeautifulSoup(responsemin.text, features="html.parser")
                soup_list = soup.find_all("div", {"class": "sc-1x32wa2-9 bKmKjX"})
                time = soup_list[0]
                time_int = int(time.text[:2])
                print(f"{choose} US dollars is {time_int * choose} grivnas")

        if operation == "s":
            choose = int(input("Enter a number of US dollars: "))

            if responsemin.status_code == 200:
                soup = BeautifulSoup(responsemin.text, features="html.parser")
                soup_list = soup.find_all("div", {"class": "sc-1x32wa2-9 bKmKjX"})
                time = soup_list[2]
                time_int = int(time.text[:2])
                print(f"{choose} US dollars is {time_int * choose} grivnas")

