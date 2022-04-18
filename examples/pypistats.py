import manyapi

pypi = manyapi.PypiStats("manyapi")

print(pypi.downloads())
print(pypi.operating_system()) # alias : os
print(pypi.overall())
