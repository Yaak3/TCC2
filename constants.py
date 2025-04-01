__CATEGORIES = ['Brazil', 'England', 'Italy', 'Germany', 'Spain', 'France', 'Portugal', 'Belgium', 'USA', 'Argentina', 'Denmark', 'Netherlands', 'Mexico', 'Czech Republic', 'Poland', 'Turkey', 'Switzerland']
__BASE_URL = 'https://api.sofascore.com/api/v1/'
__DATA_BASE_DIR = './data/'
__TROUNAMENTS = ['Brasileirão Betano', 'Premier League', 'Championship', 'Serie A', 'Bundesliga', '2. Bundesliga', 'LaLiga', 'Ligue 1', 'Liga Portugal Betclic', 'Pro League', 'MLS', 'Liga Profesional de Fútbol', 'Danish Superliga', 'Eredivise', 'Liga MX, Apertura', 'Liga MX, Clausura', 'Czech First League', 'Ekstraklasa', 'Trendyol Süper Lig', 'Serie B', 'Swiss Super League']
__SEASON_YEARS = {
    'Brasileirão Betano': ['2024', '2023'],
    'Premier League': ['23/24','22/23'],
    'Championship': ['23/24','22/23'],
    'Serie A': ['23/24','22/23'],
    'Bundesliga': ['23/24','22/23'],
    '2. Bundesliga': ['23/24','22/23'],
    'LaLiga': ['23/24','22/23'],
    'Ligue 1': ['23/24','22/23'],
    'Liga Portugal Betclic': ['23/24','22/23'],
    'Pro League': ['23/24','22/23'],
    'MLS': ['2024', '2023'],
    'Liga Profesional de Fútbol': ['2024', '2023'],
    'Danish Superliga': ['23/24','22/23'],
    'Eredivise': ['23/24','22/23'],
    'Liga MX, Apertura': ['2024', '2023'],
    'Liga MX, Clausura': ['2024', '2023'],
    'Czech First League': ['23/24','22/23'],
    'Ekstraklasa': ['23/24','22/23'],
    'Trendyol Süper Lig': ['23/24','22/23'],
    'Serie B': ['23/24','22/23'],
    'Swiss Super League': ['23/24','22/23']
}
__QUADRANTS = {
    "first": {"top_left": (0, 0), "bottom_right": (25, 25)},
    "second": {"top_left": (26, 0), "bottom_right": (50, 25)},
    "third": {"top_left": (51, 0), "bottom_right": (75, 25)},
    "fourth": {"top_left": (76, 0), "bottom_right": (100, 25)},
    "fifth": {"top_left": (0, 26), "bottom_right": (25, 50)},
    "sixth": {"top_left": (26, 26), "bottom_right": (50, 50)},
    "seventh": {"top_left": (51, 26), "bottom_right": (75, 50)},
    "eighth": {"top_left": (76, 26), "bottom_right": (100, 50)},
    "ninth": {"top_left": (0, 51), "bottom_right": (25, 75)},
    "tenth": {"top_left": (26, 51), "bottom_right": (50, 75)},
    "eleventh": {"top_left": (51, 51), "bottom_right": (75, 75)},
    "twelfth": {"top_left": (76, 51), "bottom_right": (100, 75)},
    "thirteenth": {"top_left": (0, 76), "bottom_right": (25, 100)},
    "fourteenth": {"top_left": (26, 76), "bottom_right": (50, 100)},
    "fifteenth": {"top_left": (51, 76), "bottom_right": (75, 100)},
    "sixteenth": {"top_left": (76, 76), "bottom_right": (100, 100)}
}