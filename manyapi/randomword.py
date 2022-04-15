import requests

class Randomword:
	def __init__(self, number:int):
		if isinstance(number, str) == True:
			raise TypeError('"number" argument cannot string, must integer.')
		base_url = f"https://random-word-api.herokuapp.com/word?number={number}"
		self.response = requests.get(base_url)
		
	def list(self):
		json = self.response.json()
		return '\n'.join(str(x) for x in json)
		
	def json(self):
		return self.response.json()
