import pandas as pd

# CRITERES :
# Taux Réussite Attendu France Total séries
# Taux_Mention_attendu_toutes_series


# Display csv file a table
def get_datas_from_schools_csv(file_path):
    data_frame = pd.read_csv(file_path, low_memory=False, sep=';', skipinitialspace=False)
    return data_frame


def merge_row_by_insee_code(data_frame):
    data_frame_grouped = data_frame.groupby(['Code commune']).sum()
    # solution = {'Index': [3, 1, 2], 'Villes': ['Lyon', 'Lyon', 'Marseille'], 'Population': [1, 2, 3], 'datas': [5, 10, 15]}
    # solution_frame = pd.DataFrame(data=solution, index=None)
    # solution_frame_grouped = solution_frame.groupby(['Villes']).sum()
    # print(data_frame_grouped.mean())
    return data_frame_grouped

