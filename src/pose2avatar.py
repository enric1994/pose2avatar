#!/usr/bin/env python3

import bpy
from random import randint,random
import utils as utils
from bones_ref import *
import numpy as np
import math
import os
from tqdm import tqdm

version = '4.4'
minor = '0'
model = 'claudia'
keypoints = 'enric_hand'
render_video = False
render_hands = True

base_path = '/pose2avatar'

experiment = ('{}.{}.{}.{}'.format(keypoints, model, version, minor))
keypoints_path = os.path.join(base_path, 'data/keypoints', keypoints)
project_path = os.path.join(base_path,'blender/{}.{}.blend'.format(model, version))
bpy.ops.wm.open_mainfile(filepath=project_path)

downsample_ratio = 4
keypoints_resize = 70


total_frames = utils.get_total_frames(keypoints_path)

print('''
Starting experiment: {}
Frames: {}
'''.format(experiment, total_frames)
)

def main():

	print('Preparing pose from JSON:')
	for frame in tqdm(range(0, int(total_frames / downsample_ratio))):
		frame *=4
		bpy.context.scene.frame_set(frame)
		pose_positions = np.array(utils.get_pose_bones_positions_at_frame(keypoints_path, frame))/keypoints_resize
		if render_hands:
			left_hand_positions, right_hand_positions = np.array(utils.get_hand_bones_positions_at_frame(keypoints_path, frame))/keypoints_resize

		for bone in pose_bones:
			bpy.ops.object.mode_set(mode='OBJECT')
			obj = bpy.context.scene.objects[pose_bones[bone]]
			empty = bpy.data.objects[pose_bones[bone]]
			empty.location = pose_positions[bone*3], 0, -pose_positions[bone*3 + 1]
			obj.keyframe_insert(data_path='location',index = -1, frame=frame)
		if render_hands:
			for bone in left_hand_bones:
				bpy.ops.object.mode_set(mode='OBJECT')
				obj = bpy.context.scene.objects[left_hand_bones[bone]]
				empty = bpy.data.objects[left_hand_bones[bone]]
				empty.location = left_hand_positions[bone*3], 0, -left_hand_positions[bone*3 + 1]
				obj.keyframe_insert(data_path='location',index = -1, frame=frame)
			
			for bone in right_hand_bones:
				bpy.ops.object.mode_set(mode='OBJECT')
				obj = bpy.context.scene.objects[right_hand_bones[bone]]
				empty = bpy.data.objects[right_hand_bones[bone]]
				empty.location = right_hand_positions[bone*3], 0, -right_hand_positions[bone*3 + 1]
				obj.keyframe_insert(data_path='location',index = -1, frame=frame)

	if render_video:
		print('Rendering frames...')
		for i in tqdm(range(0,total_frames)):
			bpy.context.scene.frame_current = i
			bpy.context.scene.render.image_settings.file_format = 'PNG'
			os.makedirs(os.path.join(base_path, 'data', 'output', experiment), exist_ok=True)
			bpy.context.scene.render.filepath = os.path.join(base_path, 'data', 'output', experiment, str(i).zfill(6))
			bpy.ops.render.render(write_still=True)

		print('Rendering video...')
		utils.gen_video(
			os.path.join(base_path, 'data', 'output',experiment),
			os.path.join(base_path, 'data', 'videos','{}.{}'.format(experiment, 'mp4'))
		)

	utils.save_project(os.path.join(base_path, 'data', 'projects','{}.blend'.format(experiment)))


if __name__== '__main__':
  main()

