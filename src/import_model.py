import bpy
from random import randint

# Delete default cube
bpy.ops.object.delete() 

# Model path
model_path = "/home/enric/Documents/repos/3Dhackathon/models/sample_model/house.stl"

# Import model
bpy.ops.import_mesh.stl(filepath=model_path)

# Set camera
bpy.ops.view3d.camera_to_view_selected()

ob = bpy.context.object

for i in range(0,40):
    ob.rotation_euler = (3*i/40,3*i/40,3*i/40)

    # Render it
    bpy.data.scenes['Scene'].render.filepath = "output/model_render{}.png".format(i)
    bpy.ops.render.render( write_still=True ) 
    