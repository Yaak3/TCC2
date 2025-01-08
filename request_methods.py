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

def get_unique_trounaments_ids(categories_ids, trounaments):
    unique_trounaments_ids = []

    for category_id in categories_ids:
        response = make_request(f'category/{category_id}/unique-tournaments')
        response_data = response['groups'][0]

        for data in response_data['uniqueTournaments']:
            if(data['name'] in trounaments):
                unique_trounaments_ids.append(data['id'])

    
    return unique_trounaments_ids
