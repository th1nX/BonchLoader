import zipfile
import os
import json

path = "./test_mods"

for filename in os.listdir(path):
    mod = zipfile.ZipFile(f'{path}/{filename}', 'r')
    modinfo = mod.read("fabric.mod.json")
    modinfo_str = modinfo.decode("utf-8")
    modinfo_json = json.loads(modinfo_str)
    print(modinfo_json["name"])
    print(modinfo_json["depends"])
