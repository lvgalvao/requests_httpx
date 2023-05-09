from httpx import Client

pokes = ['pikachu', 'charmander', 
        'squirtle', 'bulbasaur',
        'chikorita', 'cyndaquil',
        'totodile', 'treecko',
        'torchic', 'mudkip']

def get_evolution_chain(poke):
    print(f'evolução do {poke}')
    with Client(base_url='https://pokeapi.co/api/v2/') as client:
        response = client.get(f'/pokemon/{poke}')
        id_ = response.json().get('id')

        response = client.get(f'/pokemon-species/{id_}')
        evolution_chain = response.json().get('evolution_chain').get('url')
        response = client.get(evolution_chain)
        evolution_name = response.json().get('chain').get('evolves_to')[0].get('species').get('name')
        print(f'saíde de {poke} -> {evolution_name}')

for poke in pokes:
    get_evolution_chain(poke)