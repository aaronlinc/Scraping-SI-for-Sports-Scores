'''
	Scrapes Sports illustrated url for scores. 
'''


import requests
from bs4 import BeautifulSoup


url = "http://www.si.com/scoreboard?sport=nfl&season=2015&season_status=regular&week=1&conference=all&view-mode-toggle=list"
req = requests.get(url)

soup = BeautifulSoup(req.content, "html.parser")

awayTeam = soup.find_all("div", {"class": "team left"}, {"class": "team-name"})
homeTeam = soup.find_all("div", {"class": "team right"}, {"class": "team-name"})
awayScore = soup.find_all("span", {"class": "away-score"})
homeScore = soup.find_all("span", {"class": "home-score"})

#Returns list of a soupResult
def soupList(soupResult):
	newList = []
	for item in soupResult:
		newList.append(item.text.strip())
	return newList

awayTeamList = soupList(awayTeam)
homeTeamList = soupList(homeTeam)
awayScoreList =  soupList(awayScore)
homeScoreList =  soupList(homeScore)


for away,home,scoreA,scoreH in zip(awayTeamList, homeTeamList, awayScoreList, homeScoreList):
	print away + '  ' + scoreA + '\n' + home + '  ' + scoreH + '\n'

