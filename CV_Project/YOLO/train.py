from ultralytics import YOLO

model = YOLO("yolo11s.pt")

model.train(data = "config.yaml", imgsz = 1280, batch = 2, epochs = 10, workers = 0, device = 0)