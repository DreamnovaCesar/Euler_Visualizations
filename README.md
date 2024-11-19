![Python](https://img.shields.io/badge/python-v3.10+-blue.svg)
[![Build Status](https://travis-ci.org/anfederico/clairvoyant.svg?branch=master)](https://travis-ci.org/anfederico/clairvoyant)
![Contributions welcome](https://img.shields.io/badge/contributions-welcome-orange.svg)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

<a name="readme-top"></a>

# 3D Voxel Data Visualization in Blender

This project provides a Python script for visualizing 3D voxel data in Blender. The code parses a text file containing voxel data, constructs a 3D mesh of perimeter cubes, and sets up a camera for optimal visualization.

## Project Overview

The script performs the following tasks:
1. **Scene Initialization**: Clears all existing objects in the Blender scene for a fresh start.
2. **Data Import and Reshaping**: Reads and reshapes the voxel data from a specified text file.
3. **Perimeter Voxel Detection**: Identifies perimeter voxels (solid voxels with fewer than six solid neighbors).
4. **Mesh Construction**: Constructs cubes for each perimeter voxel and adds them to the Blender scene.
5. **Camera Setup**: Configures a camera to provide a clear view of the 3D model.

## How the Script Works

1. **Data Reading and Reshaping**:
   - The script reads voxel data from a `.txt` file and loads it into a numpy array.
   - The data is reshaped to the appropriate dimensions and rotated for proper orientation.

2. **Perimeter Voxel Detection**:
   - Each voxel is checked to determine if it is a perimeter voxel using a neighbor summation technique.
   - Voxels with fewer than six solid neighbors are used to create perimeter cubes.

3. **Mesh Creation**:
   - The script defines vertices, edges, and faces for each perimeter voxel and creates a 3D mesh.
   - The mesh is added to the Blender scene as an object.

4. **Camera Configuration**:
   - A new camera is created and positioned to view the 3D model clearly.
   - The camera is oriented to point toward the center of the object.

## How to Use

1. **Prerequisites**:
   - Blender must be installed on your system.
   - Ensure that the `bpy` and `numpy` libraries are available in your Python environment.

2. **Setting the File Path**:
   - Update the `filepath` variable in the script to the path of your voxel data file.

3. **Running the Script in Blender**:
   - Open Blender.
   - Go to the "Scripting" workspace and paste the script into the text editor.
   - Click "Run Script" to generate the 3D visualization.

## Customization

- **Cube Size**: Modify the `cube_size` variable to change the size of the voxels in the 3D model.
- **Camera Position**: Adjust `camera_object.location` to change the camera's viewpoint.
- **Voxel Data**: Ensure your text file is formatted correctly (comma-separated values) for successful data loading.

## Example Use Case

This script is ideal for visualizing 3D structures derived from voxel data, such as medical imaging, scientific simulations, or voxel-based modeling. By focusing on perimeter voxels, it efficiently highlights the object's shape and boundaries.

## Notes

- Make sure to adjust the script as needed based on your specific voxel data format and desired visualization parameters.
- This project is a simple and efficient way to render voxel-based 3D models directly in Blender.

---

Feel free to reach out if you encounter any issues or have suggestions for improvement!
## Co-authors

- Dr. Hermilo Sanchez Cruz
- Ms. Elisa

### Built With

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)&nbsp;

### Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

### 🤝🏻 &nbsp;Connect with Me

<p align="center">
<a href="https://www.linkedin.com/in/cesar-eduardo-mu%C3%B1oz-chavez-a00674186/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
<a href="https://twitter.com/CesarEd43166481"><img src="https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white"/></a>