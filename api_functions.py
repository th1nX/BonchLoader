import pyrinth

class modLoaderFunctions:

    def __init__(self, modName, version, loader):
        self.modName = modName
        self.version = version
        self.loader = loader

    def searchMods(self):
        try:
            mod_search = pyrinth.Project.search(self.modName, limit=1)
            mod_id = mod_search[0].model.project_id
            mod_download = pyrinth.Project.get(mod_id).get_latest_version(loaders=[self.loader], game_versions=[self.version])
            return mod_download
        except Exception as exc:
            return exc
