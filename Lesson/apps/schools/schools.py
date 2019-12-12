import pandas as pd

# Display csv file a table
def get_data_frame_from_csv(file_path):
    data_frame = pd.read_csv(file_path, low_memory=False, header=None, sep=',', skipinitialspace=False, names=['A' + str(i) for i in range(26)])
    # data_frame.head(-1)
    # print(data_frame)
    return data_frame