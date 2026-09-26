# vikit_py

[English](./README.md) | 中文

---

Python 视觉工具包。属于 vikit（Vision Kit）库集合。

## 简介

本包提供用于计算机视觉和机器人研究的 Python 工具模块，包括：

- **transformations.py** - 3D 变换工具（旋转矩阵、四元数、欧拉角）。基于 Christoph Gohlke 的 transformations 库。
- **math_utils.py** - 线性代数辅助函数（齐次投影/反投影、反对称矩阵）
- **align_trajectory.py** - Sim(3) 轨迹对齐，使用 Umeyama 方法（两点集之间变换参数的最小二乘估计）
- **depthmap_utils.py** - 深度图处理工具
- **ros_node.py** - ROS 节点辅助工具
- **cpu_info.py** - CPU 信息获取

## 安装

本包为 `ament_python` 包：

```bash
cd ~/openflex_all/openflex_ws
colcon build --packages-select vikit_py
source install/setup.bash
```

## 使用方式

```python
from vikit_py.transformations import quaternion_from_matrix, euler_from_matrix
from vikit_py.math_utils import skew, project, unproject
from vikit_py.align_trajectory import align_sim3
```

## 依赖

- `rclpy`
- NumPy（各模块广泛使用）

## 许可证

BSD
