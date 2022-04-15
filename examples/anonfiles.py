import manyapi

af = manyapi.Anonfiles


### Upload file
upload = af.upload("example.txt")

# get results via json format
print(upload.json())
# get results via text format
print(upload.text())


### Get file info
info = af.info("file id")

# get info via json format
print(info.json())
# get info via text format
print(info.text())
