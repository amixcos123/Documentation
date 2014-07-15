Creating Game Modes
===================

Dota 2 game modes are built using the addon framework used to build the official `Frostivus`_
and `New Bloom`_ events. Addons are essentially overlays on the game
directory - any content in an addon will override the default content. Game code
is written in lua and operates server-side only. Custom assets (models, sounds,
and UI) can be added to the client and used in maps.

As there is currently no officially released toolchain, including map and
particle editors, the `Alien Swarm SDK`_  and pipeline is used to create maps and assets.

.. _Frostivus: http://www.dota2.com/frostivus/day1/
.. _New Bloom: http://www.dota2.com/newbloom/day1/ 
.. _Alien Swarm SDK: https://developer.valvesoftware.com/wiki/Authoring_Tools/SDK_(Alien_Swarm)

Getting Started
-------------

Follow the setup tutorial:

.. toctree::
  :maxdepth: 2

  sdk_setup

Mapping
-------

Currently there is no official map editor, and maps are created in Hammer, an
old Source Engine map editing tool also used for games like Portal 2, Half Life,
etc.

.. toctree::
  :maxdepth: 2

  mapping
