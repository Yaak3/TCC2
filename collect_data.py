from request_methods import get_categories_ids, get_unique_tournaments, get_unique_tournament_seasons, get_season_players, get_player_positions, get_player_characteristics, get_player_season_heatmap, get_player_season_statistics
from constants import __CATEGORIES, __TROUNAMENTS, __SEASON_YEARS, __DATA_BASE_DIR
from utils import create_directory, save_to_json

def collect_and_save_to_json(unique_tournaments, unique_tournament_season_ids):

    for tournament, tournament_id in unique_tournaments.items():

        for season in unique_tournament_season_ids[tournament]:
            directory_created = create_directory(tournament, season['year'])

            season_players = get_season_players(season_id=season['id'], tournament_id=tournament_id)

            for player in season_players:
                player_data = {}

                player_positions = get_player_positions(player_id=player)
                player_characteristics = get_player_characteristics(player_id=player)
                player_season_heatmap = get_player_season_heatmap(player_id=player, tournament_id=tournament_id, season_id=season['id'])
                player_season_statistics = get_player_season_statistics(player_id=player, season_id=season['id'], tournament_id=tournament_id)

                player_data.update(player_positions)
                player_data.update(player_characteristics)
                player_data.update(player_season_heatmap)
                player_data.update(player_season_statistics)

                player_file_name = f'{__DATA_BASE_DIR}{directory_created}/{player}.json'

                save_to_json(player_data, player_file_name)
                break

            break
    
        break


categories_ids = get_categories_ids(__CATEGORIES)
unique_trounaments = get_unique_tournaments(categories_ids, __TROUNAMENTS)
unique_tournament_season_ids = get_unique_tournament_seasons(unique_trounaments, __SEASON_YEARS)
print(unique_trounaments)
print(unique_tournament_season_ids)
#collect_and_save_to_json(unique_trounaments, unique_tournament_season_ids)

print("Coleta dos dados finalizada!")