import bpy
from random import randint,random
import src.blenderutils as blenderutils
import numpy as np
import math
import os

experiment = 'claudia.0.3.0.0'

keypoints_path='/pose2char/data/keypoints/enric_full'
total_frames= blenderutils.get_total_frames(keypoints_path)
bpy.ops.wm.open_mainfile(filepath="/pose2char/blender/claudia.0.2.0.blend")


bones = {
	0:'C_Head_0',
	1:'C_Root_1',
	2:'C_Shoulder_R_2',
	3:'C_Arm_R_3',
	4:'C_Hand_R_4',
	5:'C_Shoulder_L_5',
	6:'C_Arm_L_6',
	7:'C_Hand_L_7',
	9:'C_Hip_R_9',
	10:'C_Knee_R_10',
	11:'C_Ankle_R_11',
	12:'C_Hip_L_12',
	13:'C_Knee_L_13',
	14:'C_Ankle_L_14',
	19:'C_Foot_L_19',
	22:'C_Foot_R_22'
}


def animate_bones(bones):
	# positions =  []
	for frame in range(0,total_frames):
		# print(frame)
		bpy.context.scene.frame_set(frame)
		positions = np.array(blenderutils.get_positions_at_frame(keypoints_path, frame))/100
		for bone in bones:
			bpy.ops.object.mode_set(mode="OBJECT")
			bpy.data.objects[bones[bone]].select = True
			obj = bpy.context.scene.objects.active

			empty = bpy.data.objects[bones[bone]]
			empty.location = positions[bone*3], positions[bone*3 + 1], positions[bone*3 + 2]
			# print(empty.location)
		
		obj.keyframe_insert(data_path="location",index = -1)

		bpy.context.scene.frame_current = frame
		bpy.context.scene.render.image_settings.file_format = 'PNG'
		os.makedirs('/pose2char/output/{}'.format(experiment), exist_ok=True)
		bpy.context.scene.render.filepath = "/pose2char/output/{}/".format(experiment) + str(frame)
		bpy.ops.render.render(write_still=True)
		# import pdb;pdb.set_trace()

				# obj.keyframe_insert(data_path="location",index = -1)

			# blenderutils.get_bone_at_frame(keypoints_path, int(bone/3),frame)
			# positions.append(np.array(position)/100)
		
	# frame_num = 0
	# for position in positions:
	# 	bpy.context.scene.frame_set(frame_num)
	# 	print(frame_num, bone,position)
	# 	# obj.location = position
	# 	empty = bpy.data.objects[bones[bone]]
	# 	# import pdb;pdb.set_trace()
	# 	empty.location = position
	# 	obj.keyframe_insert(data_path="location",index = -1)

	# 	frame_num +=1



# bpy.data.objects[bones[bone]].select = True
# obj = bpy.context.scene.objects.active

animate_bones(bones)
# bpy.ops.wm.save_as_mainfile(filepath='/pose2char/test.blend')

#save images
# for i in range(0,total_frames):
# 		bpy.context.scene.frame_current = i
# 		bpy.context.scene.render.image_settings.file_format = 'PNG'
# 		bpy.context.scene.render.filepath = "/pose2char/output/" + str(i)
# 		bpy.ops.render.render(write_still=True) # render still