Mapping with Hammer
===================

Maps are created with Hammer for Dota 2, an old Source Engine map creation tool
used for Portal 2, Half Life, and other valve games.

Make sure you've completed the getting started tutorial first.

General Mapping Notes
#####################

- Maps are a much larger scale in Dota 2 than they are in other Source games. Units are around 48 units wide, towers are 128x128x320 units tall.  
- If an entity is outside the bounds of the map, it crashes the game with no error.
- AlienSwarm converts all brushwork into func_detail, so you need to seal the
  map with a func_brush named structure_seal.  The brush should be textured nodraw.  
- Required entities include: info_player_start_goodguys, info_player_start_badguys, ent_dota_game_events, env_global_light.
- Models require a shader that is not provided in Hammer.  In your extracted gamedata, open every .vmt file and replace "GlobalLitSimple" with "VertexLitGeneric".  A tool such as Notepad++ can do this quickly.

Building the NavGrid
####################

Units in Dota 2 do not navigate based on the structure of the map, rather, they
move on a 2D grid known as the navmesh. Every square in the navgrid has two
states: pathable, and not pathable. If a square is not pathable, the unit will
not walk there and cannot blink/force staff to that location. It is possible to
cross unpathable areas with blinks or force movements.

Install the GNVTool
*******************

The GNVtool (by Penguinwizzard) converts netpbm formats to the binary GridNav format. It can do two
way conversion between PBM files, which are editable in photo editing software
to manually touch up the grid.

- `Download GNVTool`_
- `List of NetPBM Software`_
- `Paint.Net PBM Plugin`_

.. _Download GNVTool: http://moddota.com/builds/GNVTool/GNVTool.exe
.. _List of NetPBM Software: http://netpbm.sourceforge.net/doc/directory.html
.. _Paint.Net PBM Plugin: http://forums.getpaint.net/index.php?/topic/17202-pnm-file-type-plugin/


Netpbms are 1 bit bitmaps. The bitmap size must be the world size / 64. The bitmap must have dimensions divisible by 8 or it will be sheared.

Usage: code::`GNVtool.exe tognv source.pbm target.gnv offsetx offsety`.

Offset x/Offset y are always negative and 1/2 the dimensions of the bitmap.  

You can view your navmesh in game with code::`dota_gridnav_show 1`.

Creating a NETPBM
#################

First, open up a Hammer map.

.. image:: http://i.imgur.com/7EjENbW.png

The first two arguments you need are the dimensions of the map. This will be a
rectangle aligned with the Hammer grid.

In this image it is 4096x4096:

.. image:: http://i.imgur.com/GLNsy4p.png

Next, you need the offset of the map from the origin. Get the top left point of
the map (in this image, -2048, 2048).

.. image:: http://i.imgur.com/MWtKAqZ.png

Using these values, you can create the netpbm. Divide the dimensions by 64 to get the
size of the pbm file you need to make (here 64x64). Use the offset (with the
y-axis-component negated, because gnv files are upside-down) to calculate the
last 2 arguments to GNVTool, and you should get a gnv file that works for your
map!

.. image:: http://i.imgur.com/l2HGTsJ.png
