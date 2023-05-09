from httpx import Client

poke = input('qual pokemon?')

with Client(base_url='https://pokeapi.co/api/v2/') as client:
    response = client.get(f'/pokemon/{poke}')
    id_ = response.json().get('id')

    response = client.get(f'/pokemon-species/{id_}')
    evolution_chain = response.json().get('evolution_chain').get('url')
    print(evolution_chain)

    response = client.get(evolution_chain)
    evolution_name = response.json().get('chain').get('evolves_to')[0].get('species').get('name')
    print(evolution_name)