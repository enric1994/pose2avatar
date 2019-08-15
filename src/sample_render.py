import bpy
from random import randint

# Create cube
# bpy.ops.mesh.primitive_cube_add()


# Render it
bpy.data.scenes['Scene'].render.filepath = "render.png"
bpy.ops.render.render( write_still=True ) 