import pyrinth
import zipfile
import os
import json
from fnmatch import fnmatch

class modLoaderFunctions:

    def __init__(self, modName, version, loader, path):
        self.modName = modName
        self.version = version
        self.loader = loader
        self.path = path

    def searchMods(self):
        try:
            mod_search = pyrinth.Project.search(self.modName, limit=1)
            mod_id = mod_search[0].model.project_id
            mod_file = pyrinth.Project.get(mod_id).get_latest_version(loaders=[self.loader], game_versions=[self.version])
            mod_file.download()
            return f'{mod_file} was downloaded'
        except Exception as exc:
            return f'Error: {exc}'

    def jar_unpacker(self):
        mods_names = []
        e_mods = []
        e_count = 0
        for filename in os.listdir(self.path):
            if fnmatch(filename, '*.jar'):
                mod = zipfile.ZipFile(f'{self.path}/{filename}', 'r')
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
                        modinfo_name = modinfo_name.replace("#mandatory", "").strip()
                        mods_names.append(modinfo_name)
                    except:
                        e_count += 1
                        e_mods.append(filename)

        return mods_names