import bpy
from random import randint,random
import src.blenderutils as blenderutils
import numpy as np
import math

keypoints_path='/pose2char/data/keypoints/enric_full'
total_frames= blenderutils.get_total_frames(keypoints_path)
bpy.ops.wm.open_mainfile(filepath="/pose2char/blender/claudia.0.2.0.blend")
bpy.ops.object.mode_set(mode="OBJECT")

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





# bpy.context.scene.render.image_settings.file_format = 'PNG'
# bpy.context.scene.render.filepath = "/pose2char/output/test"
# bpy.ops.render.render(write_still=True) # render still


def object_location_animation(obj, bone):
	positions =  []
	for frame in range(0,total_frames):
			position = blenderutils.get_bone_at_frame(keypoints_path, int(bone/3),frame)
			# if 0 in position or position[1] < 20 or position[0] <20:
			# 	# import pdb;pdb.set_trace()
			# 	position=[10000000,10000000,10000000]
			# import pdb;pdb.set_trace()
			positions.append(np.array(position)/100)
		
	frame_num = 0
	for position in positions:
		bpy.context.scene.frame_set(frame_num)
		print(frame_num, bone,position)
		# obj.location = position
		empty = bpy.data.objects[bones[bone]]
		# import pdb;pdb.set_trace()
		empty.location = position
		obj.keyframe_insert(data_path="location",index = -1)

		frame_num +=1
#End object_random_location_animation


# for bone in bones[0,1,2]:
bone=0
bpy.data.objects[bones[bone]].select = True
obj = bpy.context.scene.objects.active
object_location_animation(obj,bone)


#save images
for i in range(0,total_frames):
		bpy.context.scene.frame_current = i
		bpy.context.scene.render.image_settings.file_format = 'PNG'
		bpy.context.scene.render.filepath = "/pose2char/output/" + str(i)
		bpy.ops.render.render(write_still=True) # render still