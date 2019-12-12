import numpy as np

from apps.cities.cities import get_data_frame_from_csv, sort_column
from settings import CITIES_CSV_FILE
import pandas as pd


def test_get_data_frame_from_csv():
    datas = get_data_frame_from_csv('../../' + CITIES_CSV_FILE)
    sample = open("golden-master.txt", encoding='utf-8')
    assert datas.head(10).to_string() == sample.read()


def test_sort_column():
    ## TODO : Finir cette merde
    datas = sort_column('../../' + 'datas/villes_france_short.csv', 'Population')
    # sample = pd.read_csv("golden-master.txt", low_memory=False, header=None, sep='\t', skipinitialspace=False, names=['A' + str(i) for i in range(26)])
    # print(sample.to_string())
    # datas = {'Index': [1, 2, 3], 'Villes': ['Paris', 'Marseille', 'Lyon'], 'Population': [2, 3, 1]}
    solution = {'Index': [3, 1, 2], 'Villes': ['Lyon', 'Paris', 'Marseille'], 'Population': [1, 2, 3]}
    data_frame = pd.DataFrame(data=datas, index=None)
    solution_frame = pd.DataFrame(data=solution, index=None)
    data_frame = data_frame.sort_values(by=['Population'], ascending=True)
    print(data_frame)
    # print(sample.head(10).to_string())

    assert data_frame.to_string() == solution_frame.to_string()




