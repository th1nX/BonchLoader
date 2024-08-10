import modrinth

project = modrinth.Projects.Search('3D skin').hits[0]
versions_id = project.versions
print(versions_id)
for id in versions_id:
    version = project.getVersion(id)
    primaryFile = version.getPrimaryFile()
    print(version.getDownload(primaryFile))
