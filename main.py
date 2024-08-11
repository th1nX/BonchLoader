from api_functions import modLoaderFunctions

version = modLoaderFunctions(modName='Physics Mod', version='1.21', loader='fabric').searchMods()
print(version)

