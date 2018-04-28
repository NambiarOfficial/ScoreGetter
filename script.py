import requests
from bs4 import BeautifulSoup
import random
import time
import os
import json

main_url = 'http://www.cricbuzz.com/cricket-match/live-scores'
main_r = requests.get(main_url)
main_soup = BeautifulSoup(main_r.text,'lxml')
url = main_soup.find('a',{'class':'text-hvr-underline text-bold'})
matchId = url['href'][21:26]
url = 'http://www.cricbuzz.com' + url['href']
print(url)
print(matchId)
json_url = 'http://push.cricbuzz.com/match-api/' + matchId + '/commentary.json'

while(True):
	os.system('clear')
	
	json_url = 'http://push.cricbuzz.com/match-api/' + matchId + '/commentary.json'
	json_response = requests.get(json_url)
	json_text = json.loads(json_response.text)
	'''
	with open('jsondata.json','w') as f:
		f.seek(0)
		f.write(str(json_text))
	'''
	print(json_text['status'] + '\n')
	if json_text['score']['batting']['id'] == json_text['team1']['id']:
		print(json_text['team1']['name'])
	else:
		print(json_text['team2']['name'])
	print(json_text['score']['batting']['score'])
	print('CRR : ' + json_text['score']['crr'] + '\n')

	try:
		if json_text['score']['bowling']['id'] == json_text['team1']['id']:
			print(json_text['team1']['name'])
		else:
			print(json_text['team2']['name'])
		print(json_text['score']['bowling']['score'])
		print('RRR : ' + json_text['score']['rrr'] + '\nTarget : ' + json_text['score']['target'] + '\n')
	except:
		pass
	
	batsman1 = json_text['score']['batsman'][0]
	try:
		batsman2 = json_text['score']['batsman'][1]
	except:
		pass
	
	for player in json_text['players']:
		if player['id'] == batsman1['id']:
			print(player['name'] + '\t' + batsman1['r'] + '(' + batsman1['b'] + ')' + '\t4s = ' + batsman1['4s'] + ' 6s = ' + batsman1['6s'])
		try:	
			if player['id'] == batsman2['id']:
				print(player['name'] + '\t' + batsman2['r'] + '(' + batsman2['b'] + ')' + '\t4s = ' + batsman2['4s'] + ' 6s = ' + batsman2['6s'])
		except:
			pass
	
	bowler1 = json_text['score']['bowler'][0]
	try:
		bowler2 = json_text['score']['bowler'][1]
	except:
		pass
	for player in json_text['players']:
		if player['id'] == bowler1['id']:
			print(player['name'] + '\t' + bowler1['o'] + '-' + bowler1['m'] + '-' + bowler1['r'] + '-' + bowler1['w'])
		try:
			if player['id'] == bowler2['id']:
				print(player['name'] + '\t' + bowler2['o'] + '-' + bowler1['m'] + '-' + bowler2['r'] + '-' + bowler2['w'])
		except:
			pass

	print(json_text['score']['prev_overs'])
	
	for i in range(0,2):
		commentary = json_text['comm_lines'][i]
		try:
			if commentary['evt'] == 'other' or commentary['evt'] == 'four' or commentary['evt'] == 'six' or commentary['evt'] == 'wicket':
				print('\n' + str(commentary['o_no']) + ' ' + str(commentary['comm']) + '\n')
		except Exception as e:
			print(e)
			print('\n' + str(commentary['comm']) + '\n')

	time.sleep(5)