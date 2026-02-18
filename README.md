# 基于yolov8的安全帽检测项目

## 一、项目简介
本项目是基于yolov8m预训练模型进行模型的训练，可自动识别图像中人员是否佩戴安全帽。

项目主要内容：
- 数据集准备与格式转换（YOLO格式，附有voc转yolo格式的脚本：voc2yolo.py）
- 基于yolov8m的模型训练
- 模型性能评估（Recall、Precision、mAP）
- 置信度conf与IoU阈值分析
- 模型推理与结果可视化
- 检测结果保存

适用于：
- 计算机视觉入门
- 目标检测项目实战

## 二、项目结构
- `helmet_detect/` - 项目根目录
  - `README.md` - 项目说明
  - `requirements.txt` - 环境依赖
  - `scripts` - 推理脚本
    - `infer.py` - 推理脚本
    - `voc2yolo.py` - voc转yolo脚本
  - `config/` - 数据配置目录
    - `helmet.yaml` - 数据集配置
  - `weights/` - 模型权重目录
    - `best.pt` - 训练好的模型
    - `best.onnx` - 导出为 ONNX 格式的推理模型（可跨平台部署）
  - `results/` - 推理结果目录
    - `sample_result.jpg` - 示例结果
    - `R_curve.png` - R曲线
    - `P_curve.png` - P曲线
    - `PR_curve.png` - PR曲线
    - `F1_curve.png` - F1曲线
  - `datasets/` - 数据集目录
## 三、运行环境
python >= 3.8
安装依赖：pip install -r requirements.txt
