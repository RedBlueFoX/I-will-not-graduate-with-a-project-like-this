class Lobby:
	def __init__(self, ID, GID = 0, difficulty):
		self.ID = ID
		self.gameID = GID 
		self.URL = self.generateURL()
		self.difficulty = difficulty
	def generateURL(self):
		pass
	def linkGame(self, GID):

class Game:
	def __init__(self, ID, key):
		self.ID = ID
		self.key = key
		self.data = []

class GameInfo:
	def __init__(self, JSONInput,script):
		self.turns, self.characters, self.objects = self.__parseJSON()
		self.script = self.__parseScript()
	def __parseJSON():
		pass
	def __parseScript():
		pass