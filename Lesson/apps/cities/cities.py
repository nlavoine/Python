import pandas as pd


# Display csv file a table
def get_data_frame_from_cities_csv(file_path):
    data_frame = pd.read_csv(file_path, low_memory=False, header=None, sep=',', skipinitialspace=False, names=['A' + str(i) for i in range(26)])
    # data_frame.head(-1)
    # print(data_frame)
    return data_frame


# Sort cities by specific column
def sort_column(file_path, column):
    data_frame = get_data_frame_from_cities_csv(file_path)
    data_frame = data_frame.sort_values(by=[column], ascending=False)
    return data_frame.head(-1)



# Display specific columns
# def show_columns():
#     data_frame[['A4', 'A15']]



# Display 50 first cities
# def show_firsts():
    # data_frame.head(50)