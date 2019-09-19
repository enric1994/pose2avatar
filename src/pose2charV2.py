import bpy
from random import randint,random
import src.blenderutils as blenderutils
import numpy as np
import math
import os

experiment = 'claudia.2.4.2.0'

keypoints_path='/pose2char/data/keypoints/enric_full'
total_frames= blenderutils.get_total_frames(keypoints_path)
bpy.ops.wm.open_mainfile(filepath="/pose2char/blender/claudia.2.4.2.blend")


bones = {
     0:  "Nose",
     1:  "Neck",
     2:  "RShoulder",
     3:  "RElbow",
     4:  "RWrist",
     5:  "LShoulder",
     6:  "LElbow",
     7:  "LWrist",
     8:  "MidHip",
     9:  "RHip",
     10: "RKnee",
     11: "RAnkle",
     12: "LHip",
     13: "LKnee",
     14: "LAnkle",
    #  15: "REye",
    #  16: "LEye",
    #  17: "REar",
    #  18: "LEar",
	#Don't use foot bones
    #  19: "LBigToe",
    #  20: "LSmallToe",
    #  21: "LHeel",
    #  22: "RBigToe",
    #  23: "RSmallToe",
    #  24: "RHeel"
}


def animate_bones(bones):
	# positions =  []
	for frame in range(0,20): #total_frames
		# print(frame)
		bpy.context.scene.frame_set(frame)
		try:
			positions = np.array(blenderutils.get_positions_at_frame(keypoints_path, frame))/70
			for bone in bones:
				bpy.ops.object.mode_set(mode="OBJECT")
				bpy.data.objects[bones[bone]].select = True
				obj = bpy.context.scene.objects.active

				empty = bpy.data.objects[bones[bone]]
				empty.location = positions[bone*3], 0, -positions[bone*3 + 1]
				# print(empty.location)
			
			obj.keyframe_insert(data_path="location",index = -1)

			bpy.context.scene.frame_current = frame
			bpy.context.scene.render.image_settings.file_format = 'PNG'
			os.makedirs('/pose2char/output/{}'.format(experiment), exist_ok=True)
			bpy.context.scene.render.filepath = "/pose2char/output/{}/".format(experiment) + str(frame)
			bpy.ops.render.render(write_still=True)
		except:
			pass
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

# blenderutils.save_project()

# bpy.ops.wm.save_as_mainfile(filepath='/pose2char/test.blend')

#save images
# for i in range(0,total_frames):
# 		bpy.context.scene.frame_current = i
# 		bpy.context.scene.render.image_settings.file_format = 'PNG'
# 		bpy.context.scene.render.filepath = "/pose2char/output/" + str(i)
# 		bpy.ops.render.render(write_still=True) # render still