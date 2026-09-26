# vikit_ros

English | [中文](./README-CN.md)

---

ROS 2 integration layer for the vikit (Vision Kit) library. Provides ROS-specific visualization and parameter utilities.

## Description

This package bridges `vikit_common` with ROS 2, providing:

- **output_helper** - Functions to publish visualization markers (points, lines, arrows, camera frustums, hexacopter frames, coordinate frames) and TF transforms using Sophus SE3 types
- **params_helper** - Template functions for convenient ROS 2 parameter retrieval with default values and logging
- **camera_loader** - Header for loading camera parameters from ROS parameters

## API Overview

### output_helper (vk::output_helper)

| Function | Description |
|----------|-------------|
| `publishTfTransform` | Broadcast a TF transform from a Sophus SE3 pose |
| `publishPointMarker` | Publish a point visualization marker |
| `publishLineMarker` | Publish a line visualization marker |
| `publishArrowMarker` | Publish an arrow visualization marker |
| `publishCameraMarker` | Publish a camera frustum marker |
| `publishFrameMarker` | Publish a coordinate frame marker |
| `publishHexacopterMarker` | Publish a hexacopter body marker |

### params_helper (vk::getParam / vk::hasParam)

Template functions that wrap `rclcpp` parameter access with:
- Automatic declaration of undeclared parameters
- Warning logs when using default values
- Retry logic for required parameters

## Build

```bash
cd ~/openflex_all/openflex_ws
colcon build --packages-select vikit_ros
source install/setup.bash
```

## Usage in Other Packages

```cmake
find_package(vikit_ros REQUIRED)
target_link_libraries(your_target vikit_ros::vikit_ros)
```

```cpp
#include <vikit/output_helper.h>
#include <vikit/params_helper.h>
```

## Dependencies

- `vikit_common`
- `rclcpp`
- `tf2_ros`
- `tf2_geometry_msgs`
- `visualization_msgs`
- OpenCV
- Eigen3
- Sophus

## License

GPLv3
