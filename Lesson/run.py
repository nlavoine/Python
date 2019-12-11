# fonction ‘main’, ce fichier sera exécuté pour lancer l’application
from apps.cities.cities import show_file
from settings import CITIES_CSV_FILE

if __name__ == '__main__':
    show_file(CITIES_CSV_FILE)

