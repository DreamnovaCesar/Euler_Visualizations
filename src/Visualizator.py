import bpy
import numpy as np
import mathutils

# Clear all existing objects in the Blender scene to start fresh
bpy.ops.object.select_all(action="SELECT")
bpy.ops.object.delete()

# Specify the file path for the text file containing the 3D voxel data
filepath = r"F:\ConcatenationAlign\TXT\1.- Cheese_102_102_102_Matrix.txt"

# Open and read the data from the text file
with open(filepath, "r") as file:
    # Load the data into a numpy array, assuming the data is comma-separated
    data = np.loadtxt(file, delimiter=',')

# Reshape the data into a 3D numpy array with dimensions (522, 522, 522)
data = data.reshape(102 + 2, 102 + 2, 102 + 2)

# Rotate the 3D array 90 degrees around a specific axis
data = np.rot90(data, k=1, axes=(1, 2))  # Rotate 90 degrees in the (1, 2) plane

# Define the size of each cube (voxel) in the 3D model
cube_size = 1.0  # You can adjust this value as needed

# Pad the data array with a border of zeros to handle edge cases at the boundaries
padded_data = np.pad(data, 1, mode='constant')

# Calculate the sum of neighboring voxel values for each voxel
# Using numpy's roll function to shift the array along each axis in both directions
neighbor_sum = (
    np.roll(padded_data, 1, axis=0) + np.roll(padded_data, -1, axis=0)
    + np.roll(padded_data, 1, axis=1) + np.roll(padded_data, -1, axis=1)
    + np.roll(padded_data, 1, axis=2) + np.roll(padded_data, -1, axis=2)
)

# Identify perimeter voxels: voxels that are solid (value of 1) but have fewer than six solid neighbors
perimeter_voxels = (data == 1) & (neighbor_sum[1:-1, 1:-1, 1:-1] < 6)

# Initialize lists to store the vertices, edges, and faces of the cubes
vertices = []
edges = []
faces = []

# Iterate through each voxel in the 3D perimeter_voxels array
for i in range(perimeter_voxels.shape[0]):
    for j in range(perimeter_voxels.shape[1]):
        for k in range(perimeter_voxels.shape[2]):
            if perimeter_voxels[i, j, k]:
                # Define the vertices of the cube for this perimeter voxel
                cube_vertices = [
                    (i, j, k), (i + cube_size, j, k), (i + cube_size, j + cube_size, k), (i, j + cube_size, k),
                    (i, j, k + cube_size), (i + cube_size, j, k + cube_size), (i + cube_size, j + cube_size, k + cube_size), (i, j + cube_size, k + cube_size)
                ]
                # Add the cube's vertices to the vertices list
                vertices.extend(cube_vertices)
                
                # Calculate the starting index of the vertices for the current cube
                start_index = len(vertices) - 8
                
                # Define the edges connecting the vertices of the cube
                cube_edges = [
                    (start_index, start_index + 1), (start_index + 1, start_index + 2), (start_index + 2, start_index + 3),
                    (start_index + 3, start_index), (start_index + 4, start_index + 5), (start_index + 5, start_index + 6),
                    (start_index + 6, start_index + 7), (start_index + 7, start_index + 4), (start_index, start_index + 4),
                    (start_index + 1, start_index + 5), (start_index + 2, start_index + 6), (start_index + 3, start_index + 7)
                ]
                # Add the edges to the edges list
                edges.extend(cube_edges)
                
                # Define the faces of the cube using the vertices
                faces.extend([
                    # Bottom face
                    (start_index, start_index + 1, start_index + 2, start_index + 3),
                    # Top face
                    (start_index + 4, start_index + 5, start_index + 6, start_index + 7),
                    # Front face
                    (start_index, start_index + 1, start_index + 5, start_index + 4),
                    # Right face
                    (start_index + 1, start_index + 2, start_index + 6, start_index + 5),
                    # Back face
                    (start_index + 2, start_index + 3, start_index + 7, start_index + 6),
                    # Left face
                    (start_index + 3, start_index, start_index + 4, start_index + 7)
                ])

# Create a new mesh using the collected vertices, edges, and faces
mesh = bpy.data.meshes.new("PerimeterCubesMesh")
mesh.from_pydata(vertices, edges, faces)

# Create a new object from the mesh
object = bpy.data.objects.new("PerimeterCubes", mesh)

# Link the object to the current Blender scene
bpy.context.collection.objects.link(object)

# Update the scene to reflect the new object
bpy.context.view_layer.update()

# Create a new camera
camera_data = bpy.data.cameras.new("Camera")
camera_object = bpy.data.objects.new("Camera", camera_data)

# Link the camera object to the current Blender scene
bpy.context.collection.objects.link(camera_object)

# Set the camera position
camera_object.location = (200, -100, 200)  # Set a position that gives a clear view of the object
camera_object.rotation_mode = 'XYZ'

# Make the camera point towards the object's center
object_center = object.location
camera_direction = object_center - camera_object.location
camera_object.rotation_euler = camera_direction.to_track_quat('-Z', 'Y').to_euler()

# Set the camera as the active camera
bpy.context.scene.camera = camera_object

# Update the scene
bpy.context.view_layer.update()