import bpy
import struct
import io
import mathutils
import numpy as np
import json 

bl_info = {
    "name": "VRC dolly Json",
    "author": "Neotame4",
    "version": (1, 0),
    "blender": (3, 0, 0),
    "location": "File > Import",
    "description": "Import VRC Camera Dolly Json files",
    "category": "Import-Export",
}

class ReadJsonOperator(bpy.types.Operator):
    bl_idname = "import_path.read_json"
    bl_label = "Import Json File"
    bl_options = {'REGISTER', 'UNDO'}

    filepath: bpy.props.StringProperty(subtype="FILE_PATH")

    def execute(self, context):
        if not self.filepath:
            self.report({'ERROR'}, "No file selected")
            return {'CANCELLED'}

        read_json(self.filepath)
        self.report({'ERROR'}, 'welcome, to jurassic jank,*jurassic park.mid*')
        return {'FINISHED'}

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

def read_json(filepath):
    with open(filepath, "r") as file:
        camera_data = json.load(file)

  # made just for setting up a scene
  # no use because premade scene go brrrrrrrr
      #  coll0 = bpy.data.collections.new("0")
      #  coll1 = bpy.data.collections.new("1")
      #  coll2 = bpy.data.collections.new("2")
      #  coll3 = bpy.data.collections.new("3")
      #  coll4 = bpy.data.collections.new("4")
      #  bpy.context.scene.collection.children.link(coll0)
      #  bpy.context.scene.collection.children.link(coll1)
      #  bpy.context.scene.collection.children.link(coll2)
      #  bpy.context.scene.collection.children.link(coll3)
      #  bpy.context.scene.collection.children.link(coll4)
       # print(data)
    for frame in camera_data:
        index = frame.get("Index")
        pathindex = frame.get("PathIndex")
       # print("PathIndex", pathindex)
        focaldistance = frame.get("FocalDistance")
        aperture = frame.get("Aperture")
        hue = frame.get("Hue")
        saturation = frame.get("Saturation")
        lightness = frame.get("Lightness")
        lookatmexoffset = frame.get("LookAtMeXOffset")
        lookatmeyoffset = frame.get("LookAtMeYOffset")
        zoom = frame.get("Zoom")
        speed = frame.get("Speed")
        duration = frame.get("Duration")
        position = frame.get("Position", {})
        rotation = frame.get("Rotation", {})
       # print("collection", collection)
    # BRING ON THE JANKY STUFF
        if pathindex == 0:
            collection = bpy.data.collections["0"]
        elif pathindex == 1:
            collection = bpy.data.collections["1"]
        elif pathindex == 2:
            collection = bpy.data.collections["2"]
        elif pathindex == 3:
            collection = bpy.data.collections["3"]
        elif pathindex == 4:
            collection = bpy.data.collections["4"]
        o = bpy.data.objects.new(str(index), None)
       # bpy.context.scene.collection.objects.link(o)
        if pathindex == 0:
            bpy.data.collections["0"].objects.link(o)
        elif pathindex == 1:
            bpy.data.collections["1"].objects.link(o)
        elif pathindex == 2:
            bpy.data.collections["2"].objects.link(o)
        elif pathindex == 3:
            bpy.data.collections["3"].objects.link(o)
        elif pathindex == 4:
            bpy.data.collections["4"].objects.link(o)

        o.empty_display_size = 1
        o.empty_display_type = 'PLAIN_AXES'

       # print("position", position.get("X"))
        o.location[0] = position.get("X")
        o.location[1] = position.get("Z")
        o.location[2] = position.get("Y")

        o.rotation_euler[0] = rotation.get("X")
        o.rotation_euler[1] = rotation.get("Y")
        o.rotation_euler[2] = rotation.get("Z")
        print(f"Frame {index}: Position {position}, Rotation {rotation}")



def menu_func(self, context):
    self.layout.operator(ReadJsonOperator.bl_idname)

def register():
    bpy.utils.register_class(ReadJsonOperator)
    bpy.types.TOPBAR_MT_file_import.append(menu_func)


def unregister():
    bpy.utils.unregister_class(ReadJsonOperator)
    bpy.types.TOPBAR_MT_file_import.remove(menu_func)

if __name__ == "__main__":
    register()
