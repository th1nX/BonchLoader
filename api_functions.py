import modrinth

class modLoaderFunctions:

    def __init__(self, modName, version, loader):
        self.modName = modName
        self.version = version
        self.loader = loader

    def searchMods(self):
        project = modrinth.Projects.Search(self.modName).hits[0]
        versions_id = project.versions
        versions = []
        for id in versions_id:
            version = project.getVersion(id)
            primaryFile = version.getPrimaryFile()
            downloadLink = version.getDownload(primaryFile)
            versions.append(downloadLink)
        return versions
