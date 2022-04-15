import manyapi

yt = manyapi.Youtube("youtube video link", "Youtube API v3 key")

# Get video details
title = yt.title()
author = yt.author()
thumbnail = yt.thumbnail()
duration = yt.duration()
video_id = yt.id()
video_definition = yt.definition()
likes = yt.likes()
views = yt.views()
comments_count = yt.comments()
upload_date = yt.upload_date()
description = yt.description()

print("just input all the variables above, I'm lazy :3")

# Search video
search = yt.search(
	query="Valorant",
	max_results=50,
	type="video",
	sort_by="relevance",
	video_definition="any",
	safesearch_type="moderate"
	)
	
print(search)
