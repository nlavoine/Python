
from apps.cities.cities import *
from settings import CITIES_CSV_FILE


def test_cities():
    datas = get_data_frame_from_csv('../../' + CITIES_CSV_FILE)
    sample = open("golden-master.txt", encoding='utf-8')

    assert datas.head(10).to_string() == sample.read()

