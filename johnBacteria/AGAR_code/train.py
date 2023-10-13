from ultralytics import YOLO

model = YOLO('yolov8n.pt')

results = model.train(data='C:/Users/precisionag/Documents/bacteria/johnBacteria/AGAR_code/data.yaml',epochs=100,imgsz=512)