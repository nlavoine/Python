
from apps.cities.cities import *
from settings import CITIES_CSV_FILE


def create_golden_master():
    datas = show_file('../../' + CITIES_CSV_FILE)
    f = open("golden-master.txt", "w+", encoding='utf-8')
    f.write(datas.to_string())
    f.close()
    print("File created")


if __name__ == '__main__':
    create_golden_master()
