from bs4 import BeautifulSoup
import requests
import pprint

class FantasyLeague(object):

	def __init__(self, name, teams):
		self.name = name
		self.contestants = self.getContestants()
		self.teams = teams
		self.getTeamScores()

	def getContestants(self):
		score_dict = {}
		page = requests.get('http://bachelor.realityfantasyleague.com/contestants')
		soup = BeautifulSoup(page.content, 'html.parser')
		for section in soup.find_all("section"):
			for tr in section.findAll("div", "tr"):
				try:
					name = tr.a.get("title")
					score = tr.findAll("div")[4].get_text()
					score_dict[name] = float(score)
				except:
					pass
		return score_dict

	def getTeamScores(self):
		for team in self.teams:
			for contestant in team.contestants:
				team.score += self.contestants[contestant]

	def printTeamScores(self):
		for team in self.teams:
			print("Manager: %s" % team.manager)
			print("Team Name: %s" % team.team_name)
			print("Score: %f" % team.score)
			print("------------------------------------")


class FantasyTeam(object):

	def __init__(self, manager, team_name, contestants):
		self.manager = manager
		self.team_name = team_name
		self.contestants = contestants
		self.score = 0

