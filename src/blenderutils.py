import bpy
import json
import os

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

def parse_json_3d(path, bone):
	with open(path, 'r') as f:
		distros_dict = json.load(f)

	return [distros_dict['people'][0]['pose_keypoints_2d'][bone],
	distros_dict['people'][0]['pose_keypoints_2d'][bone+1],
	distros_dict['people'][0]['pose_keypoints_2d'][bone+2]
	]


def get_bone_at_frame(path, bone, frame):
	files = []
	for r, d, f in os.walk(path):
		for file in f:
			if '.json' in file:
				files.append(os.path.join(r, file))
	return parse_json_3d(os.path.join(r,f[frame]), bone)

def get_total_frames(path):
	file_count = next(os.walk(path))[2]
	return len(file_count)