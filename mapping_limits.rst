Mapping Limitations
==================

There are limitations and a rulesets for maps in Hammer and their calculation
in Dota 2.


Overlay Limit
############

You cannot decompile and re-compile the dota.bsp map as it has too many
overlays. The overlay limit was raised to 8192 from 512 for Dota 2, but the
compiler toolchain still works under the 512 limit.

Fog of War Calculation
######################

Units can climb to virtually any height within the map, but there are only five
Fog or War heights defined in the Dota 2 engine. They are:

- 0-128: River
- 128-256: Midlane
- 256-384: Highground base
- 384-512: Ward spots
- 512-∞: Edge of the map.

The camera will stay in place above 512 units in the Z axis.
