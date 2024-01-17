import bpy

i = 0
j = 0

max_i = 10
separation = 1

for obj in bpy.context.selected_objects:
    if i == max_i:
        i = 0
        j += separation
    obj.location.x = i
    obj.location.y = j
    i += separation