# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Copyright 2020 Enric Moreu. All Rights Reserved.

import bpy
import argparse
from random import randint,random
import utils as utils
from bones_ref import *
import numpy as np
import math
import os
from tqdm import tqdm


keypoints_path = '/pose2avatar/data/keypoints'
project_path = '/pose2avatar/data/blender/example.blend'
frames_output = '/pose2avatar/data/frames'
video_output = '/pose2avatar/data/video_output'
video_name = 'example.mp4'
output_project_path = '/pose2avatar/projects/output_example.blend'

bpy.ops.wm.open_mainfile(filepath=project_path)

downsample_ratio = 4
keypoints_resize = 70

total_frames = utils.get_total_frames(keypoints_path)
print('Total frames: {}'.format(str(total_frames)))

def main():

	print('Preparing pose from JSON:')
	for frame in tqdm(range(0, int(total_frames / downsample_ratio))):
		frame *=4
		bpy.context.scene.frame_set(frame)
		pose_positions = np.array(utils.get_pose_bones_positions_at_frame(keypoints_path, frame))/keypoints_resize

		for bone in pose_bones:
			bpy.ops.object.mode_set(mode='OBJECT')
			obj = bpy.context.scene.objects[pose_bones[bone]]
			empty = bpy.data.objects[pose_bones[bone]]
			empty.location = pose_positions[bone*3], empty.location.y, -pose_positions[bone*3 + 1]
			obj.keyframe_insert(data_path='location',index = -1, frame=frame)

	if render_video:
		print('Rendering frames...')
		for i in tqdm(range(0,total_frames)):
			bpy.context.scene.frame_current = i
			bpy.context.scene.render.image_settings.file_format = 'PNG'
			bpy.context.scene.render.filepath = os.path.join(frames_output, str(i).zfill(6))
			bpy.ops.render.render(write_still=True)

		print('Rendering video...')
		utils.gen_video(
			video_output,
			os.path.join(video_output,video_name)
		)

	utils.save_project(output_project_path)


if __name__== '__main__':
  main()
