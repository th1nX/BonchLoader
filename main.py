import modrinth
from api_functions import modLoaderFunctions

version = modLoaderFunctions(modName='3D skin', version='1.21', loader='fabric').searchMods()
print(version)

