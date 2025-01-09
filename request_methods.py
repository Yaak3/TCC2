import requests
from constants import __BASE_URL

def make_request(endpoint):
    response = requests.get(__BASE_URL + endpoint)
    response.raise_for_status()

    response = response.json()

    return response

def get_categories_ids(categories):
    categories_ids = []

    response = make_request('sport/football/categories')
    response_data = response['categories']

    for data in response_data:
        if(data['name'] in categories):
            categories_ids.append(data['id'])

    return categories_ids

def get_unique_tournaments(categories_ids, trounaments):
    unique_tournaments_ids = {}

    for category_id in categories_ids:
        response = make_request(f'category/{category_id}/unique-tournaments')
        response_data = response['groups'][0]

        for data in response_data['uniqueTournaments']:
            if(data['name'] in trounaments):
                unique_tournaments_ids[data['name']] = data['id']

    
    return unique_tournaments_ids

def get_unique_tournament_seasons(unique_tournaments, season_years):
    unique_tournament_season_ids = {}

    for tournamnet, tournament_id in unique_tournaments.items():
        response = make_request(f'unique-tournament/{tournament_id}/seasons')

        response_data = response['seasons']

        season_ids = []

        for index, data in enumerate(response_data):
            years = season_years[tournamnet]

            if(data['year'] in years):
                season_ids.append({'id': data['id'], 'year': data['year']})
            
            if(index + 1 == len(response_data)):
                unique_tournament_season_ids[tournamnet] = season_ids


    return unique_tournament_season_ids

def get_teams_last_season(unique_tournaments, unique_tournament_season_ids):
    players = {}
    offset = 0
    season_players = []

    for tournament, tournament_id in unique_tournaments.items():
        for trounament_seasons in unique_tournament_season_ids[tournament]:
            while(True):
                response = make_request(f'unique-tournament/{tournament_id}/season/{trounament_seasons["id"]}/statistics?limit=100&offset={offset}')

                response_data = response['results']

                if(len(response_data) == 0):
                    break
                
                print(response_data)
                for data in response_data:
                    season_players.append(data['player']['id'])

                break


            players[tournament][trounament_seasons['id']] = season_players

            offset = 0
            season_players = []
                
    return players

'''
TODO: Coletar todos os jogadores de um time, e encontrar uma forma de identificar de qual campeonato cada time pertence

Depois, utilizar os endpoints abaixo para coletar estatisticas dos jogadores

https://www.sofascore.com/api/v1/player/981619/characteristics - coleta as posições dos jogadores

https://www.sofascore.com/api/v1/player/981619/attribute-overviews - coleta o mapa de overview do jogador

https://www.sofascore.com/api/v1/player/981619/statistics/seasons - da para coletar todas as temporadas que o jogador jogou em todos os torneios

https://www.sofascore.com/api/v1/player/981619/unique-tournament/325/season/58766/statistics/overall - pega as estatisticas gerais do jogador na temporada

https://api.sofascore.com/api/v1/player/7635/unique-tournament/8/season/18020/heatmap - pega o heatmap da temporada do jogador

https://www.sofascore.com/api/v1/player/981619 - pega as características fisicas dos jogadores
'''