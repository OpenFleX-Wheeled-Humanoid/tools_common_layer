# vikit_py

English | [中文](./README-CN.md)

---

Python vision toolkit utilities. Part of the vikit (Vision Kit) library collection.

## Description

This package provides Python utility modules for computer vision and robotics research, including:

- **transformations.py** - 3D transformation utilities (rotation matrices, quaternions, Euler angles). Based on Christoph Gohlke's transformations library.
- **math_utils.py** - Linear algebra helpers (homogeneous projection/unprojection, skew-symmetric matrix)
- **align_trajectory.py** - Sim(3) trajectory alignment using the Umeyama method (least-squares estimation of transformation parameters between two point patterns)
- **depthmap_utils.py** - Depth map processing utilities
- **ros_node.py** - ROS node helper utilities
- **cpu_info.py** - CPU information retrieval

## Installation

This is an `ament_python` package:

```bash
cd ~/openflex_all/openflex_ws
colcon build --packages-select vikit_py
source install/setup.bash
```

## Usage

```python
from vikit_py.transformations import quaternion_from_matrix, euler_from_matrix
from vikit_py.math_utils import skew, project, unproject
from vikit_py.align_trajectory import align_sim3
```

## Dependencies

- `rclpy`
- NumPy (used extensively in all modules)

## License

BSD
