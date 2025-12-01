CPU: 
epoch = 10: 
![alt text](C:\Users\tugsu\Pictures\Screenshots\CPU_epoch_10.jpg)

epoch = 298: 
![alt text](C:\Users\tugsu\Pictures\Screenshots\CPU_epoch_298.jpg)
"C:\Users\tugsu\AppData\Local\Programs\Python\Python312\python.exe" -m pip install ultralytics>=8.3.0 –no-cache-dir

"C:\Users\tugsu\AppData\Local\Programs\Python\Python312\python.exe" -m ultralytics predict model=buuz_runs\yolo11s_60photos\weights\best.pt source=test.jpg conf=0.4 save=True


Ажиллуулах
"C:\Users\tugsu\AppData\Local\Programs\Python\Python312\python.exe" "C:\Users\tugsu\Desktop\a\hicheel\2025-2026 namar\AI\FinalProject\Count_my_buuz.py"

magick mogrify -auto-orient *.jpg

pyTorch GPU ашиглах/татах
"C:\Users\tugsu\AppData\Local\Programs\Python\Python312\python.exe" -m pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

"C:\Users\tugsu\AppData\Local\Programs\Python\Python312\python.exe" -m pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

Model (GPU) сургах
yolo train model=yolo11s.pt data="C:\Users\tugsu\Desktop\a\hicheel\2025-2026 namar\AI\FinalProject\Data\data.yaml" epochs=300 imgsz=640 batch=8 patience=40 freeze=10 amp=True project=buuz_runs name=yolo11s_gpu_fast exist_ok=True

yolo train model=yolo11s.pt data=data.yaml epochs=300 imgsz=640 batch=8 patience=40 freeze=10 amp=True project=buuz_runs name=yolo11s_gpu_fast exist_ok=True
