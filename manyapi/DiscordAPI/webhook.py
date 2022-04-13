import requests

class webhook:	
	def __init__(self, url):
		self.data = None
		self.url = url
		
		
	def message(self, username:str, message:str, avatar_url:str=None):
		self.data = {
			"username":username,
			"content": message,
			"avatar_url": avatar_url
		}
		
	
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
		url:str=None,
		color:int=None,
		image:str=None,
		author_name:str=None,
		author_url:str=None,
		author_icon:str=None,
		fields=None,
		thumbnail_url:str=None,
		footer_text:str=None,
		footer_icon:str=None
		):

		self.data["embeds"] = [
			{
			"title": title,
			"description": description,
			"url": url,
			"color": color,
			
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
		except requests.exceptions.HTTPError as error:
			raise RuntimeError(error)
		else:
			return "Payload successfully delivered."
