import sys
import logging
logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":
    def users_input ():
        print("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:")
        choice = input ("Wciśnij odpowiedni klawisz: ")
        number_1 = float(input("Podaj składnik 1: "))
        number_2 = float(input("Podaj składnik 2: "))
        operations (number_1,number_2, choice)
        return
   
    def operations(number_1, number_2, choice):
        if (choice == "1"):
            logging.info ("Dodaję", number_1 + number_2)
        
        elif (choice == "2"):
            logging.info ("Odejmuję", number_1 - number_2)
            
        elif (choice == "3"):
            logging.info ("Mnoże", number_1 * number_2)
            
        elif (choice == "4"):
            logging.info ("Wynik to:", number_1 / number_2)

        logging.info("The program was called with this parameters %s" % choice)
        logging.debug("First parameter is %s" % number_1)
        logging.debug("Second parameter is %s" % number_2)
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)f %(message)f', filename="logfile.log")
users_input()
