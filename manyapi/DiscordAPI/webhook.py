import requests
from datetime import datetime
from ..exceptions import *

class webhook:	
	def __init__(self, url):
		self.data = None
		self.url = url
		
		
	def message(self, username:str, message:str, avatar_url:str):
		self.data = {
			"username":username,
			"content": message,
			"avatar_url": avatar_url
		}
		
	
	def timestamp(self):
		return str(datetime.utcnow())
	
	def fields(self,
		name:str,
		value:str,
		inline=False
		):
		
		payload = {
			"name": name,
			"value": value,
			"inline": inline
			}
			
		return payload
		
	def embed(self,
		title:str, 
		description:str,
		url:str,
		color:int,
		timestamp,
		image:str,
		author_name:str,
		author_url:str,
		author_icon:str,
		fields,
		thumbnail_url:str,
		footer_text:str,
		footer_icon:str
		):

		self.data["embeds"] = [
			{
			"title": title,
			"description": description,
			"url": url,
			"color": color,
			"timestamp": timestamp,
			
			"author": {
				"name": author_name,
				"url": author_url,
				"icon_url": author_icon
				},
			
			"fields": fields,
				
			"thumbnail": {
				"url": thumbnail_url
				},
			
			"image": {
				"url": image
				},
				
			"footer": {
				"text": footer_text,
				"icon_url": footer_icon
				}
			}
		]
		
		
	def post(self):
		response = requests.post(self.url, json=self.data)
		try:
			response.raise_for_status()
		except requests.RequestException as error:
			raise RequestsErrors(error)
		else:
			return "Payload successfully delivered."
