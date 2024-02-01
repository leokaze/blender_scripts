import bpy

objects = bpy.context.selected_objects

for obj in objects:
    # Unlink the object from others collections
    for c in bpy.data.collections:
        if obj.name in c.objects:
            c.objects.unlink(obj)

    collection = bpy.data.collections.new(obj.name)
    bpy.context.scene.collection.children.link(collection)
    collection.objects.link(obj)


# This script will create a new collection for each selected object, 
# and move the object to that collection.
# Then it will unlink the default collection from the scene.
