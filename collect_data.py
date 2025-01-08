import pprint
import requests
from request_methods import get_categories_ids, get_unique_tournaments, get_unique_tournament_seasons, get_teams_last_season
from constants import __CATEGORIES, __TROUNAMENTS, __SEASON_YEARS

try:
    categories_ids = get_categories_ids(__CATEGORIES)
    unique_trounaments = get_unique_tournaments(categories_ids, __TROUNAMENTS)
    unique_tournament_season_ids = get_unique_tournament_seasons(unique_trounaments, __SEASON_YEARS)
    teams = get_teams_last_season(unique_trounaments, unique_tournament_season_ids)
    
    print(unique_trounaments)
    print(unique_tournament_season_ids)
    print(teams)

except requests.exceptions.HTTPError as err:
    print(f"Erro HTTP: {err}")
except requests.exceptions.RequestException as err:
    print(f"Erro de conexão: {err}")
except ValueError:
    print("Erro ao processar a resposta JSON.")