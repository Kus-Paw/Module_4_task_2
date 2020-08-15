import sys
import logging
logging.basicConfig(level=logging.DEBUG)

print("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:")
def summary():
    dodawanie = number_1 + number_2
    print ("Wynik to:", dodawanie)
def subtraction():
    odejmowanie = number_1 - number_2
    print ("Wynik to:", odejmowanie)
def multiplication():
    mnożenie = number_1 * number_2
    print ("Wynik to:", mnożenie)
def split():
    dzielenie = number_1 / number_2
    print ("Wynik to:", dzielenie)

choice = input ("Wciśnij odpowiedni klawisz: ")
# jeżeli zorbie funkcje pobierania danych od użytkownika np. def number_choices():
# number_1 = float(input("Podaj składnik 1 "))
# number_2 = float(input("Podaj składnik 2 "))
# to mam problem aby wywołać tylko wynik to co wpisał uzytkownik w logging.info ("Dodaję ", number_1, "i ", number_2)

number_1 = float(input("Podaj składnik 1 "))
number_2 = float(input ("Podaj sładnik 2 "))
if (choice == "1"):
    logging.info ("Dodaję ", number_1, "i ", number_2)
    print(summary())
elif (choice == "2"):
    logging.info ("Odejmuję", number_1, "i",  number_2)
    print(subtraction())
elif (choice == "3"):
    logging.info ("Mnoże", number_1, "i", number_2)
    print(multiplication())
elif (choice == "4"):
    logging.info ("Dzielę", number_1, "i", number_2)
    print(split())

logging.info("The program was called with this parameters %s" % choice)
logging.debug("First parameter is %s" % number_1)
logging.debug("Second parameter is %s" % number_2)
    
logging.basicConfig(level=logging.DEBUG, format='%(asctime)f %(message)f', filename="logfile.log")

