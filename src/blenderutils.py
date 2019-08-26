import bpy

#Not working
def reset_blend():
    bpy.ops.wm.read_factory_settings()

    for scene in bpy.data.scenes:
        for obj in scene.objects:
            scene.objects.unlink(obj)

    for bpy_data_iter in (
            bpy.data.objects,
            bpy.data.meshes,
            bpy.data.lamps,
            bpy.data.cameras,
            ):
        for id_data in bpy_data_iter:
            bpy_data_iter.remove(id_data)

def remove_startup_cube():
    objs = bpy.data.objects
    objs.remove(objs["Cube"], do_unlink=True)