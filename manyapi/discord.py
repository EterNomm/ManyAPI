from .DiscordAPI.webhook import webhook
from .DiscordAPI.send_message import send_message

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
			
			
			
	class send_message:
		def __init__(self, token:str, channel_id:int, api_version:int=9):
			self.sm = send_message(token, channel_id, api_version)
		
		def tag_user(self, user_id:int):
			return self.sm.tag_user(user_id)
		
		def send(self, message:str):
			return self.sm.send(message)
