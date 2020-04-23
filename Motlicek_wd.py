import argparse
import sys


def main():
    muj_parser = argparse.ArgumentParser(description='Soubor.')
    muj_parser.add_argument('soubor')
    muj_parser.add_argument("radky", help="Spočítat řádky", action="store_true")
    muj_parser.add_argument("znaky", help="Spočítat znaky", action="store_true")
    muj_parser.add_argument("slova", help="Spočítat slova", action="store_true")

    argumenty = muj_parser.parse_args()

    try:
        f = open(argumenty.soubor, "r")
        soubor = f.read()
        flag = False
        if argumenty.slova:
            pocet_slov = word_counter(soubor)
            print(f"Počet slov: {pocet_slov}")
            flag = True

        if argumenty.znaky:
            pocet_znaku = znaky_counter(soubor)
            print(f"Počet znaků: {pocet_znaku}")
            flag = True

        if argumenty.radky:
            pocet_radku = line_counter(soubor)
            print(f"Počet řádků: {pocet_radku}")
            flag = True

        if not flag:
            pocet_slov = word_counter(soubor)
            pocet_znaku = znaky_counter(soubor)
            pocet_radku = line_counter(soubor)
            print(f"Počet slov: {pocet_slov}\nPočet znaků: {pocet_znaku}\nPočet řádků: {pocet_radku}")
    except:
        print("Houstne, máme problém. Něco se pokazilo. ")
        sys.exit(1)

def word_counter(f):
    pocet_slov = f.count(' ') + len(f.split('\n'))
    return pocet_slov
    pass
def line_counter(f):
    pocet_radku = len(f.split('\n'))
    return pocet_radku
def znaky_counter(f):
    pocet_znaku = len(f)
    return pocet_znaku

main()