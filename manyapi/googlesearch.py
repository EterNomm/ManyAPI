import requests
from bs4 import BeautifulSoup
from .exceptions import *


class Googlesearch:
	"""
	A google search API wrapper (doesn't need API key)
	----
	Classmethod:
	- search
	"""
	@classmethod
	def search(self, query:str, results_total:int=15):
		"""
		A method to search google
		----
		Parameters:
		- query: `str` | Search query
		- results_total: `int` | how much results to search
		
		yield title and url
		"""
		query = query.replace(" ", "+")
		results_total+=2 # If "results_total" is 15 then the final results is only 13
		url = f"https://www.google.com/search?q={query}&num={results_total}"
		
		try:
			req = requests.get(url)
		except requests.RequestException as error:
			raise RequestsErrors(error)
		bs4 = BeautifulSoup(req.content, "html.parser")
		bs4_results = bs4.find_all("a")
		

		for link in bs4_results:
			link_href = link.get("href")
			if "url?q=" in link_href and not "webcache" in link_href:
				find_h3 = link.find_all('h3')
				if len(find_h3) > 0:
					url = link.get('href').split("?q=")[1].split("&sa=U")[0]
					title = find_h3[0].getText()
					
					yield title, url
