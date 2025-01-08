import requests
from request_methods import get_categories_ids, get_unique_trounaments_ids
from constants import __BASE_URL, __CATEGORIES, __TROUNAMENTS

try:
    categories_ids = get_categories_ids(__CATEGORIES)
    unique_trounaments_ids = get_unique_trounaments_ids(categories_ids, __TROUNAMENTS)
    print(unique_trounaments_ids)

except requests.exceptions.HTTPError as err:
    print(f"Erro HTTP: {err}")
except requests.exceptions.RequestException as err:
    print(f"Erro de conexão: {err}")
except ValueError:
    print("Erro ao processar a resposta JSON.")