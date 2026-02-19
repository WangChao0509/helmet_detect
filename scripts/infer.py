from ultralytics import YOLO
import cv2
import time

# 配置
MODEL_PATH = r'E:\pycharm\Projects\helmet_detect\runs\detect\train\weights\best.pt'
OUTPUT_PATH = r'E:\pycharm\Projects\helmet_detect\runs\detect\predict\result.jpg'
SOURCE = r'E:\pycharm\Projects\helmet_detect\infer_data\helmet3.jpg'
CONF = 0.45
SAVE = True

# 加载模型
model = YOLO(MODEL_PATH)

# 图片推理
def infer_img(SOURCE):
    results = model(SOURCE, conf=CONF)
    img = results[0].plot()

    if SAVE:
        cv2.imwrite(OUTPUT_PATH, img)

    cv2.imshow('result', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 视频/摄像头推理
def infer_video(SOURCE):
    cap = cv2.VideoCapture(SOURCE)

    # 检查视频是否能打开
    if not cap.isOpened():
        print('视频无法打开！')
        return

    # 逐帧推理
    while True:
        ret, frame = cap.read()

        if not ret:
            print('视频读取完毕！')
            break

        start = time.time()
        results = model(frame, conf=CONF)
        end = time.time()

        fps = 1 / (end - start)

        img = results[0].plot()
        cv2.putText(img, f'fps: {fps:.1f}', (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        img = cv2.resize(img, (960, 540), interpolation=cv2.INTER_AREA)
        cv2.imshow('YOLOv8 Detection', img)

        if cv2.waitKey(10) & 0xFF ==27:
            break

    cap.release()
    cv2.destroyAllWindows()

# 主函数
if __name__ == '__main__':

    # 图片推理
    if isinstance(SOURCE, str) and SOURCE.endswith(('.jpg', '.jpeg', 'png')):
        infer_img(SOURCE)
    else:
        infer_video(SOURCE)