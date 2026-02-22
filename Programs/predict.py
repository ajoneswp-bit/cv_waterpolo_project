from ultralytics import YOLO

model = YOLO("best.pt")

results = model.predict(source="Bucknell Men's Water Polo Vs. Mercyhurst (10⁄10⁄25) (720p_60fps_H264-128kbit_AAC) - Trim.mp4", save=True, imgsz=720, conf=0.25)