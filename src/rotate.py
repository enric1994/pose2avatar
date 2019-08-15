import bpy
from random import randint

# Create cube
# bpy.ops.mesh.primitive_cube_add()

ob = bpy.context.object

for i in [1,2,3,4]:
    ob.rotation_euler = (i,i,0)

    # Render it
    bpy.data.scenes['Scene'].render.filepath = "render{}.png".format(i)
    bpy.ops.render.render( write_still=True ) 
