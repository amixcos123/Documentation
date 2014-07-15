SDK Setup Tutorial
==================

Install the Alien Swarm SDK. In Steam, go to the Library section, and under
Tools, download the Alien Swarm SDK. You can also click `this shortcut link`_.

.. _this shortcut link: steam://install/640

Extract Dota's Files
####################

Dota 2's content files are distributed in compressed VPK form. You can extract
them using `GCFScape`_ to later modify them in your game mode. You may need to
use the x86 version, which works fine on 64 bit systems.

.. _GCFScape: http://nemesis.thewavelength.net/index.php?p=26

The primary Dota 2 package is the :code:`pak01_dir.vpk` file under the base dota
game directory. Open the pak in GCFScape, right click the root element, and
extract the files to :code:`Alien Swarm\swarm\addons` so they may be used in the
Alien Swarm editors.

Rename the directory you have just created in the Alien Swarm addons to
`Dota2Extract`.

Misc. Files
###########

Copy the :code:`bin` and :code:`platform` directories into the
:code:`Dota2Extract` directory.

Finally, download `dota2fgd`_ (by RoyAwesome on GitHub) and `UpVersion.exe`_ (by
ModDota) to the bin directory within `Dota2Extract`.

.. _dota2fgd: https://github.com/RoyAwesome/dota2fgd
.. _UpVersion.exe: http://moddota.com/builds/UpVersion/UpVersion.exe

Alien Swarm Search Paths
########################

Replace the contents of :code:`Alien Swarm\swarm\gameinfo.txt` with::
    "game"         "Alien Swarm"
    "title"        ""
    "type"         "multiplayer_only"
    "GameData"     "swarm.fgd"
    "InstancePath" "tilegen/instances/"
    
    "SupportsDX8"  0
    
    "FileSystem"
    {
        "SteamAppId" "630"
        "ToolsAppId"  "211"

        "SearchPaths"
        {
            "Game"  "|gameinfo_path|."
            "Game" "swarm_base"
            "Game"  "platform"
            "Game" "|gameinfo_path|addons\Dota2Extract"
         }
     }
