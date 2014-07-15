Welcome to D2Moddin Docs
========================

`D2Moddin`_ is a platform to easily play Dota 2 custom game modes. It is also a
base for the Dota 2 modding community, with the `D2Moddin forums`_ and the
`developer documentation`_ you are reading right now.

.. _D2Moddin: http://d2modd.in/
.. _D2Moddin forums: http://d2modd.in/
.. _developer documentation: http://docs.d2modd.in/

.. _addon-docs:

Creating Game Modes
-------------------

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

See the below documentation pages to get started:

.. toctree::
  :maxdepth: 2

  getting_started_addons
  lua_api

.. _d2mp-docs:

Integration with D2Moddin
-------------------------

Integrating your addon with D2Moddin is a relatively painless process.
D2Moddin's server network supports granular versioning using simple version
numbers, and normal Dota 2 addons.

See the below documentation pages to get started:

.. toctree::
  :maxdepth: 2

  getting_started_d2moddin
  d2moddin_info
  deploying_updates

.. _chat-docs:

Chat with Us
------------

If you have any questions during development you can chat on the `forums`_ or in
the irc channel **#dota2mods** on `GameSurge`_.

.. _forums: http://forum.d2modd.in/
.. _GameSurge: https://gamesurge.net/
