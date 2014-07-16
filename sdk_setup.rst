SDK Setup Tutorial
==================

This page is based on the `Dota 2 wiki`_.

.. _Dota 2 wiki: https://developer.valvesoftware.com/wiki/Dota_2_Maps

Install the Alien Swarm SDK. In Steam, go to the Library section, and under
Tools, download the Alien Swarm SDK. You can also click `this shortcut link`_.

.. _this shortcut link: steam://install/640

Extract Dota's Files
####################

Dota 2's content files are distributed in compressed VPK form. You can extract
them using `GCFScape`_ to later modify them in your game mode. You may need to
use the x86 version, which works fine on 64 bit systems.

.. _GCFScape: http://nemesis.thewavelength.net/index.php?p=26

The primary Dota 2 package is the `pak01_dir.vpk` file under the base dota
game directory. Open the pak in GCFScape, right click the root element, and
extract the files to `Alien Swarm\\swarm\\addons` so they may be used in the
Alien Swarm editors.

Rename the directory you have just created in the Alien Swarm addons to
`Dota2Extract`.

Misc. Files
###########

Copy the `bin` and `platform` directories into the `Dota2Extract` directory.

Finally, download `dota2fgd`_ (by RoyAwesome on GitHub) and `UpVersion.exe`_ (by
ModDota) to the bin directory within `Dota2Extract`.

.. _dota2fgd: https://github.com/RoyAwesome/dota2fgd
.. _UpVersion.exe: http://moddota.com/builds/UpVersion/UpVersion.exe

Alien Swarm Search Paths
########################

Replace the contents of `Alien Swarm\\swarm\\gameinfo.txt` with::

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
            "Game" "|gameinfo_path|addons\\Dota2Extract"
         }
     }

Configuring Hammer
##################

In Steam, open the Alien Swarm SDK. In the menu that pops up (the tool
launcher), select "Hammer World Editor". Select Tools->Options, and add the 
Start the Alien Swarm SDK, select Hammer World Editor and let it open up.
Now go to "Tools" -> "Options" and add the "dota2.fgd" from `Alien Swarm\\Swarm\\addons\\Dota2Extract\\bin\\dota2.fgd`.

Next, increase the render distance so that the entire map will be visible at any
given time. Under "3D Views" increase the Model Render Distance and Detail
Render Distance.


Creating a Test Map
###################

Under File, create a new map. Save it as `test.vmf`. Next, select
File->Run Map and press "Expert" in the bottom left corner:

.. image:: http://i.imgur.com/oHosYCQ.png

Click "Edit" and create a new config for Dota 2. We will define the build process as a series of commands.

The BSP Command
***************

Click "New", then "Cmds" and "BSP Program". Add `-alldetail -game $gamedir $path\\$file`.  

UpVersion
*********

Upversion is a tool that will convert the BSP into a format suitable for Dota 2.

Click "new" then "cmds". Select "Executable" and find "UpVersion.exe" in
`Alien Swarm\\swarm\\addons\\Dota2Extract\\bin`. If it's not there, return t
the Misc Files step and download it.

Add the parameters `$path\\$file.bsp $path\\$file.$ext $path\\$file.pbm`.

Copy Map
********

Finally, to use the map in Dota 2 we will copy the compiled .bsp to the Dota 2
maps directory.

Click "new" then "cmds". Select "Executable" and specify:
`CgWindows\\System32\\xcopy.exe`, the built in Windows copy tool. Add the
parameters: `$path\\$file.bsp "C:\\Program Files (x86)\\Steam\\SteamApps\\common\\dota 2
beta\\dota\\maps" /y`. Make sure the path is the correct path to your Dota 2 maps
directory.`

Next Steps
##########

You now have the Alien Swarm SDK set up properly to start working on Dota 2 game
modes. You can follow the mapping tutorial in the next section. 
