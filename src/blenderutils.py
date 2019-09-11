import bpy
import json
import os
import math


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
		# import pdb;pdb.set_trace()
		f.sort()
		return parse_json_3d(os.path.join(r,f[frame]), bone)

def get_total_frames(path):
	file_count = next(os.walk(path))[2]
	return len(file_count)

def set_camera(tx, ty, tz, rx, ry, rz):
	scene = bpy.data.scenes["Scene"]

	# Set render resolution
	# scene.render.resolution_x = 480
	# scene.render.resolution_y = 359

	# Set camera fov in degrees
	# scene.camera.data.angle = fov*(pi/180.0)

	# Set camera rotation in euler angles
	scene.camera.rotation_mode = 'XYZ'
	scene.camera.rotation_euler[0] = rx
	scene.camera.rotation_euler[1] = ry
	scene.camera.rotation_euler[2] = rz

	# Set camera translation
	scene.camera.location.x = tx
	scene.camera.location.y = ty
	scene.camera.location.z = tz

def get_positions_at_frame(keypoints_path, frame):


	for r, d, f in os.walk(keypoints_path):
		# import pdb;pdb.set_trace()
		f.sort()

		with open(os.path.join(keypoints_path,f[frame]), 'r') as f:
			pose_dict = json.load(f)
	# import pdb;pdb.set_trace()
	return pose_dict['bodies'][0]['joints26']


def save_project(path='/pose2char/test.blend'):
	bpy.ops.wm.save_as_mainfile(filepath=path)