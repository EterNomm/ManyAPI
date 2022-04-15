import manyapi

rw = manyapi.Randomword(12)

# Print with list format (new line every word)
print(rw.list())

# Print with json format (list)
print(rw.json())
