# 基于yolov8的安全帽检测项目

## 一、项目简介
本项目是基于yolov8m预训练模型进行模型的训练，可自动识别图像中人员是否佩戴安全帽（分为helmet和nohelmet两类），支持图片、视频和实时监测。

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
    - `infer.py` - 推理脚本（支持图片和视频）
    - `voc2yolo.py` - voc转yolo脚本
    - `demo_realtime.py` - 推理脚本（支持实时监测）
  - `config/` - 数据配置目录
    - `helmet.yaml` - 数据集配置
  - `weights/` - 模型权重目录
    - `best.pt` - 训练好的模型
    - `best.onnx` - 导出为 ONNX 格式的推理模型（可跨平台部署）
  - `results/` - 推理结果目录
    - `sample_result.jpg` - 示例结果
    - `sample_result.mp4` - 示例结果 
    - `R_curve.png` - R曲线
    - `P_curve.png` - P曲线
    - `PR_curve.png` - PR曲线
    - `F1_curve.png` - F1曲线
  - `datasets/` - 数据集目录
## 三、结果分析
- 训练集train为6000，val验证集为1000。
- 在验证集上conf为0.453时最佳F1为0.9，两类的Precision和Recall都是0.90+，其中helmet的Precision和Recall都高于nohelmet，mAP@0.5为0.935，mAP@0.5:0.95为0.63。
- 在终端上，best.pt单张图片的平均推理速度为25ms（模型未预热）,使用推理脚本进行实时推测时，平均推理速度为5ms（模型预热后）；导出为.onnx后单张图片的平均推理速度为5.4ms。
## 四、运行环境与代码说明
- 本项目python版本为3.9.25，best.pt大小为21.4MB。
- 安装项目依赖：pip install -r requirements.txt
- 模型训练：yolo detect train data=config/helmet.yaml model=yolov8m.pt imgsz=640 batch=16 epochs=120 device=0
- 模型验证：yolo detect val model=weights/best.pt data=data/helmet.yaml
- 模型推理：yolo detect predict model=weights/best.pt source='文件路径' ；或者使用脚本：python infer.py/demo_realtime.py
- 模型导出：yolo export model=weights/best.pt format=onnx（.onnx模型体积较大，未上传至weights）
## 五、模型改进方向
在实时检测中，离检测摄像头过近时（约1米内），模型有时会将较密的头发误判为安全帽；但在实际正常的检测距离内，检测结果比较稳定。可能原因是模型学习的数据中缺乏相关数据集，样本需要进一步丰富；也可能是近距离情况下头发局部区域在视觉上与安全帽边缘存在一定相似性。改进方向如下：增加未佩戴安全帽的人头负样本，尤其是近距离、多角度样本；调整conf置信度阈值以减少误检；扩充数据集规模并增加训练轮次（epochs），提高模型泛化能力。
