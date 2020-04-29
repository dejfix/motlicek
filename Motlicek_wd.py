import argparse
import sys
import requests

def main():
    muj_parser = argparse.ArgumentParser(description='Soubor.')
    muj_parser.add_argument("website", help="Název webu")
    muj_parser.add_argument("--radky", help="Spočítat řádky", action="store_true")
    muj_parser.add_argument("--znaky", help="Spočítat znaky", action="store_true")
    muj_parser.add_argument("--slova", help="Spočítat slova", action="store_true")
    args = muj_parser.parse_args()

    try:
        r = requests.get(args.website)
        f = r.text
        check = False

        if args.radky:
            pocet_radku = len(f.split('\n'))
            print(f"Počet řádků: {pocet_radku}")
            check = True

        if args.znaky:
            pocet_znaku = len(f)
            print(f"Počet znaků: {pocet_znaku}")
            check = True

        if args.slova:
            pocet_slov = f.count(' ') + len(f.split('\n'))
            print(f"Počet slov: {pocet_slov}")
            check = True

        if check == False:
            pocet_slov = f.count(' ') + len(f.split('\n'))
            pocet_znaku = len(f)
            pocet_radku = len(f.split('\n'))
            print(f" Počet řádků: {pocet_radku}\n Počet znaků: {pocet_znaku}\n Počet slov: {pocet_slov}")

    except:
        print("Houstne, máme problém. Něco se pokazilo, asi chyba souboru.")
        sys.exit(1)

main()