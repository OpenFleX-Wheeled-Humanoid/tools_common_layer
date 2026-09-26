# pcd2pgm

[English](./README.md) | 中文

---

PCD 点云转 2D 占据栅格地图（PGM）ROS 2 节点。

## 简介

本包提供一个 ROS 2 节点，加载 3D PCD 点云文件，进行高度滤波和半径离群点去除，然后将剩余点投影为 2D 占据栅格地图，以 `nav_msgs/msg/OccupancyGrid` 消息发布。

## 主要功能

- 使用 PCL 加载 PCD 文件
- Z 轴（高度）直通滤波，提取相关障碍物层
- 半径离群点去除，消除噪声
- 生成可配置分辨率的占据栅格
- 以 transient-local QoS（锁存）发布地图，便于下游消费
- 支持组件化加载（rclcpp_components）

## 话题

### 发布

| 话题 | 类型 | QoS | 说明 |
|------|------|-----|------|
| `map`（可配置） | `nav_msgs/msg/OccupancyGrid` | Transient-local, reliable | 2D 占据栅格地图 |

## 参数

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `pcd_path` | `""` | PCD 文件绝对路径（覆盖 file_directory/file_name） |
| `file_directory` | `~/openflex_all/openflex_maps/pcd2pgm/` | PCD 文件所在目录 |
| `file_name` | `RMUC` | PCD 文件名（不含 .pcd 后缀） |
| `thre_z_min` | `0.5` | 直通滤波最小 Z 高度（m） |
| `thre_z_max` | `2.0` | 直通滤波最大 Z 高度（m） |
| `flag_pass_through` | `false` | 反转直通滤波（移除范围内点） |
| `thre_radius` | `0.5` | 离群点去除搜索半径（m） |
| `thres_point_count` | `10` | 半径内最少邻居数 |
| `map_resolution` | `0.05` | 栅格单元尺寸（m/格） |
| `map_topic_name` | `map` | 发布的地图话题名 |

## 启动

```bash
ros2 launch pcd2pgm pcd2pgm.launch.py pcd_path:=/path/to/your/map.pcd
```

启动参数：

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `use_sim_time` | `true` | 使用仿真时间 |
| `pcd_path` | `""` | PCD 文件绝对路径 |

## 编译

```bash
cd ~/openflex_all/openflex_ws
colcon build --packages-select pcd2pgm
source install/setup.bash
```

## 配置

默认配置文件位于 `config/pcd.yaml`。生产配置使用：
- `thre_z_min: -0.10`、`thre_z_max: 0.35`（地面层障碍物）
- `map_resolution: 0.05`（5 cm 栅格）
- `flag_pass_through: true`

## 依赖

- `rclcpp`
- `rclcpp_components`
- `nav_msgs`
- `pcl_ros`
- `pcl_conversions`

## 许可证

MIT
