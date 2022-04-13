from .DiscordApi.webhook import webhook

class Discord:
	class webhook:
		def __init__(self, url:str):
			self.wh = webhook(url)
			
		def message(self,
			username:str,
			message:str,
			avatar_url:str=None
			):
				
			self.wh.message(username, message, avatar_url)
			
		def fields(self,
			name:str,
			value:str,
			inline=False
			):
				return self.wh.fields(name, value, inline)
				
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
			
			self.wh.embed(
			title,
			description,
			url,
			color,
			image,
			author_name,
			author_url,
			author_icon,
			fields,
			thumbnail_url,
			footer_text,
			footer_icon
			)
			
		def post(self):
			return self.wh.post()
