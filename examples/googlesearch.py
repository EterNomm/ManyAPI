import manyapi

google = manyapi.Googlesearch()

for title, url in google.search("EterNomm github", 20):
	print(title)
	print(url)
	print("-------")
