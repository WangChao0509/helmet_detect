from ultralytics import YOLO
import cv2
import time


# 数据配置
MODEL_PATH = r'E:\pycharm\Projects\helmet_detect\runs\detect\train\weights\best.pt'    # 模型路径
OUTPUT_PATH = r'E:\pycharm\Projects\helmet_detect\runs\detect\predict\result.mp4'      # 结果保存路径
SOURCE = 0               # 0表示设备默认摄像头，根据实际修改
CONF = 0.45              # 模型最佳F1对应的conf阈值
SAVE_VIDEO = False       # 设置是否保存视频


model = YOLO(MODEL_PATH)

cap = cv2.VideoCapture(SOURCE)

# 获取视频的数据
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))            # 图像宽度
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))          # 图像高度
fps_cam = cap.get(cv2.CAP_PROP_FPS)                       # 帧数

# 防止帧率为0而无法保存视频
if fps_cam == 0:
    fps_cam = 25

# 创建视频保存器
if SAVE_VIDEO:
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')              # 设置输出文件格式
    out = cv2.VideoWriter(OUTPUT_PATH, fourcc, fps_cam, (width, height))        # 创建视频保存器对象

while True:
    ret, frame = cap.read()

    if not ret:
        break

    time_start = time.time()
    results = model(frame, conf=CONF)
    time_end = time.time()

    fps = 1 / (time_end - time_start)

    img = results[0].plot()

    cv2.putText(img, f'FPS: {fps:.1f}', (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow('YOLO RealTime Detection', img)

    if SAVE_VIDEO:
        out.write(img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
if SAVE_VIDEO:
    out.release()
cv2.destroyAllWindows()