import pandas as pd

# CRITERES :
# Taux Réussite Attendu France Total séries
# Taux_Mention_attendu_toutes_series

# Display csv file a table
def get_data_frame_from_csv(file_path):
    data_frame = pd.read_csv(file_path, low_memory=False, header=None, sep=';', skipinitialspace=False)

    return data_frame
