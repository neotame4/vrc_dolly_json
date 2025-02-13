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
    "description": "Import Json files",
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
        return {'FINISHED'}

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

def read_json(filepath):
    with open(filepath, 'rb') as file:
        data = json.load(file) 
       # for i in data['emp_details']:
        print(data)



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
