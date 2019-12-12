# fonction ‘main’, ce fichier sera exécuté pour lancer l’application
from apps.cities.cities import get_data_frame_from_cities_csv
from apps.schools.schools import get_data_frame_from_schools_csv
from settings import CITIES_CSV_FILE
from settings import SCHOOLS_CSV_FILE


def main():
    # data_frame_cities = get_data_frame_from_cities_csv(CITIES_CSV_FILE)
    data_frame_schools = get_data_frame_from_schools_csv(SCHOOLS_CSV_FILE)
    print(data_frame_schools.head(30))


if __name__ == '__main__':
    main()

