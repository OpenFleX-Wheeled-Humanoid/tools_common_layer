# pcd2pgm

English | [中文](./README-CN.md)

---

PCD point cloud to 2D occupancy grid (PGM) converter ROS 2 node.

## Description

This package provides a ROS 2 node that loads a 3D PCD point cloud file, applies height filtering and radius outlier removal, then projects the remaining points into a 2D occupancy grid map. The resulting map is published as a `nav_msgs/msg/OccupancyGrid` message.

## Key Features

- Loads PCD files using PCL
- Pass-through filter on Z-axis (height) to isolate relevant obstacle layer
- Radius outlier removal to eliminate noise
- Generates occupancy grid at configurable resolution
- Publishes map with transient-local QoS (latched) for downstream consumers
- Supports component-based loading (rclcpp_components)

## Topics

### Published

| Topic | Type | QoS | Description |
|-------|------|-----|-------------|
| `map` (configurable) | `nav_msgs/msg/OccupancyGrid` | Transient-local, reliable | 2D occupancy grid map |

## Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| `pcd_path` | `""` | Absolute path to input PCD file (overrides file_directory/file_name) |
| `file_directory` | `~/openflex_all/openflex_maps/pcd2pgm/` | Directory containing PCD file |
| `file_name` | `RMUC` | PCD file name (without .pcd extension) |
| `thre_z_min` | `0.5` | Minimum Z height for pass-through filter (m) |
| `thre_z_max` | `2.0` | Maximum Z height for pass-through filter (m) |
| `flag_pass_through` | `false` | Invert pass-through filter (remove inside range) |
| `thre_radius` | `0.5` | Radius for outlier removal filter (m) |
| `thres_point_count` | `10` | Minimum neighbors within radius to keep point |
| `map_resolution` | `0.05` | Grid cell size (m/cell) |
| `map_topic_name` | `map` | Published map topic name |

## Launch

```bash
ros2 launch pcd2pgm pcd2pgm.launch.py pcd_path:=/path/to/your/map.pcd
```

Launch arguments:

| Argument | Default | Description |
|----------|---------|-------------|
| `use_sim_time` | `true` | Use simulation time |
| `pcd_path` | `""` | Absolute path to PCD file |

## Build

```bash
cd ~/openflex_all/openflex_ws
colcon build --packages-select pcd2pgm
source install/setup.bash
```

## Configuration

The default config file is at `config/pcd.yaml`. The production config uses:
- `thre_z_min: -0.10`, `thre_z_max: 0.35` (ground-level obstacles)
- `map_resolution: 0.05` (5 cm grid)
- `flag_pass_through: true`

## Dependencies

- `rclcpp`
- `rclcpp_components`
- `nav_msgs`
- `pcl_ros`
- `pcl_conversions`

## License

MIT
