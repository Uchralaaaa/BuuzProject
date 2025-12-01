from ultralytics import YOLO
import cv2
import os

# Surgasan hamgiin shildeg modeliin zamaa hiih
model = YOLO(r"buuz_runs\yolo11s_rtx5090\weights\best.pt")  

def count_buuz(image_path):
    # Ymar ch path baisan Windows deer ajillah bolomjtoi bolgoh
    image_path = os.path.expanduser(image_path)
    
    img = cv2.imread(image_path)
    if img is None:
        print(f"Zurgiig unshij chadsangui!: {image_path}")
        return
    
    results = model(img, conf=0.5, iou=0.37)[0]
    num = len(results.boxes)
    
    print(f"Detected {num} бууз ! → {os.path.basename(image_path)}")
    
    annotated = results.plot()
    cv2.putText(annotated, f"BUUZ = {num}", (70, 150),
                cv2.FONT_HERSHEY_SIMPLEX, 5, (0, 255, 0), 10)
    
    output_path = image_path.replace(".", "_counted.")
    cv2.imwrite(output_path, annotated)
    print(f"Saved → {output_path}\n")


# Zamaa zaaj uguud function-oo ajilluulah
count_buuz(r"C:\Users\tugsu\Desktop\a\hicheel\2025-2026 namar\AI\FinalProject\Data\588603512_1566298998020793_8862663010305376630_n.jpg")
count_buuz(r"C:\Users\tugsu\Desktop\a\hicheel\2025-2026 namar\AI\FinalProject\Data\591311740_1293583872783438_6324046172971033690_n.jpg")
count_buuz(r"C:\Users\tugsu\Desktop\a\hicheel\2025-2026 namar\AI\FinalProject\Data\592183752_1185985893501253_8349152003096402615_n.jpg")

# Zurag nemeheer bol
count_buuz(r"C:\Users\tugsu\Desktop\a\hicheel\2025-2026 namar\AI\FinalProject\Data\buuz_new_phone.jpg")