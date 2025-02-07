from ultralytics import YOLO

model = YOLO('runs/classify/train3/weights/best.pt')

results = model('images/train/commercial/0a27e6d4-Data0_000120_0_5200.jpg')
results[0].show()
