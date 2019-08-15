import bpy
from random import randint

# Delete default cube
bpy.ops.object.delete() 

# Model path
model_path = "/home/enric/Documents/repos/3Dhackathon/models/sample2/lowpolymountains.3ds"

# Import model
bpy.ops.import_scene.autodesk_3ds(filepath=model_path)

# Set camera
# bpy.ops.view3d.camera_to_view_selected()


bpy.ops.view3d.camera_to_view_selected()


# scene = bpy.data.scenes["Scene"]
# scene.camera.rotation_mode = 'XYZ'
# rx=0
# ry=0
# rz=0.5
# pi=3.14
# scene.camera.rotation_euler[0] = rx*(pi/180.0)
# scene.camera.rotation_euler[1] = ry*(pi/180.0)
# scene.camera.rotation_euler[2] = rz*(pi/180.0)

ob = bpy.context.object

# for i in range(0,40):
#     ob.rotation_euler = (3*i/40,3*i/40,3*i/40)

    # Render it
bpy.data.scenes['Scene'].render.filepath = "output/model_render3.png"
bpy.ops.render.render( write_still=True ) 
    