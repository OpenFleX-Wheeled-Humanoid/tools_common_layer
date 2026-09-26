# vikit_common

English | [中文](./README-CN.md)

---

Common computer vision toolkit library (C++). Part of the vikit (Vision Kit) library collection originally developed for SVO (Semi-direct Visual Odometry).

## Description

This package provides a shared C++ library with common computer vision utilities, including:

- Multiple camera models: pinhole, ATAN, equidistant, omnidirectional, polynomial
- Math utilities (linear algebra helpers, transformations)
- Vision utilities (feature extraction, patch scoring, image alignment)
- Homography computation
- Robust cost functions (Tukey, Huber)
- Non-linear least squares solver (Gauss-Newton)
- Performance monitoring and timing utilities
- Ring buffer, file reader, and user input thread

## Camera Models

| Model | File | Description |
|-------|------|-------------|
| Pinhole | `pinhole_camera.cpp` | Standard pinhole with radial distortion |
| ATAN | `atan_camera.cpp` | FOV/ATAN distortion model |
| Equidistant | `equidistant_camera.cpp` | Equidistant (fisheye) model |
| Omnidirectional | `omni_camera.cpp` | Omnidirectional model |
| Polynomial | `polynomial_camera.cpp` | Polynomial distortion model |

## Build

```bash
cd ~/openflex_all/openflex_ws
colcon build --packages-select vikit_common
source install/setup.bash
```

## Tests

The package includes test executables:

```bash
ros2 run vikit_common test_vk_common_camera
ros2 run vikit_common test_vk_common_triangulation
ros2 run vikit_common test_vk_common_patch_score
```

## Dependencies

- OpenCV (core, calib3d, features2d, highgui, imgproc)
- Sophus (Lie group library)
- fmt
- Eigen3

## Usage in Other Packages

Link against `vikit_common` in your CMakeLists.txt:

```cmake
find_package(vikit_common REQUIRED)
target_link_libraries(your_target vikit_common::vikit_common)
```

## License

GPLv3
