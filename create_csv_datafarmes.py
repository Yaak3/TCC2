from os import listdir
import pandas as pd
from json import loads

data_directory = 'data/'
data_directory_childs = listdir(data_directory)
players_dataframe = pd.DataFrame()

for tournament in data_directory_childs:
    child_directory = listdir(f'{data_directory}{tournament}')

    data = []
    for season in child_directory:
        
        json_files = listdir(f'{data_directory}/{tournament}/{season}/')

        for json_file in json_files:
            with open(f'{data_directory}/{tournament}/{season}/{json_file}', 'r') as file:
                file_data = loads(file.read())

            file_data['season'] = season
            data.append(file_data)

    tournament_dataframe = pd.DataFrame(data)
    tournament_dataframe['tournament'] = tournament
    players_dataframe = pd.concat([players_dataframe, tournament_dataframe])

players_dataframe.to_csv('csv_datasets/data_from_all_players_tournaments_seasons_dataset.csv')