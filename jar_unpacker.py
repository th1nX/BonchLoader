import zipfile
import os
import json
from fnmatch import fnmatch

path = r"./test_mods"

mods_names = []
e_mods = []
e_count = 0

for filename in os.listdir(path):
    if fnmatch(filename, '*.jar'):
        mod = zipfile.ZipFile(f'{path}/{filename}', 'r')
        try:
            modinfo = mod.read("fabric.mod.json")
            modinfo_str = modinfo.decode("utf-8")
            modinfo_json = json.loads(modinfo_str)
            modinfo_name = modinfo_json["name"]
            mods_names.append(modinfo_name)
        except:
            try:
                modinfo = mod.read("META-INF/mods.toml")
                modinfo_str = modinfo.decode("utf-8")
                modinfo_split = modinfo_str.split("\n")

                for line in modinfo_split:
                    if line.count("displayName"):
                        name_line = line

                name_line_replace = name_line.replace("displayName=", "").replace('"', "")
                modinfo_name = name_line_replace.replace("displayName", "").replace("=", "").strip()
                mods_names.append(modinfo_name)
            except:
                e_count += 1
                e_mods.append(mod)

print("Mods names:",mods_names)
print("Errors:", e_count)
print("Error mods:", e_mods)
