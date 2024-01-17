import bpy
import math

i = 0
j = 0

amount_objects = len(bpy.context.selected_objects)
max_i = math.sqrt(amount_objects)

separation = 1

for obj in bpy.context.selected_objects:
    if i >= max_i:
        i = 0
        j += separation
    obj.location.x = i
    obj.location.y = j
    i += separation
