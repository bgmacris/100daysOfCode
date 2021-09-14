import requests
import telebot

API_TELEGRAM = ''
bot = telebot.TeleBot(API_TELEGRAM)

key = ''
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
        return (response.json()['id'], response.json()['summonerLevel'])
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
            return 'No have'
    else:
        return False

def get_data_match(id):
	response = requests.get(f'{MATCH}{id}{API_KEY}')
	data = response.json()
	for i in data['frames'][-1]['events']:
		print(i)

def get_player_matches(id):
    response = requests.get(f'{PLAYER_MATCH}{id}{API_KEY}')
    if response.status_code == 200:
        data = response.json()
        content = {}
        for i in data['matches']:
            content[i['gameId']] = {
				'champ': search_champion(i['champion']),
				'role': i['role'],
				'lane': i['lane']
            }
        return content
    else:
        print(response)
        return False

@bot.message_handler(commands=['p'])
def bot_player(message):
	player_name = message.text.replace('/p ', '')
	try:
		player_data = {
			'id': get_player_id(player_name)[0],
			'count_id': get_player_count_id(player_name),
			'lvl': get_player_id(player_name)[1]
		}
		is_in_game = get_active_game(player_data['id'])
		league = get_player_leage(player_data['id'])
		matches = get_player_matches(player_data['count_id'])
		partidas = [[matches[i]['champ'], matches[i]['role'], matches[i]['lane']] for i in matches]
		print(partidas)
		response = f"""
		{player_name} - lvl: {player_data['lvl']}
		League: {league}
		Matches:
		"""
		for i in partidas:
			response = response + '-'.join(i) + '\n'
		bot.reply_to(message, response)
	except Exception as e:
		print(e)
		bot.reply_to(message, 'User not found')


bot.polling()

