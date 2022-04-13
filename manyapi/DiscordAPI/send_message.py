import requests

class send_message:
	def __init__(self, token:str, channel_id:int, api_version:int):
		self.token = token
		self.url = f"https://discord.com/api/v{api_version}/channels/{channel_id}/messages"
		
	def tag_user(self, user_id:int):
		return f"<@{user_id}>"
		
	def send(self, message:str):
		payload = {
			"content": message
		}
		
		headers = {
			"authorization": self.token
		}
		
		response = requests.post(self.url, data=payload, headers=headers)
		try:
			response.raise_for_status()
		except requests.exceptions.HTTPError as error:
			raise RuntimeError(error)
		else:
			return "Payload successfully delivered."
