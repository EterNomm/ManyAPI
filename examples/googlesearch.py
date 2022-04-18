import manyapi

google = manyapi.Googlesearch()

for title, url in google.search("EterNomm github"):
	print(title)
	print(url)
	print("-------")
