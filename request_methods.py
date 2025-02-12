import requests
from constants import __BASE_URL
from time import sleep

def make_request(endpoint):
    try:
        response = requests.get(__BASE_URL + endpoint)
        sleep(0.5)
        response.raise_for_status()

        response = response.json()

        return response
    except requests.exceptions.HTTPError as err:
        print(f"Erro HTTP: {err}")
    except requests.exceptions.RequestException as err:
        print(f"Erro de conexão: {err}")
    except ValueError:
        print("Erro ao processar a resposta JSON.")

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

def get_season_players(tournament_id, season_id):
    players = {}
    offset = 0
    season_players = []

    while(True):
        response = make_request(f'unique-tournament/{tournament_id}/season/{season_id}/statistics?limit=100&offset={offset}')

        response_data = response['results']

        if(len(response_data) == 0):
            break
                
        for data in response_data:
            season_players.append(data['player']['id'])

        offset += 100

    return season_players

def get_player_positions(player_id):
    response = make_request(f'player/{player_id}/characteristics')

    return response

def get_player_season_statistics(player_id, tournament_id, season_id):
    player_statistics = {}
    
    response = make_request(f'player/{player_id}/unique-tournament/{tournament_id}/season/{season_id}/statistics/overall')
    
    player_statistics['statistics'] = response['statistics']
    player_statistics['team'] = response['team']
    
    return player_statistics

def get_player_season_heatmap(player_id, tournament_id, season_id):
    heatmap = {}
    
    response = make_request(f'player/{player_id}/unique-tournament/{tournament_id}/season/{season_id}/heatmap')

    heatmap['points'] = response['points']
    heatmap['matches'] = response['matches']

    return heatmap

def get_player_characteristics(player_id):
    response = make_request(f'player/{player_id}')

    return response

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