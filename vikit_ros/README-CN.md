# vikit_ros

[English](./README.md) | 中文

---

vikit（Vision Kit）库的 ROS 2 集成层。提供 ROS 特有的可视化和参数工具。

## 简介

本包将 `vikit_common` 与 ROS 2 桥接，提供：

- **output_helper** - 使用 Sophus SE3 类型发布可视化 Marker（点、线、箭头、相机视锥、六旋翼机体、坐标系）和 TF 变换的函数
- **params_helper** - 模板函数，便捷地获取 ROS 2 参数并带默认值和日志
- **camera_loader** - 从 ROS 参数加载相机参数的头文件

## API 概览

### output_helper (vk::output_helper)

| 函数 | 说明 |
|------|------|
| `publishTfTransform` | 从 Sophus SE3 位姿广播 TF 变换 |
| `publishPointMarker` | 发布点可视化 Marker |
| `publishLineMarker` | 发布线段可视化 Marker |
| `publishArrowMarker` | 发布箭头可视化 Marker |
| `publishCameraMarker` | 发布相机视锥 Marker |
| `publishFrameMarker` | 发布坐标系 Marker |
| `publishHexacopterMarker` | 发布六旋翼机体 Marker |

### params_helper (vk::getParam / vk::hasParam)

封装 `rclcpp` 参数访问的模板函数，具有：
- 自动声明未声明的参数
- 使用默认值时打印警告日志
- 必需参数的重试逻辑

## 编译

```bash
cd ~/openflex_all/openflex_ws
colcon build --packages-select vikit_ros
source install/setup.bash
```

## 在其他包中使用

```cmake
find_package(vikit_ros REQUIRED)
target_link_libraries(your_target vikit_ros::vikit_ros)
```

```cpp
#include <vikit/output_helper.h>
#include <vikit/params_helper.h>
```

## 依赖

- `vikit_common`
- `rclcpp`
- `tf2_ros`
- `tf2_geometry_msgs`
- `visualization_msgs`
- OpenCV
- Eigen3
- Sophus

## 许可证

GPLv3
