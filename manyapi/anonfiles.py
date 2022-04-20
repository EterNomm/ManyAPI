import requests
from .exceptions import *

class Anonfiles:
	class upload:
		def __init__(self, file:str):
			payload = {
				"file": (file, open(file, "rb"))
			}

			try:
				self.res = requests.post("https://api.anonfiles.com/upload", payload=payload)
			except requests.RequestException as error:
				raise RequestsErrors(error)
		
		def json(self):
			return self.res.json()
			
		def text(self):
			json = self.res.json()
			
			status = json['status']
			short_url = json['data']['file']['url']['short']
			full_url = json['data']['file']['url']['full']
			size = json['data']['file']['metadata']['size']['readable']
			filename = json['data']['file']['metadata']['name']
			file_id = json['data']['file']['metadata']['id']
			
			return f"Status : {status}\nShort url : {short_url}\nFull url : {full_url}\nSize : {size}\nFilename : {filename}\nFile ID : {file_id}"
			
	
	class info:
		def __init__(self, file_id:str):
			try:
				res = requests.get(f"https://api.anonfiles.com/v2/file/{file_id}/info")
			except requests.RequestException as error:
				raise RequestsErrors(error)
			self.res_json = res.json()
			
		def json(self):
			return self.res_json
			
		def text(self):
			status = self.res_json['status']
			short_url = self.res_json['data']['file']['url']['short']
			full_url = self.res_json['data']['file']['url']['full']
			size = self.res_json['data']['file']['metadata']['size']['readable']
			filename = self.res_json['data']['file']['metadata']['name']
			file_id = self.res_json['data']['file']['metadata']['id']
			
			return f"Status : {status}\nShort url : {short_url}\nFull url : {full_url}\nSize : {size}\nFilename : {filename}\nFile ID : {file_id}"
