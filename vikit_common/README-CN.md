# vikit_common

[English](./README.md) | 中文

---

通用计算机视觉工具库（C++）。属于 vikit（Vision Kit）库集合，最初为 SVO（半直接法视觉里程计）开发。

## 简介

本包提供一个 C++ 共享库，包含常用的计算机视觉工具，包括：

- 多种相机模型：针孔、ATAN、等距、全向、多项式
- 数学工具（线性代数辅助函数、变换）
- 视觉工具（特征提取、图像块评分、图像对齐）
- 单应性计算
- 鲁棒代价函数（Tukey、Huber）
- 非线性最小二乘求解器（高斯-牛顿法）
- 性能监控和计时工具
- 环形缓冲区、文件读取器、用户输入线程

## 相机模型

| 模型 | 文件 | 说明 |
|------|------|------|
| 针孔 | `pinhole_camera.cpp` | 标准针孔模型含径向畸变 |
| ATAN | `atan_camera.cpp` | FOV/ATAN 畸变模型 |
| 等距 | `equidistant_camera.cpp` | 等距（鱼眼）模型 |
| 全向 | `omni_camera.cpp` | 全向模型 |
| 多项式 | `polynomial_camera.cpp` | 多项式畸变模型 |

## 编译

```bash
cd ~/openflex_all/openflex_ws
colcon build --packages-select vikit_common
source install/setup.bash
```

## 测试

本包包含测试可执行文件：

```bash
ros2 run vikit_common test_vk_common_camera
ros2 run vikit_common test_vk_common_triangulation
ros2 run vikit_common test_vk_common_patch_score
```

## 依赖

- OpenCV（core、calib3d、features2d、highgui、imgproc）
- Sophus（李群库）
- fmt
- Eigen3

## 在其他包中使用

在 CMakeLists.txt 中链接 `vikit_common`：

```cmake
find_package(vikit_common REQUIRED)
target_link_libraries(your_target vikit_common::vikit_common)
```

## 许可证

GPLv3
