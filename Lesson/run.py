# fonction ‘main’, ce fichier sera exécuté pour lancer l’application
from apps.cities.cities import get_data_frame_from_csv
from settings import CITIES_CSV_FILE


def main():
    data_frame = get_data_frame_from_csv(CITIES_CSV_FILE)


if __name__ == '__main__':
    main()

