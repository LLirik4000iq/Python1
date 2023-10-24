import requests
from bs4 import BeautifulSoup

#WEATHER
responsedeg = requests.get("https://meteo.ua/ua/34/kiev#2023-10-21--15-00")

#USD
responsemin = requests.get("https://minfin.com.ua/ua/currency/usd/")

#EUR
responsefin = requests.get("https://finance.i.ua")

try:
    time_or_currency = input(f"Select what you want to check \n weather, enter w/  \n currency, enter c: ")

    if time_or_currency == "c":
        currency = input(f"USD - u "
                         f"\nEUR - e"
                         f"\nPlease select currency: ")

    #USD-----------------------------------------------------------------------------------------------------------
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
                    result = time_int * choose
                    print(f"{choose} US dollars is {result} UAH")

            if operation == "s":
                choose = int(input("Enter a number of US dollars: "))

                if responsemin.status_code == 200:
                    soup = BeautifulSoup(responsemin.text, features="html.parser")
                    soup_list = soup.find_all("div", {"class": "sc-1x32wa2-9 bKmKjX"})
                    time = soup_list[2]
                    time_int = int(time.text[:2])
                    result = time_int * choose
                    print(f"{choose} US dollars is {result} UAH")

    #EUR-----------------------------------------------------------------------------------------------------------

        if (currency == "e"):
            operation = input(f"Buy - b"
                              f"\nSell - s"
                              f"\nChoose operation: ")

            if operation == "b":
                choose = int(input("Enter a number of Euros: "))

                if responsefin.status_code == 200:
                    soup = BeautifulSoup(responsefin.text, features="html.parser")
                    soup_list = soup.find_all("span", {"class": "value -decrease"})
                    time = soup_list[1]
                    time_int = int(time.text[:2])
                    result = time_int * choose
                    print(f"{choose} euro is {result} UAH")

            if operation == "s":
                choose = int(input("Enter a number of Euros: "))

                if responsefin.status_code == 200:
                    soup = BeautifulSoup(responsefin.text, features="html.parser")
                    soup_list = soup.find_all("span", {"class": "value -decrease"})
                    time = soup_list[0]
                    time_int = int(time.text[:2])
                    result = time_int * choose
                    print(f"{choose} euro is {result} UAH")

    #WEATHER-----------------------------------------------------------------------------------------------------------

    if time_or_currency == "w":
        if responsedeg.status_code == 200:
            soup = BeautifulSoup(responsedeg.text, features="html.parser")
            soup_list = soup.find_all("div", {"class": "weather-detail__main-degree"})
            if soup_list:
                result = soup_list[0].text.strip()
            print(f"{result} in Kyiv now")


    with open(f"TipoTablisa.txt", "a") as file:
        file.write(f"\n{str(result)}")
except NameError:
    print("Error!")
