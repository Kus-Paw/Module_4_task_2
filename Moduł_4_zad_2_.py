import sys
import logging
logging.basicConfig(level=logging.DEBUG)

print("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:")

choice = input ("Wciśnij odpowiedni klawisz: ")
number_1 = float(input("Podaj składnik 1 "))
number_2 = float(input ("Podaj sładnik 2 "))
if (choice == "1"):
    logging.info ("Dodaję ", number_1, "i ",  number_2)
    summary = number_1 + number_2
    print("Wynik to", summary)
elif (choice == "2"):
    logging.info ("Odejmuję", number_1, "i",  number_2)
    subtraction = number_1 - number_2
    print("Wynik to:", (subtraction))
elif (choice == "3"):
    logging.info ("Mnoże", number_1, "i", number_2)
    multiplication = number_1 * number_2
    print("Wynik to:", multiplication)
elif (choice == "4"):
    logging.info ("Dzielę", number_1, "i", number_2)
    split = number_1 / number_2
    print("Wynik to:", split)

logging.info("The program was called with this parameters %s" % choice)
logging.debug("First parameter is %s" % number_1)
logging.debug("Second parameter is %s" % number_2)
    
logging.basicConfig(level=logging.DEBUG, format='%(asctime)f %(message)f', filename="logfile.log")


