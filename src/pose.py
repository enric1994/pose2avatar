import bpy

def print(data):
    for window in bpy.context.window_manager.windows:
        screen = window.screen
        for area in screen.areas:
            if area.type == 'CONSOLE':
                override = {'window': window, 'screen': screen, 'area': area}
                bpy.ops.console.scrollback_append(override, text=str(data), type="OUTPUT")      

print('Script started')

##Go to pose mode and select armature
for ob in bpy.context.selected_objects:
    ob.select = False

armature = bpy.data.objects['Armature.001']
armature.select = True
bpy.context.scene.objects.active = armature
bpy.ops.object.mode_set(mode='POSE')


# armature.data.edit_bones

for bone in armature.pose.bones:
    print(bone.head)
