import bpy
import math

# initializing variables
x = 0
y = 0

amount_objects = len(bpy.context.selected_objects)
max_x = math.sqrt(amount_objects)

# amount of separation between objects. 
# CHANGE THIS
separation = 1

for obj in bpy.context.selected_objects:
    if x >= max_x * separation:
        x = 0
        y += separation
    obj.location.x = x
    obj.location.y = y
    x += separation
