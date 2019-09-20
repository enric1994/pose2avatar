!#/usr/bin/python3

import bpy
import json
import os
import io
import sys

def remove_startup_cube():
	objs = bpy.data.objects
	objs.remove(objs['Cube'], do_unlink=True)

def get_total_frames(path):
	file_count = next(os.walk(path))[2]
	return len(file_count)

def get_bones_positions_at_frame(keypoints_path, frame):
	for r, d, f in os.walk(keypoints_path):
		f.sort()
		with open(os.path.join(keypoints_path,f[frame]), 'r') as f:
			pose_dict = json.load(f)
	return pose_dict['people'][0]['pose_keypoints_2d']

def save_project(path='/pose2avatar/test.blend'):
	bpy.ops.wm.save_as_mainfile(filepath=path)

def gen_video(experiment, input_images, output_video):
		os.system('ffmpeg -y -framerate 30 -i {}/%06d.png -c:v libx264 -profile:v high -crf 20 -pix_fmt yuv420p {}'.format(input_images,experiment, output_video))

def render(bpy):
	text_trap = io.StringIO()
	sys.stdout = text_trap
	bpy.ops.render.render(write_still=True)
	sys.stdout = sys.__stdout__