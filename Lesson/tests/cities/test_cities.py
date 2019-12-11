import filecmp

from pandas.util.testing import assert_frame_equal

from apps.cities.cities import *
from settings import CITIES_CSV_FILE

def test_cities():
    # assert show_file('../../' + CITIES_CSV_FILE) == []
    datas = show_file('../../' + CITIES_CSV_FILE)
    f = open("dataframe.txt", "w+", encoding='utf-8')
    f.write(datas.to_string())
    f.close()
    df = open("dataframe.txt",  encoding='utf-8')
    # sample = pd.DataFrame({'a': [1, 2], 'b': [3.0, 4.0]})
    sample = open("golden-master.txt", encoding='utf-8')
    # assert_frame_equal(df, sample)
    assert df.read() == sample.read()
    # assert filecmp.cmp("dataframe.txt", "golden-master.txt", shallow=False)
    # df.close()

    # assert datas == sample
    # print(sample)
    # print(datas)

