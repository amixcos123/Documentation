Creating an Addon
=================

"Addon" and "Game Mode" are used interchangeably throughout this documentation.

Addon Bootstrapper
##################

.. image:: http://i.imgur.com/7JIgVZL.png

The `D2Moddin addon bootstrapper`_ will ask you some simple questions about your
game mode and build the files for your mode based on your answers. In the future
it will also be able to create additional files for you for NPCs, units,
particles, maps, etc.

First, download the latest version of the bootstrapper. You can use `git clone
--recursive https://github.com/D2Modding/d2tool.git` or just download from `here`_.

.. _here: https://github.com/D2Modding/d2tool
.. _D2Moddin addon bootstrapper: https://github.com/D2Modding/d2tool

Next, run the bootstrapper with Node.JS. `node d2tool.js`. In the future there
will be a compiled exe for this as well.

Answer the questions:

.. image:: http://fat.gfycat.com/InferiorIncompatibleBabirusa.gif

The result will be the following directory structure (in this example, a mode
called "teamfight")::

    ├── addoninfo.txt     - Version & name information.
    ├── info.json         - D2Moddin metadata
    ├── maps              - Maps
    │   ├── teamfight.bsp - Compiled map
    │   └── teamfight.gnv - Compiled gridnav
    ├── materials         - Any engine materials
    │   └── overviews     - Minimaps (named Overviews)
    │       ├── teamfight.vmt
    │       └── teamfight.vtf
    ├── particles         - Custom particles
    │   ├── frostivus_gameplay.pcf
    │   ├── frostivus_herofx.pcf
    │   └── test_particle.pcf
    ├── PhysicsReadme.txt - Readme of the physics system
    ├── resource          - Translations & flash resources
    │   ├── addon_english.txt
    │   ├── flash3
    │   │   └── images
    │   │       ├── items
    │   │       │   └── example_item.png
    │   │       └── spellicons
    │   │           ├── holdout_battle_rage.png
    │   │           ├── holdout_blade_fury.png
    │   │           ├── holdout_culling_blade.png
    │   │           ├── holdout_fiery_soul.png
    │   │           ├── holdout_focusfire.png
    │   │           ├── holdout_friendly_skewer.png
    │   │           ├── holdout_glacier_arrows.png
    │   │           ├── holdout_gods_strength.png
    │   │           ├── holdout_guardian_angel.png
    │   │           ├── holdout_multishot.png
    │   │           ├── holdout_omnislash.png
    │   │           ├── holdout_scourge_ward.png
    │   │           ├── holdout_voodoo.png
    │   │           └── templar_assassin_refraction_holdout.png
    │   └── overviews - Define any custom overviews
    │       └── teamfight.txt
    ├── scripts       - Scripts and other game mode data.
    │   ├── custom_events.txt
    │   ├── game_sounds_custom.txt
    │   ├── maps
    │   │   └── barebones.txt
    │   ├── npc       - KV files for heros, items, units
    │   │   ├── herolist.txt
    │   │   ├── npc_abilities_custom.txt
    │   │   ├── npc_abilities_override.txt
    │   │   ├── npc_heroes_custom.txt
    │   │   ├── npc_items_custom.txt
    │   │   └── npc_units_custom.txt
    │   ├── shops     - Shop data
    │   │   └── barebones_shops.txt
    │   ├── vscripts  - Server-side scripts (can be excluded in the client)
    │   │   ├── addon_game_mode.lua
    │   │   ├── addon_init.lua
    │   │   ├── physics.lua
    │   │   ├── teamfight.lua
    │   │   └── util.lua
    │   └── world_map_custom.txt
    └── sound        - Custom sounds
        └── mini_rosh_firebreath.wav

Addon Initialization
####################

When the server starts up and loads your game mode, it will first execute
`addon_init.lua`. In the bootstrapped addon, `addon_init.lua` will require util,
physics, and finally your game mode lua file at the end of the script.

Next, when the server is ready to create your game mode instance, it will
execute `addon_game_mode.lua`, which, in the bootstrapper, will simply call
`InitGameMode()` on your game mode defined in `gamemode.lua`.

Lua Scope
#########

Any variables defined in the root of the script, without the `local` tag, will
be considered global and accessible anywhere in any lua file loaded into the Dota 2 Lua
VM.

You will generally want to use the `local` tag before variables so you don't
pollute the global scope.

Game Mode Class
###############

Game modes are Lua objects/tables, defined as such::

  TeamFightGameMode = {}
  TeamFightGameMode.szEntityGameMode = "gamemode"
  TeamFightGameMode.szNativeClassName = "dota_base_game_mode"
  TeamFightGameMode.__index = TeamFightGameMode

This definition block occurs in `gamemode.lua`, which will be named according to
your mod's name.

Next, the functions that the mode requires are defined on the game mode
table/object, for example: ::

  function TeamFightGameMode:InitGameMode()
    ...
  end

Registering Hooks
#################

Most of the logic in the lua game mode code revolves around hooking into the
game's standard events.

For example, to perform some logic when a player says something, register the
hook in the game mode init::

  ListenToGameEvent('player_say', Dynamic_Wrap(TeamFightGameMode, 'PlayerSay'), self)

Here, we ask the Lua engine to call `TeamFightGameMode:PlayerSay(keys)` when the
`player_say` game event is fired.

Next, define your implementation::

  function TeamFightGameMode:PlayerSay(keys)
    local ply = self.vUserIds[keys.userid]
    Log(keys.text)
  end

In this case, `keys` is a table/object with relevant data to the say event, such
as the text of the message.

You can view the full API in the API docs sections.

Timers
######

To put off execution of some code into some seconds in the future, you can
register a timer with a unique ID generated by `DoUniqueString`::

  TeamFightGameMode:CreateTimer(DoUniqueString("dothislater"), {
    endTime = GameRules:GetGameTime() + 3,
    useGameTime = true,
    callback = function(teamfight, args)
      Log("Three... seconds... later...")
    end
  })

Here, you pass in the ID of the timer (a unique string starting with `dothislater`, which can be any unique string) and an object with options. In this case, the callback will be called when the game time is greater than `endTime`, which is set to the current game time plus three seconds. Game time or server time can be used, where server time based timers will tick even while the game is paused.


