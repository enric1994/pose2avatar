!#/usr/bin/python3

import bpy
from random import randint,random
import src.utils as utils
import numpy as np
import math
import os
import tqdm

version = '3.0.0'
model = 'claudia'
keypoints = 'enric_full'

base_path = '/pose2avatar'
os.path.join(,)

experiment = ('{}.{}.{}'.format(keypoints, model, version))
keypoints_path = os.path.join(base_path, 'data/keypoints', keypoints)
project_path = os.path.join(base_path,'blender/{}.blend'.format(experiment))
bpy.ops.wm.open_mainfile(filepath=project_path)

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


def main():

	for frame in tqdm(range(0,total_frames)):
		frame *=4
		bpy.context.scene.frame_set(frame)
		try:
			positions = np.array(utils.get_bones_positions_at_frame(keypoints_path, frame))/70
			for bone in pose_bones:
				bpy.ops.object.mode_set(mode='OBJECT')
				obj = bpy.context.scene.objects[pose_bones[bone]]
				empty = bpy.data.objects[pose_bones[bone]]
				empty.location = positions[bone*3], 0, -positions[bone*3 + 1]
				obj.keyframe_insert(data_path='location',index = -1, frame=frame)

		except:
			pass

	for i in tqdm(range(0,total_frames)):
		bpy.context.scene.frame_current = i
		bpy.context.scene.render.image_settings.file_format = 'PNG'
		os.makedirs(os.join(base_path, 'data', 'output', experiment), exist_ok=True)
		bpy.context.scene.render.filepath = os.join(base_path, 'data', 'output', experiment, str(i).zfill(6))
		utils.render(bpy)

	utils.gen_video(experiment,
		os.join(base_path, 'data', 'output',experiment),
		os.join(base_path, 'data', 'videos','{}.{}'.format(experiment, 'mp4'))
	)
	utils.save_project()


if __name__== '__main__':
  main()

