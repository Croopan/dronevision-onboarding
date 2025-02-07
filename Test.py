from ultralytics import YOLO

model = YOLO('../runs/detect/train2/weights/best.pt')

results = model('Test.jpg')
results[0].show()