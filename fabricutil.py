from metautil import *
import jsonobject

variants = {
    "fabric": {
        "name": "Fabric Loader",
        "description": "Fabric Loader is a tool to load Fabric-compatible mods in game environments.",
        "url": "https://fabricmc.net",
        "authors": ["Fabric Developers"],
        "meta": "https://meta.fabricmc.net",
        "maven": "https://maven.fabricmc.net",
        "loader_uid": "net.fabricmc.fabric-loader",
        "intermediary_uid": "net.fabricmc.intermediary",
        "exclude": [],
    },
    "legacy-fabric": {
        "name": "Fabric Loader 1.8.9",
        "description": "Fabric Loader for 1.8.9 and below.",
        "url": "https://legacyfabric.net",
        "authors": ["Legacy Fabric Developers"],
        "meta": "https://meta.legacyfabric.net",
        "maven": "https://maven.legacyfabric.net",
        "loader_uid": "net.legacyfabric.fabric-loader-189",
        "intermediary_uid": "net.legacyfabric.intermediary",
        "exclude": ["fabric-loader"],
    },
    "minecraft-cursed-legacy": {
        "name": "Cursed Fabric Loader",
        "description": "Fabric Loader for Beta 1.7.3.",
        "url": "https://minecraft-cursed-legacy.github.io",
        "authors": ["Cursed Minecraft Legacy Developers"],
        "meta": "http://localhost:5555",
        "maven": "https://storage.googleapis.com/devan-maven",
        "loader_uid": "io.github.minecraft-cursed-legacy.cursed-fabric-loader",
        "intermediary_uid": "io.github.minecraft-cursed-legacy.intermediary",
        "exclude": ["fabric-loader"],
        "skip_update": True,
        "intermediary_override": {
            "b1.7.3": {
                "name": "io.github.minecraft-cursed-legacy:intermediary:b1.7.3",
                "MMC-absoluteUrl": "https://gist.github.com/leo60228/e7de61c54cc35a86a84a4c864291c237/raw/b1.7.3.jar",
            },
            "1.2.5": {
                "name": "io.github.minecraft-cursed-legacy:intermediary:1.2.5",
                "MMC-absoluteUrl": "https://gist.github.com/leo60228/e7de61c54cc35a86a84a4c864291c237/raw/1.2.5.jar",
            },
        },
        "extra_loader_options": {
            "minecraftArguments": "--username ${auth_player_name} --session ${auth_session} --gameDir ${game_directory} --assetsDir ${game_assets}",
            "addTraits": [
                "noapplet"
            ],
        },
    },
}

# barebones semver-like parser
def isFabricVerStable(ver):
    s = ver.split("+")
    return ("-" not in s[0])

class FabricInstallerArguments(JsonObject):
    client = ListProperty(StringProperty)
    common = ListProperty(StringProperty)
    server = ListProperty(StringProperty)

class FabricInstallerLaunchwrapper(JsonObject):
    tweakers = ObjectProperty(FabricInstallerArguments, required=True)

class FabricInstallerLibraries(JsonObject):
    client = ListProperty(MultiMCLibrary)
    common = ListProperty(MultiMCLibrary)
    server = ListProperty(MultiMCLibrary)

class FabricInstallerDataV1(JsonObject):
    version = IntegerProperty(required=True)
    libraries = ObjectProperty(FabricInstallerLibraries, required=True)
    mainClass = jsonobject.DefaultProperty()
    arguments = ObjectProperty(FabricInstallerArguments, required=False)
    launchwrapper = ObjectProperty(FabricInstallerLaunchwrapper, required=False)

class FabricJarInfo(JsonObject):
    releaseTime = ISOTimestampProperty()
    size = IntegerProperty()
    sha256 = StringProperty()
    sha1 = StringProperty()
