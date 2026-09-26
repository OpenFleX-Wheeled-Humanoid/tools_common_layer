# 工具与通用依赖层

[English](./README.md) | 中文

---

本层放置跨算法复用的工具包、视觉几何基础库和地图格式转换工具。

## 包清单

- `vikit_common`: 视觉几何、相机模型、图像对齐、优化等通用 C++ 工具。
- `vikit_ros`: vikit 与 ROS 2 的桥接工具。
- `vikit_py`: Python 轨迹、数学和 ROS 辅助工具。
- `pcd2pgm`: 将 PCD 点云转换为 Nav2 可使用的 2D occupancy grid。

## 职责边界

本层不承担在线控制、建图主流程或导航主流程。它提供可被其它层复用的库和离线/半离线工具。

## 许可证

本包通过 知识共享 署名-非商业性使用-相同方式共享 4.0 国际许可协议 (CC BY-NC-SA 4.0) 进行许可。

版权所有 (c) 2026 成都长数机器人有限公司 (Chengdu Changshu Robot Co., Ltd.)

详情请参阅 [LICENSE](LICENSE) 文件或访问：http://creativecommons.org/licenses/by-nc-sa/4.0/

## 致谢

本包是 OpenFlex 全身人形机器人平台生态系统的一部分，专为人形机器人领域的研究和工业应用而开发。

---

## 📞 联系我们

### 成都长数机器人有限公司
**Chengdu Changshu Robotics Co., Ltd.**

| 联系方式 | 信息 |
|---------|------|
| 📧 邮箱 | openarmrobot@gmail.com |
| 📱 电话/微信 | +86-17746530375 |
| 🌐 官网 | https://openarmx.com/ |
| 🌐 文档 | http://docs.openarmx.com/ |
| 📍 地址 | 天津市西青区・稻潮机器人体验基地（明日之城）・天津市人形机器人中心 |
| 👤 联系人 | 王先生 |
