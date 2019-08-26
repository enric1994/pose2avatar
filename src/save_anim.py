import bpy
from random import randint,random
import src.blenderutils as blenderutils

blenderutils.remove_startup_cube()

# reset_blend()

bpy.ops.group.create(name="CubeXGroup")
 
group = bpy.data.groups['CubeXGroup']

def main():
    start_pos=(0,0,0)
    for i in range(1):
        add_box(i);
   
def add_box(i):
    #generate our object
    bpy.ops.mesh.primitive_cube_add(location = [0,0,0])
    #Select the active object (last added is always the active one
    obj = bpy.context.scene.objects.active
    object_random_location_animation(obj,-3,3)
    object_random_color(obj,i)
    obj.select = True
    bpy.ops.object.group_link(group="CubeXGroup")

#End AddBox

def object_random_location_animation(obj,min,max):
    positions =  []
    for i in range(0,4):
        positions.append([ randint(min,max) for axis in 'xyz'])
        
    frame_num = 0
    for position in positions:
        bpy.context.scene.frame_set(frame_num)
        obj.location = position
        obj.keyframe_insert(data_path="location",index = -1)

        frame_num +=30
#End object_random_location_animation

def  object_random_color(obj,i):
    material = bpy.data.materials.new(name = "RandomMaterial" + str(i))
    obj.data.materials.append(material)
    bpy.context.object.active_material.diffuse_color = (random(),random(), random())
   # bpy.context.object.active_material.name = "Object Material"
    #inputs[0].default_value = (random(),random(), random(), 1)
    #NOTE: Colours may be very interesting or not so great
    #You can select colours from a list of predefined colours
#End  object_random_color

main();

#save images
for i in range(0,100):
        bpy.context.scene.frame_current = i
        bpy.context.scene.render.image_settings.file_format = 'PNG'
        bpy.context.scene.render.filepath = "/pose2char/output/" + str(i)
        bpy.ops.render.render(write_still=True) # render still