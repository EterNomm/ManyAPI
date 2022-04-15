# Reference :
#	https://stackoverflow.com/a/48475541
#	https://stackoverflow.com/a/32190892
#	https://developers.google.com/youtube/v3/docs/search/list


import requests
from .YoutubeAPI.converter import convert

class Youtube:
	def __init__(self, url:str, api_key:str):
		self.key = api_key
		self.video_url = url
		# Get video ID
		video_id = url.split("/")[-1]
		self.video_id = video_id
		
	def title(self):
		# Doesn't need API key
		url = self.video_url
		res = requests.get(f"https://noembed.com/embed?url={url}")
		return str(res.json()["title"])
		
	def author(self):
		# Doesn't need API key
		url = self.video_url
		res = requests.get(f"https://noembed.com/embed?url={url}")
		# [Author name, Author channel url]
		return [res.json()["author_name"], res.json()["author_url"]]
		
	def thumbnail(self):
		# Doesn't need API key
		url = self.video_url
		res = requests.get(f"https://noembed.com/embed?url={url}")
		return str(res.json()["thumbnail_url"])
		
	def duration(self):
		key = self.key
		video_id = self.video_id
		res = requests.get(f"https://www.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails%2Cstatistics&id={video_id}&key={key}")
		json = res.json()
		
		for items in json["items"]:
			duration = items["contentDetails"]["duration"]
			
		# [Simple version, Complicated version]
		return [convert(duration, "s"), convert(duration, "m")]
		
	def id(self):
		return str(self.video_id)
			
	def definition(self):
		key = self.key
		video_id = self.video_id
		res = requests.get(f"https://www.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails%2Cstatistics&id={video_id}&key={key}")
		json = res.json()
	
		for items in json["items"]:
			definition = items["contentDetails"]["definition"]
		
		definition = str(definition)
		return str.upper(definition)
			
	
	def likes(self):
		key = self.key
		video_id = self.video_id
		res = requests.get(f"https://www.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails%2Cstatistics&id={video_id}&key={key}")
		json = res.json()
		
		for items in json["items"]:
			likes = items['statistics']['likeCount']
			
		return int(likes)
			
	def views(self):
		key = self.key
		video_id = self.video_id
		res = requests.get(f"https://www.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails%2Cstatistics&id={video_id}&key={key}")
		json = res.json()
		
		for items in json["items"]:
			views = items['statistics']['viewCount']
			
		return int(views)
			
	def comments(self):
		key = self.key
		video_id = self.video_id
		res = requests.get(f"https://www.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails%2Cstatistics&id={video_id}&key={key}")
		json = res.json()
		
		for items in json["items"]:
			comments = items['statistics']['commentCount']
				
		return int(comments)
			
	def upload_date(self):
		key = self.key
		video_id = self.video_id
		res = requests.get(f"https://www.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails%2Cstatistics&id={video_id}&key={key}")
		json = res.json()
		
		for items in json["items"]:
			publish = items['snippet']['publishedAt']
			
		# Idk how to convert ISO 8601 format, so i tricked with this :)
		publish = str(publish)
		publish = publish.replace("T", " ")
		publish = publish.replace("Z", "")
		return publish
		
	def description(self):
		key = self.key
		video_id = self.video_id
		res = requests.get(f"https://www.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails%2Cstatistics&id={video_id}&key={key}")
		json = res.json()
		
		for items in json["items"]:
			description = items["snippet"]["description"]
			
		return description
		
	def search(self, 
		query:str, 
		max_results:int=10,
		type:str="video",
		sort_by:str="relevance",
		video_definition:str="any",
		safesearch_type:str="moderate"
		):
			
		if sort_by == "view":
			sort_by = "viewCount"
		elif sort_by == "video":
			sort_by = "viewCount"
		
		key = self.key
		query = query.replace(" ", "%20")
		
		results = []
		req = requests.get(f"https://youtube.googleapis.com/youtube/v3/search?part=snippet&safeSearch={safesearch_type}&order={sort_by}&q=v{query}&type={type}&videoDefinition={video_definition}&maxResults={max_results}&key={key}")
		parse = req.json()
		
		for items in parse["items"]:
			title = items["snippet"]["title"]
			video_id = items["id"]["videoId"]
			video_link = "https://youtube.com/watch?v="+video_id
			
			res = {title: video_link}
			results.append(res)
			
		return results
