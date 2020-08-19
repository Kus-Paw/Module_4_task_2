from functools import reduce
import logging
logging.basicConfig(level=logging.DEBUG)

def add(a, b, *args):
    """add 2 or more arguments"""
    logging.info(f"Dodaję: {a}, {b}, {','.join(map(str, args))}")
    return a + b + sum(args)

def sub(a, b, *args):
    logging.info(f"Odejmuję: {a}, {b}, {', '.join(map(str, args))}")
    return a - b

def mul(a, b, *args):
    logging.info(f"Mnożę: {a}, {b}, {', '.join(map(str, args))}")
    return a * b * reduce(lambda x, y: x * y, args)

def div(a, b, *args):
    logging.info(f"Dzielę: {a}, {b}, {', '.join(map(str, args))}")
    if b != 0:
        return a / b
    else:
        raise ZeroDivisionError("Nie dziel przez 0!")

def get_data(op):
    a = int(input("Podaj składnik  1: "))
    b = int(input("Podaj składnik  2: "))
    args = []
    if op in ["1", "3"]:
        while True:
            d = input("Podaj kolejną liczbę lub wpisz k by zakończyć: ")
            if d == "k":
                break
            args.append(int(d))
    return a, b, args

operations = {
    "1": add,
    "2": sub,
    "3": mul,
    "4": div
}

if __name__ == "__main__":
    op = input(
        "Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:"
    )
    a, b, args = get_data(op)

    result = operations[op](a, b, *args)
    print("Wynik to: ", result)

logging.info("The program was called with this parameters %s" % op)
logging.debug("First parameter is %s" % a)
logging.debug("Second parameter is %s" % b)
