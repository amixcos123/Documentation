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

To use the bootstrapper, you will need `Node.JS`_. Download and install it.

First, download the latest version of the bootstrapper. You can use `git clone
--recursive https://github.com/D2Modding/d2tool.git` or just download from `here`_.

If you downloaded from the link you need to also download `barebones`_ and put
it into the `barebones` directory in d2tool. Otherwise you will see an error
saying `info.json` is missing.

.. _here: https://github.com/D2Modding/d2tool
.. _D2Moddin addon bootstrapper: https://github.com/D2Modding/d2tool
.. _barebones: https://github.com/D2Modding/barebones
.. _Node.JS: http://nodejs.org/

Use the `cd` command to move into the d2tool directory.

Install the dependencies with NPM, run `npm install` in the d2tool directory.

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

