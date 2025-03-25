import re
import unicodedata
from os import makedirs, path
from json import dump, loads
import matplotlib.pyplot as plt
import seaborn as sns
from constants import __DATA_BASE_DIR

def convert_directory_name(tournament):
    
    normalized_string = unicodedata.normalize('NFKD', tournament).encode('ASCII', 'ignore').decode('utf-8')
    
    directory_name = re.sub(r'\s+', '_', normalized_string)
    
    directory_name = re.sub(r'[^\w_]', '', directory_name)
    
    directory_name = directory_name.lower()
    
    return directory_name

def normalize_year(year):
    return re.sub(r'\/', '_', year)

def create_directory(tournament, year):

    directory_to_create = convert_directory_name(tournament)
    normalized_year = normalize_year(year)
    directory_to_create = f'{directory_to_create}/{normalized_year}'

    makedirs(f'{__DATA_BASE_DIR}{directory_to_create}', exist_ok=True)

    return directory_to_create

def save_to_json(data, filename):
    with open(filename, "w", encoding="utf-8") as json_file:
        dump(data, json_file, ensure_ascii=False, indent=4)

def update_pointer(tournament, season, player, pointer):
    new_pointer = {tournament: {season: player}}
    pointer.update(new_pointer)

    with open('./data/pointer', "w", encoding="utf-8") as json_file:
        dump(pointer, json_file, ensure_ascii=False, indent=4)

    return pointer

def generate_pointer():
    file = './data/pointer'
    pointer = {}
    
    if(path.exists(file)):
        with open(file, 'r') as file:
            pointer = loads(file.read())

    return pointer

def generic_bar_graph(categories, values, x_label, y_label, title, x_rotation=0, x_size=8, y_size=6):

    plt.bar(categories, values, color='blue')
    plt.title(title)
    plt.xlabel(x_label)
    plt.xticks(rotation=x_rotation)
    plt.ylabel(y_label)

    return plt.show()

def generic_distribution_plot(data, variables, graphs_per_row=3, bins_dict=None):
    num_vars = len(variables)
    num_rows = -(-num_vars // graphs_per_row)
    

    fig, axes = plt.subplots(num_rows, graphs_per_row, figsize=(graphs_per_row * 5, num_rows * 4))
    axes = axes.flatten()
    
    
    for i, var in enumerate(variables):
        bins = bins_dict.get(var, 10) if bins_dict else 10  
        sns.histplot(data=data, x=var, kde=True, bins=bins, ax=axes[i])
        axes[i].set_title(f'Distribuição de {var} ({bins} bins)')
    
    
    for j in range(len(variables), len(axes)):
        fig.delaxes(axes[j])
    
    
    plt.tight_layout()
    plt.show()

def generic_plot_boxplots(data, variables, graphs_per_row=3):
    num_vars = len(variables)
    num_rows = -(-num_vars // graphs_per_row)
    
    fig, axes = plt.subplots(num_rows, graphs_per_row, figsize=(graphs_per_row * 5, num_rows * 4))
    axes = axes.flatten()
    
    
    for i, var in enumerate(variables):
        sns.boxplot(data=data, y=var, ax=axes[i], color='skyblue')
        axes[i].set_title(f'Boxplot de {var}')
        axes[i].set_xlabel('')
    
    
    for j in range(len(variables), len(axes)):
        fig.delaxes(axes[j])
    
    
    plt.tight_layout()
    plt.show()