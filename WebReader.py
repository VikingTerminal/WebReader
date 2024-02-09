import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style, Back
import random
import time

def leggi_contenuto_web(dominio):
    try:
        url = f'http://{dominio}'
        response = requests.get(url)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            testo_formattato = ' '.join(soup.stripped_strings)
            
            print(f"\n{Fore.CYAN}Contenuto della pagina {url}:{Style.RESET_ALL}\n")
            
            # Aggiungi effetto "macchina da scrivere" e rendi il testo verde lime
            for char in testo_formattato:
                time.sleep(0.01)  # Ritardo tra i caratteri per effetto "macchina da scrivere"
                colore_testo = Fore.LIGHTGREEN_EX
                print(f"{colore_testo}{char}{Style.RESET_ALL}", end='', flush=True)

            print("\n")
        else:
            print(f"\nErrore {response.status_code}: Impossibile accedere alla pagina {url}")
    except Exception as e:
        print(f"\nErrore durante la richiesta HTTP: {e}")

def main():
    while True:
        dominio = input(f"{Fore.LIGHTYELLOW_EX}Inserisci il dominio (es. www.example.com), o scrivi 'exit' per uscire: {Style.RESET_ALL}")
        
        if dominio.lower() == 'exit':
            print(f"\nGrazie per utilizzare lo script! Cordiali saluti: {Fore.YELLOW}t.me/VikingTerminal{Style.RESET_ALL}")
            break
        elif dominio:
            leggi_contenuto_web(dominio)
        else:
            print("Il dominio inserito non è valido.")

if __name__ == "__main__":
    main()
