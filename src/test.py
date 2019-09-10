import bpy
from random import randint,random
import src.blenderutils as blenderutils
import numpy as np
import math

bpy.ops.wm.open_mainfile(filepath="/pose2char/blender/trump_rigged0.2.1.blend")



empty = bpy.data.objects['Empty']
bpy.ops.object.mode_set(mode="OBJECT")
print(empty.location)
empty.location = (5,5,0)


bpy.context.scene.render.image_settings.file_format = 'PNG'
bpy.context.scene.render.filepath = "/pose2char/output/test"
bpy.ops.render.render(write_still=True) # render still