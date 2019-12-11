import pandas as pd


# Display csv file a table
def show_file(csv):
    data_frame = pd.read_csv(csv, low_memory=False, header=None, sep=',', skipinitialspace=False, names=['A' + str(i) for i in range(26)])
    # data_frame.head(-1)
    # print(data_frame)
    return data_frame


# Sort cities by specific column
# def sort_column():
#     data_frame2 = data_frame.sort_values(by=['A15'], ascending=False)
#     data_frame2.head(-1)



# Display specific columns
# def show_columns():
#     data_frame[['A4', 'A15']]



# Display 50 first cities
# def show_firsts():
    # data_frame.head(50)