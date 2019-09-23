#!/usr/bin/env python3

import bpy
from random import randint,random
import utils as utils
import numpy as np
import math
import os
from tqdm import tqdm

version = '3.0'
minor = '6'
model = 'claudia'
keypoints = 'enric_full'

base_path = '/pose2avatar'

experiment = ('{}.{}.{}.{}'.format(keypoints, model, version, minor))
keypoints_path = os.path.join(base_path, 'data/keypoints', keypoints)
project_path = os.path.join(base_path,'blender/{}.{}.blend'.format(model, version))
bpy.ops.wm.open_mainfile(filepath=project_path)

downsample_ratio = 4
keypoints_resize = 70

pose_bones = {
	 0:  'Nose',
	 1:  'Neck',
	 2:  'RShoulder',
	 3:  'RElbow',
	 4:  'RWrist',
	 5:  'LShoulder',
	 6:  'LElbow',
	 7:  'LWrist',
	 8:  'MidHip',
	 9:  'RHip',
	 10: 'RKnee',
	 11: 'RAnkle',
	 12: 'LHip',
	 13: 'LKnee',
	 14: 'LAnkle',
	#  15: 'REye',
	#  16: 'LEye',
	#  17: 'REar',
	#  18: 'LEar',
	#  19: 'LBigToe',
	#  20: 'LSmallToe',
	#  21: 'LHeel',
	#  22: 'RBigToe',
	#  23: 'RSmallToe',
	#  24: 'RHeel'
}

total_frames = utils.get_total_frames(keypoints_path)

print('''
Starting experiment: {}
Frames: {}
'''.format(experiment, total_frames)
)

def main():

	print('Reading pose from JSON:')
	for frame in tqdm(range(0, int(total_frames / downsample_ratio))):
		frame *=4
		bpy.context.scene.frame_set(frame)
		positions = np.array(utils.get_bones_positions_at_frame(keypoints_path, frame))/keypoints_resize
		for bone in pose_bones:
			bpy.ops.object.mode_set(mode='OBJECT')
			obj = bpy.context.scene.objects[pose_bones[bone]]
			empty = bpy.data.objects[pose_bones[bone]]
			empty.location = positions[bone*3], 0, -positions[bone*3 + 1]
			obj.keyframe_insert(data_path='location',index = -1, frame=frame)

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

	utils.save_project()


if __name__== '__main__':
  main()

