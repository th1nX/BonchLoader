import pyrinth


def get_mod(name, version, loader):
    mod_search = pyrinth.Project.search(name, limit=1)
    mod_id = mod_search[0].model.project_id
    mod_download = pyrinth.Project.get(mod_id).get_latest_version(loaders=[loader], game_versions=[version])
    print(mod_download)

get_mod("Mod menu", "1.19.4", "fabric" )