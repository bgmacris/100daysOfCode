import requests

key = 'RGAPI-844835f9-ed83-464f-bcec-6d201b1b2fb0'
API_KEY = f'?api_key={key}'

global PLAYER_DATA, ACTIVE_GAME, PLAYER_LEAGE, PLAYER_MATCH, MATCH
PLAYER_DATA = 'https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/'
ACTIVE_GAME = 'https://euw1.api.riotgames.com/lol/lol/spectator/v4/active-games/by-summoner/'
PLAYER_LEAGE = 'https://euw1.api.riotgames.com/lol/league/v4/entries/by-summoner/'
PLAYER_MATCH = 'https://euw1.api.riotgames.com/lol/match/v4/matchlists/by-account/'
MATCH = 'https://euw1.api.riotgames.com/lol/match/v4/timelines/by-match/'

global champions
champions = requests.get('http://ddragon.leagueoflegends.com/cdn/6.24.1/data/en_US/champion.json').json()['data']
def search_champion(id):
    for i in champions:
        if champions[i]['key'] == str(id):
            return i

def get_player_id(name):
    response = requests.get(f'{PLAYER_DATA}{name}{API_KEY}')
    if response.status_code == 200:
        return response.json()['id']
    else:
        return response.status_code

def get_player_count_id(name):
    response = requests.get(f'{PLAYER_DATA}{name}{API_KEY}')
    if response.status_code == 200:
        return response.json()['accountId']
    else:
        return response.status_code

def get_active_game(id):
    response = requests.get(f'{ACTIVE_GAME}{id}{API_KEY}')
    if response.status_code == 200:
        return response.json()
    else:
        return False

def get_player_leage(id):
    response = requests.get(f'{PLAYER_LEAGE}{id}{API_KEY}')
    if response.status_code == 200:
        data = response.json()
        if data != []:
            return {
                'tier': data[0]['tier'],
                'rank': data[0]['rank']
            }
        else:
            return 'NO'
    else:
        return False

def get_player_matches(id):
    response = requests.get(f'{PLAYER_MATCH}{id}{API_KEY}')
    if response.status_code == 200:
        data = response.json()
        for i in data['matches']:
            print(i)
        return True
    else:
        print(response)
        return False

player_id = get_player_id('kiticat111')
player_count_id = get_player_count_id('kiticat111')
print(player_id, player_count_id)

is_in_game = get_active_game(player_id)
print(is_in_game)

player_leage = get_player_leage(player_id)
print(player_leage)

maches = get_player_matches(player_count_id)
print(maches)
