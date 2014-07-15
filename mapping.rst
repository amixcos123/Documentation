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
====================

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
=================

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

=== Making a Minimap ===

Minimaps require a few files in a few places.

You will need [http://nemesis.thewavelength.net/index.php?c=238#p238 VTFEdit]
to convert an image into a .vtf file

First is the overview screenshot.  This can be created in a number of ways
(Valve paints theirs, other people have taken screenshots).  Once a suitable
image is found, Open VTFEdit, select Import, find your image, and save it as
MAPNAME.vtf.  Also, go to 'Tools' and click 'Create VMT'.  In the Options tab,
for shader, select UnlitGeneric and check the boxes 'Translucent' and 'Vertex
Alpha'.  Save it as MAPNAME.vmt.

Put both of these files in a folder named materials/overviews in your dota (or
addon) directory.

Next, create a new textfile named MAPNAME.txt.  This is a [[KeyValues | Key
Value]] file denoting where the bounds of the minimap lie.  The structure is as
follows:

<syntaxhighlight >

MAPNAME // Change this key to your map's name
{
material "overviews/MAPNAME" //path to the VTF and VMT above.  Note that the
file extension is missing here
  
        //Coordinates to the upper left corner of your map
                pos_y 2560
                  pos_x -2560


                    scale 5.000 //Minimap scale.  Smaller the map, smaller the
                    number. 
                      rotate 0 //Minimap rotation.  This should always be 0.  
                        zoom 1.0000 //Minimap zoom.  This should always be 1
                        unless your texture is larger than the playable bounds
                        of your map.  

}

</syntaxhighlight>

Put this file in your resource/overviews folder in your dota (or addon)
directory



=== Additional Notes ===

The func_brush named "structure_seal" should be nodraw (no skybox required).
Select a hero by typing "jointeam goodguys/badguys"

== Special Mapping Notes ==

There are limitations and a rulesets for maps in Hammer and their calculation
in Dota 2.

=== Overlays ===

If you try to decompile and recompile the main map, dota.bsp, you'll notice
that it ends up not working in VBSP, because there are too many overlays. The
limit on overlays was raised from 512 to 8192 for Dota 2, and we're working on
a workaround for this issue.

=== Fog of War Calculation ===

While the limitations in height are nearly non-existant, but there are only
five heights considered as different heights in the Fog of War calculation.
Starting from you 0-point in z-axis, they're increasing in 128 units, so the
max-height is 512 Units. Everything above will be considered as one height.

Calculation of different height is simple: '''x∈n;128*(x-1);1>=x>=5'''
On this way we can always refer on 5 different heights. In example the heights
for Dota.bsp are 1 - river; 2 - Midlane height; 3 - highground base; 4 -
wardspots (like defensive radiant wardspot); 5 - the edge of the map.

If you're **higher** then 512 units the heightmap will continue to increase,
but the player-camera still sits on the same place. So gets a unit closer to
the camera and the total Field of View gets smaller. If you're getting below 0
on the z-axis, the camera will follow that height as it should be.

== Maps ==

[https://github.com/Z-Machine/Flatgrass Flatgrass] by Z-Machine

[https://github.com/ash47/Frota Frota] by Ash47 - An addon that comes with
Arena of the Dark Rift, Deadlock, Frostivus, Riverofsouls, and Runehill.

[https://github.com/Z-Machine/RiverOfSouls River of Souls] by Z-Machine
